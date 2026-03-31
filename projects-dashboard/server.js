import express from 'express';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const app = express();
const PORT = process.env.PORT || 3000;
const HOST = process.env.HOST || '0.0.0.0';
const dataPath = path.join(__dirname, 'data', 'projects.json');
const dashboardPassword = process.env.DASHBOARD_PASSWORD || '';

app.use(express.json());
app.use('/static', express.static(path.join(__dirname, 'static')));

function loadProjects() {
  const raw = fs.readFileSync(dataPath, 'utf8');
  return JSON.parse(raw);
}

function saveProjects(data) {
  fs.writeFileSync(dataPath, JSON.stringify(data, null, 2));
}

function isAuthorized(req) {
  if (!dashboardPassword) return true;
  const supplied = req.headers['x-dashboard-password'];
  return supplied && supplied === dashboardPassword;
}

function rejectIfUnauthorized(req, res, next) {
  if (!isAuthorized(req)) {
    return res.status(401).json({ error: 'unauthorized' });
  }
  next();
}

function normalizeProject(project) {
  return {
    id: project.id,
    name: project.name,
    status: project.status || 'planning',
    semaphore: project.semaphore || 'yellow',
    updatedAt: project.updatedAt || new Date().toISOString().slice(0, 10),
    summary: project.summary || '',
    tags: Array.isArray(project.tags) ? project.tags : [],
    nextSteps: Array.isArray(project.nextSteps) ? project.nextSteps : [],
    blockers: Array.isArray(project.blockers) ? project.blockers : [],
    stalledByLuis: Boolean(project.stalledByLuis),
    stalledReason: project.stalledReason || '',
    activities: Array.isArray(project.activities) ? project.activities : []
  };
}

app.get('/api/health', (_req, res) => {
  res.json({ ok: true });
});

app.get('/api/projects', rejectIfUnauthorized, (_req, res) => {
  res.json(loadProjects());
});

app.post('/api/projects', rejectIfUnauthorized, (req, res) => {
  const data = loadProjects();
  const project = req.body;

  if (!project.id || !project.name) {
    return res.status(400).json({ error: 'id and name are required' });
  }

  if (data.projects.find((p) => p.id === project.id)) {
    return res.status(409).json({ error: 'project id already exists' });
  }

  const newProject = normalizeProject(project);
  newProject.updatedAt = new Date().toISOString().slice(0, 10);

  data.projects.push(newProject);
  saveProjects(data);
  res.status(201).json(newProject);
});

app.post('/api/projects/:id/activities', rejectIfUnauthorized, (req, res) => {
  const data = loadProjects();
  const project = data.projects.find((p) => p.id === req.params.id);

  if (!project) {
    return res.status(404).json({ error: 'project not found' });
  }

  const activity = {
    date: req.body.date || new Date().toISOString().slice(0, 10),
    title: req.body.title || 'Update',
    note: req.body.note || ''
  };

  project.activities.unshift(activity);
  project.updatedAt = activity.date;
  if (req.body.status) project.status = req.body.status;
  if (req.body.semaphore) project.semaphore = req.body.semaphore;
  if (typeof req.body.summary === 'string') project.summary = req.body.summary;

  saveProjects(data);
  res.status(201).json(activity);
});

app.patch('/api/projects/:id', rejectIfUnauthorized, (req, res) => {
  const data = loadProjects();
  const project = data.projects.find((p) => p.id === req.params.id);

  if (!project) {
    return res.status(404).json({ error: 'project not found' });
  }

  if (typeof req.body.name === 'string') project.name = req.body.name;
  if (typeof req.body.status === 'string') project.status = req.body.status;
  if (typeof req.body.semaphore === 'string') project.semaphore = req.body.semaphore;
  if (typeof req.body.summary === 'string') project.summary = req.body.summary;
  if (Array.isArray(req.body.tags)) project.tags = req.body.tags;
  if (Array.isArray(req.body.nextSteps)) project.nextSteps = req.body.nextSteps;
  if (Array.isArray(req.body.blockers)) project.blockers = req.body.blockers;
  if (typeof req.body.stalledByLuis === 'boolean') project.stalledByLuis = req.body.stalledByLuis;
  if (typeof req.body.stalledReason === 'string') project.stalledReason = req.body.stalledReason;
  project.updatedAt = new Date().toISOString().slice(0, 10);

  saveProjects(data);
  res.json(project);
});

app.get('/', (_req, res) => {
  const html = fs.readFileSync(path.join(__dirname, 'static', 'index.html'), 'utf8');
  res.type('html').send(html);
});

app.listen(PORT, HOST, () => {
  console.log(`Projects dashboard running on http://${HOST}:${PORT}`);
});

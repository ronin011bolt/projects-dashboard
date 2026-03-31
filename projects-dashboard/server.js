import express from 'express';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const app = express();
const PORT = process.env.PORT || 3000;
const dataPath = path.join(__dirname, 'data', 'projects.json');

app.use(express.json());
app.use('/static', express.static(path.join(__dirname, 'static')));

function loadProjects() {
  const raw = fs.readFileSync(dataPath, 'utf8');
  return JSON.parse(raw);
}

function saveProjects(data) {
  fs.writeFileSync(dataPath, JSON.stringify(data, null, 2));
}

app.get('/api/projects', (_req, res) => {
  res.json(loadProjects());
});

app.post('/api/projects', (req, res) => {
  const data = loadProjects();
  const project = req.body;

  if (!project.id || !project.name) {
    return res.status(400).json({ error: 'id and name are required' });
  }

  if (data.projects.find((p) => p.id === project.id)) {
    return res.status(409).json({ error: 'project id already exists' });
  }

  data.projects.push({
    id: project.id,
    name: project.name,
    status: project.status || 'planning',
    updatedAt: project.updatedAt || new Date().toISOString().slice(0, 10),
    summary: project.summary || '',
    activities: Array.isArray(project.activities) ? project.activities : []
  });

  saveProjects(data);
  res.status(201).json(project);
});

app.get('/', (_req, res) => {
  const html = fs.readFileSync(path.join(__dirname, 'static', 'index.html'), 'utf8');
  res.type('html').send(html);
});

app.listen(PORT, () => {
  console.log(`Projects dashboard running on port ${PORT}`);
});

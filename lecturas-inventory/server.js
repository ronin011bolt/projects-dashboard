import express from 'express';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const app = express();
const PORT = process.env.PORT || 3010;
const HOST = process.env.HOST || '0.0.0.0';
const dashboardPassword = process.env.DASHBOARD_PASSWORD || '';
const dataPath = path.join(__dirname, 'data', 'index.json');

app.use(express.json());
app.use('/static', express.static(path.join(__dirname, 'static')));

function loadIndex() {
  return JSON.parse(fs.readFileSync(dataPath, 'utf8'));
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

app.get('/api/health', (_req, res) => res.json({ ok: true }));
app.get('/api/index', rejectIfUnauthorized, (_req, res) => res.json(loadIndex()));
app.get('/', (_req, res) => {
  res.type('html').send(fs.readFileSync(path.join(__dirname, 'static', 'index.html'), 'utf8'));
});

app.listen(PORT, HOST, () => {
  console.log(`Reading Index running on http://${HOST}:${PORT}`);
});

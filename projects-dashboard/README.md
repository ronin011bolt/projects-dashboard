# Projects Dashboard

Private dashboard to track multiple projects separately.

## What it does

- Keeps each project isolated in the data model
- Shows status, summary, tags, and activity log per project
- Lets you create projects from the UI
- Lets you add activity updates from the UI
- Supports a simple private password gate
- Ready to deploy on Railway

## Local run

```bash
cd projects-dashboard
npm install
cp .env.example .env
npm run dev
```

Open: http://localhost:3000

Optional local env:

```bash
export DASHBOARD_PASSWORD=your-password
```

## Railway deploy

1. Create a new Railway project
2. Connect this repo/folder
3. Add an environment variable:
   - `DASHBOARD_PASSWORD=your-private-password`
4. Keep the example projects or replace `data/projects.json` later with real ones
5. Deploy using the included `railway.json`

## Data

Project data lives in:

- `data/projects.json`

Each project has:

- `id`
- `name`
- `status`
- `updatedAt`
- `summary`
- `tags[]`
- `activities[]`

## Current limits

- Password protection is simple and lightweight, not enterprise auth
- Data is stored in JSON, not a database
- Good for phase 1 private operations, but should later move to a proper DB + stronger auth

## Good next improvements

- Edit and archive projects from the UI
- Per-project milestones
- Search
- Database persistence
- Proper authentication layer

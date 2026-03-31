# Projects Dashboard

Private dashboard to track multiple projects separately.

## What it does

- Keeps each project isolated in the data model
- Shows status, summary, and activity log per project
- Ready to deploy on Railway

## Local run

```bash
cd projects-dashboard
npm install
npm run dev
```

Open: http://localhost:3000

## Railway deploy

1. Create a new Railway project
2. Connect this repo/folder
3. Deploy using the included `railway.json`

## Data

Project data lives in:

- `data/projects.json`

Each project has:

- `id`
- `name`
- `status`
- `updatedAt`
- `summary`
- `activities[]`

## Next improvements

- Add project creation/edit UI
- Add filters and tags
- Add auth for private access
- Persist via a database instead of JSON

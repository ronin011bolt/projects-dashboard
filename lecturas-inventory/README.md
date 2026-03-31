# Lecturas Inventory

Private dashboard to index and search the `lecturas` corpus.

## Goals

- inventory documents, reports, papers, decks, and media
- preserve folder/topic structure
- create a fast searchable index
- support future classification and metadata enrichment

## Current approach

- source corpus stays in place at `~/Desktop/lecturas`
- Python script builds a JSON inventory
- Node/Express app serves a searchable dashboard

## Commands

```bash
cd lecturas-inventory
npm install
npm run index
npm start
```

For local-network access:

```bash
cd lecturas-inventory
./scripts/start-network.sh
```

## Environment

- `LECTURAS_ROOT` → root folder of the corpus
- `DASHBOARD_PASSWORD` → optional dashboard password

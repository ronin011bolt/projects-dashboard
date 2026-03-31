#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
export HOST=0.0.0.0
export PORT="${PORT:-3010}"
npm start

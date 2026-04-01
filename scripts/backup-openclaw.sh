#!/usr/bin/env bash
set -euo pipefail

STAMP="$(date +%Y%m%d-%H%M%S)"
SRC="$HOME/.openclaw"
DEST_ROOT="${1:-$HOME/Desktop/openclaw-backups}"
DEST_DIR="$DEST_ROOT/openclaw-backup-$STAMP"
ARCHIVE="$DEST_DIR/openclaw-home-$STAMP.tar.gz"
MANIFEST="$DEST_DIR/manifest.txt"
CHECKSUMS="$DEST_DIR/sha256.txt"
STATUS_OUT="$DEST_DIR/openclaw-status.txt"
UPDATE_OUT="$DEST_DIR/openclaw-update-status.txt"
AUDIT_OUT="$DEST_DIR/openclaw-security-audit.txt"

mkdir -p "$DEST_DIR"

if [[ ! -d "$SRC" ]]; then
  echo "Source directory not found: $SRC" >&2
  exit 1
fi

echo "Creating archive..."
tar -czf "$ARCHIVE" -C "$HOME" .openclaw

echo "Writing manifest..."
{
  echo "OpenClaw backup manifest"
  echo "Created: $(date -Iseconds)"
  echo "Source: $SRC"
  echo "Archive: $ARCHIVE"
  echo
  echo "Top-level contents:"
  find "$SRC" -maxdepth 2 | sed "s#^$HOME#~#" | sort
} > "$MANIFEST"

echo "Writing checksums..."
(
  cd "$DEST_DIR"
  shasum -a 256 "$(basename "$ARCHIVE")" > "$CHECKSUMS"
)

echo "Capturing diagnostics where available..."
if command -v openclaw >/dev/null 2>&1; then
  openclaw status > "$STATUS_OUT" 2>&1 || true
  openclaw update status > "$UPDATE_OUT" 2>&1 || true
  openclaw security audit > "$AUDIT_OUT" 2>&1 || true
else
  echo "openclaw command not found" > "$STATUS_OUT"
  echo "openclaw command not found" > "$UPDATE_OUT"
  echo "openclaw command not found" > "$AUDIT_OUT"
fi

echo
printf 'Backup created:\n%s\n' "$ARCHIVE"
printf 'Manifest:\n%s\n' "$MANIFEST"
printf 'Checksums:\n%s\n' "$CHECKSUMS"
printf 'Diagnostics:\n- %s\n- %s\n- %s\n' "$STATUS_OUT" "$UPDATE_OUT" "$AUDIT_OUT"

echo
printf 'Next step: verify the archive and copy %s to a second location if possible.\n' "$DEST_DIR"

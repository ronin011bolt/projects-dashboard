#!/usr/bin/env python3
import json
import os
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(os.environ.get('LECTURAS_ROOT', '/Users/ronin/Desktop/lecturas')).expanduser()
OUT = Path(__file__).resolve().parent.parent / 'data' / 'index.json'

SKIP_EXTENSIONS = {'.ds_store'}
SKIP_DIRS = {'.git', 'node_modules'}


def guess_tags(parts, name):
    tags = []
    lowered = ' '.join(parts + [name]).lower()
    mapping = {
        'ai': ['ai'],
        'disinformation': ['disinformation'],
        'propaganda': ['propaganda'],
        'osint': ['osint'],
        'cybersecurity': ['cybersecurity'],
        'privacy': ['privacy'],
        'journalism': ['journalism'],
        'hate speech': ['hate-speech'],
        'harassment': ['harassment'],
        'extremism': ['extremism'],
        'radicalizacion': ['extremism'],
        'surveillance': ['surveillance'],
        'censorship': ['censorship'],
        'internet': ['internet'],
        'psyops': ['psyops'],
        'public policy': ['policy'],
        'content moderation': ['content-moderation'],
        'encryption messaging apps': ['messaging-apps'],
        'opsec': ['opsec']
    }
    for key, values in mapping.items():
        if key in lowered:
            tags.extend(values)
    return sorted(set(tags))


def main():
    docs = []
    by_ext = Counter()
    by_top = Counter()

    if not ROOT.exists():
        raise SystemExit(f'Root folder does not exist: {ROOT}')

    for path in ROOT.rglob('*'):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        rel = path.relative_to(ROOT)
        ext = path.suffix.lower().lstrip('.') or 'noext'
        if ext in SKIP_EXTENSIONS:
            continue
        parts = list(rel.parts)
        top_level = parts[0] if parts else ''
        stat = path.stat()
        docs.append({
            'id': str(rel).lower().replace(' ', '-').replace('/', '__'),
            'name': path.name,
            'relativePath': str(rel),
            'topLevel': top_level,
            'folderPath': '/'.join(parts[:-1]),
            'extension': ext,
            'sizeBytes': stat.st_size,
            'modifiedAt': datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc).isoformat(),
            'tags': guess_tags(parts[:-1], path.stem),
            'notes': '',
            'kind': 'document' if ext in {'pdf', 'doc', 'docx', 'txt', 'ppt', 'pptx', 'key'} else 'media' if ext in {'jpg', 'jpeg', 'png', 'gif', 'heic', 'mov', 'wav', 'wmv'} else 'other'
        })
        by_ext[ext] += 1
        by_top[top_level] += 1

    payload = {
        'generatedAt': datetime.now(timezone.utc).isoformat(),
        'root': str(ROOT),
        'stats': {
            'totalFiles': len(docs),
            'byExtension': dict(sorted(by_ext.items(), key=lambda kv: (-kv[1], kv[0]))),
            'byTopLevel': dict(sorted(by_top.items(), key=lambda kv: (-kv[1], kv[0])))
        },
        'documents': sorted(docs, key=lambda d: d['relativePath'].lower())
    }

    OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f'Indexed {len(docs)} files into {OUT}')


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
import hashlib
import json
import os
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(os.environ.get('LECTURAS_ROOT', '/Users/ronin/Desktop/Reading  Index')).expanduser()
OUT = Path(__file__).resolve().parent.parent / 'data' / 'index.json'

SKIP_EXTENSIONS = {'.ds_store'}
SKIP_DIRS = {'.git', 'node_modules'}


def file_hash(path, chunk_size=1024 * 1024):
    h = hashlib.sha1()
    with path.open('rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


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
        'opsec': ['opsec'],
        'far right': ['far-right'],
        'democracy': ['democracy'],
        'election': ['elections'],
        'troll': ['trolling'],
        'ransomware': ['ransomware'],
        'telegram': ['telegram'],
        'signal': ['signal'],
        'whatsapp': ['whatsapp']
    }
    for key, values in mapping.items():
        if key in lowered:
            tags.extend(values)
    return sorted(set(tags))


def detect_language(text):
    lowered = text.lower()
    score_es = sum(token in lowered for token in [' informe ', ' para ', ' y ', ' de ', ' la ', ' el ', ' una ', ' sobre '])
    score_en = sum(token in lowered for token in [' the ', ' and ', ' of ', ' report ', ' for ', ' in ', ' on '])
    if score_es > score_en and score_es > 1:
        return 'es'
    if score_en > score_es and score_en > 1:
        return 'en'
    return 'unknown'


def classify_format(ext, name):
    lowered = name.lower()
    if ext in {'pdf', 'doc', 'docx', 'txt', 'rtf'}:
        if 'report' in lowered or 'informe' in lowered:
            return 'report'
        if 'guide' in lowered or 'toolkit' in lowered or 'manual' in lowered:
            return 'guide'
        if 'brief' in lowered:
            return 'brief'
        if 'proposal' in lowered:
            return 'proposal'
        if 'complaint' in lowered or 'ley' in lowered or 'law' in lowered:
            return 'legal-policy'
        return 'document'
    if ext in {'ppt', 'pptx', 'key', 'pps'}:
        return 'presentation'
    if ext in {'jpg', 'jpeg', 'png', 'gif', 'heic'}:
        return 'image'
    if ext in {'mov', 'wav', 'wmv'}:
        return 'media'
    if ext in {'xls', 'xlsx', 'dbf', 'db'}:
        return 'dataset'
    return 'other'


def initial_triage(doc_format, is_duplicate):
    if is_duplicate:
        return 'review'
    if doc_format in {'report', 'guide', 'brief', 'legal-policy', 'presentation', 'dataset'}:
        return 'keep'
    return 'review'


def main():
    docs = []
    by_ext = Counter()
    by_top = Counter()
    hash_groups = defaultdict(list)

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
        digest = file_hash(path) if stat.st_size <= 50 * 1024 * 1024 else None
        if digest:
            hash_groups[digest].append(str(rel))
        doc_kind = 'document' if ext in {'pdf', 'doc', 'docx', 'txt', 'ppt', 'pptx', 'key'} else 'media' if ext in {'jpg', 'jpeg', 'png', 'gif', 'heic', 'mov', 'wav', 'wmv'} else 'other'
        doc_format = classify_format(ext, path.name)
        language = detect_language(f" {' '.join(parts[:-1])} {path.stem} ")
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
            'language': language,
            'format': doc_format,
            'triage': 'review',
            'notes': '',
            'duplicateGroup': digest,
            'kind': doc_kind
        })
        by_ext[ext] += 1
        by_top[top_level] += 1

    duplicate_groups = {k: v for k, v in hash_groups.items() if len(v) > 1}
    duplicate_paths = {p for paths in duplicate_groups.values() for p in paths}
    triage_counter = Counter()
    format_counter = Counter()
    language_counter = Counter()
    for doc in docs:
        doc['isPossibleDuplicate'] = doc['relativePath'] in duplicate_paths
        doc['triage'] = initial_triage(doc['format'], doc['isPossibleDuplicate'])
        triage_counter[doc['triage']] += 1
        format_counter[doc['format']] += 1
        language_counter[doc['language']] += 1

    payload = {
        'generatedAt': datetime.now(timezone.utc).isoformat(),
        'root': str(ROOT),
        'stats': {
            'totalFiles': len(docs),
            'possibleDuplicateFiles': len(duplicate_paths),
            'duplicateGroups': len(duplicate_groups),
            'byExtension': dict(sorted(by_ext.items(), key=lambda kv: (-kv[1], kv[0]))),
            'byTopLevel': dict(sorted(by_top.items(), key=lambda kv: (-kv[1], kv[0]))),
            'byFormat': dict(sorted(format_counter.items(), key=lambda kv: (-kv[1], kv[0]))),
            'byLanguage': dict(sorted(language_counter.items(), key=lambda kv: (-kv[1], kv[0]))),
            'byTriage': dict(sorted(triage_counter.items(), key=lambda kv: (-kv[1], kv[0])))
        },
        'duplicateGroups': duplicate_groups,
        'documents': sorted(docs, key=lambda d: d['relativePath'].lower())
    }

    OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f'Indexed {len(docs)} files into {OUT}')
    print(f'Possible duplicate files: {len(duplicate_paths)} in {len(duplicate_groups)} groups')


if __name__ == '__main__':
    main()

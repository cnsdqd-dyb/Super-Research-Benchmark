"""Offline tools for Super Research questions and report collections."""
import argparse
import collections
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data'

def read_rows(path):
    with Path(path).open(encoding='utf-8-sig') as f:
        return [json.loads(line) for line in f if line.strip()]

def write_rows(path, rows):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', encoding='utf-8') as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False, allow_nan=False) + '\n')

def questions():
    return read_rows(DATA / 'questions.jsonl')

def verify():
    hashes = json.loads((DATA / 'checksums.json').read_text(encoding='utf-8'))
    for name, expected in hashes.items():
        path = (DATA / name).resolve()
        if not path.is_relative_to(DATA.resolve()):
            raise ValueError('Invalid checksum path')
        if hashlib.sha256(path.read_bytes()).hexdigest() != expected:
            raise ValueError(f'Content hash mismatch: {name}')
    qs = questions()
    ids = {q['task_id'] for q in qs}
    if len(qs) != 300 or len(ids) != 300:
        raise ValueError('Expected 300 unique questions')
    for q in qs:
        if hashlib.sha256(q['question'].encode()).hexdigest() != q['question_sha256']:
            raise ValueError('Question hash mismatch: ' + q['task_id'])
    systems = json.loads((DATA / 'systems.json').read_text(encoding='utf-8'))
    reports = read_rows(DATA / 'report_manifest.jsonl')
    counts = collections.defaultdict(set)
    for r in reports:
        if r['task_id'] in counts[r['system_id']]:
            raise ValueError('Duplicate report')
        counts[r['system_id']].add(r['task_id'])
        body = DATA / r['report_path']
        if hashlib.sha256(body.read_bytes()).hexdigest() != r['report_sha256']:
            raise ValueError('Report hash mismatch')
    if set(counts) != {s['system_id'] for s in systems} or any(tasks != ids for tasks in counts.values()):
        raise ValueError('Incomplete system report collection')
    return {'questions': len(qs), 'systems': len(systems), 'reports': len(reports), 'verified_files': len(hashes)}

def validate(path, complete=False):
    qs = {q['task_id']: q for q in questions()}
    rows = read_rows(path)
    if not rows:
        raise ValueError('Report collection is empty')
    seen = set()
    per_system = collections.Counter()
    for index, row in enumerate(rows, 1):
        task, system = row.get('task_id'), row.get('system_id')
        if task not in qs or not isinstance(system, str) or not system.strip():
            raise ValueError(f'Invalid task or system at row {index}')
        if row.get('question_sha256') != qs[task]['question_sha256']:
            raise ValueError(f'Question hash mismatch at row {index}')
        if not isinstance(row.get('report_text'), str) or not row['report_text'].strip():
            raise ValueError(f'Empty report at row {index}')
        if (system, task) in seen:
            raise ValueError(f'Duplicate system/task at row {index}')
        seen.add((system, task))
        per_system[system] += 1
    if complete and any(n != len(qs) for n in per_system.values()):
        raise ValueError('Complete validation requires 300 reports per system')
    return {'validated_reports': len(rows), 'tasks_per_system': dict(per_system)}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('verify')
    sub.add_parser('stats')
    task_parser = sub.add_parser('tasks')
    task_parser.add_argument('--limit', type=int, default=300)
    task_parser.add_argument('--output', required=True, type=Path)
    export_parser = sub.add_parser('export')
    export_parser.add_argument('--system', required=True)
    export_parser.add_argument('--output', required=True, type=Path)
    validate_parser = sub.add_parser('validate')
    validate_parser.add_argument('--input', required=True, type=Path)
    validate_parser.add_argument('--require-complete', action='store_true')
    args = parser.parse_args()
    if args.command == 'verify':
        result = verify()
    elif args.command == 'stats':
        qs = questions()
        result = {'questions': len(qs), 'domains': dict(collections.Counter(q['domain'] for q in qs)), 'systems': json.loads((DATA / 'systems.json').read_text(encoding='utf-8'))}
    elif args.command == 'tasks':
        if not 1 <= args.limit <= 300:
            raise ValueError('Limit must be between 1 and 300')
        write_rows(args.output, questions()[:args.limit])
        result = {'exported_tasks': args.limit, 'output': str(args.output)}
    elif args.command == 'export':
        qs = {q['task_id']: q for q in questions()}
        records = [r for r in read_rows(DATA / 'report_manifest.jsonl') if r['system_id'] == args.system]
        if not records:
            raise ValueError('Unknown system: ' + args.system)
        output = []
        for r in records:
            output.append({'task_id': r['task_id'], 'system_id': r['system_id'], 'question_sha256': qs[r['task_id']]['question_sha256'], 'report_text': (DATA / r['report_path']).read_text(encoding='utf-8-sig'), 'model': r['model'], 'report_input': r['report_input'], 'report_input_sha256': r['report_input_sha256']})
        write_rows(args.output, output)
        result = {'exported_reports': len(output), 'output': str(args.output)}
    else:
        result = validate(args.input, args.require_complete)
    print(json.dumps(result, ensure_ascii=True, indent=2))

if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, KeyError, TypeError) as exc:
        print(f'Error: {exc}', file=sys.stderr)
        sys.exit(1)

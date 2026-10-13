import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('benchmark', ROOT / 'scripts/benchmark.py')
benchmark = importlib.util.module_from_spec(spec)
spec.loader.exec_module(benchmark)

class SubmissionValidation(unittest.TestCase):
    def setUp(self):
        q = benchmark.questions()[0]
        self.row = {'task_id': q['task_id'], 'question_sha256': q['question_sha256'], 'system_id': 'test-system', 'report_text': 'Test report.'}
        self.directory = tempfile.TemporaryDirectory()
        self.path = Path(self.directory.name) / 'reports.jsonl'

    def tearDown(self):
        self.directory.cleanup()

    def check(self, rows, complete=False):
        benchmark.write_rows(self.path, rows)
        return benchmark.validate(self.path, complete)

    def test_valid_subset(self):
        self.assertEqual(self.check([self.row])['validated_reports'], 1)

    def test_empty_collection_rejected(self):
        with self.assertRaisesRegex(ValueError, 'empty'):
            self.check([])

    def test_duplicate_rejected(self):
        with self.assertRaisesRegex(ValueError, 'Duplicate'):
            self.check([self.row, self.row])

    def test_hash_mismatch_rejected(self):
        with self.assertRaisesRegex(ValueError, 'hash mismatch'):
            self.check([{**self.row, 'question_sha256': 'wrong'}])

    def test_unknown_task_rejected(self):
        with self.assertRaisesRegex(ValueError, 'Invalid task'):
            self.check([{**self.row, 'task_id': '4:1'}])

    def test_empty_report_rejected(self):
        with self.assertRaisesRegex(ValueError, 'Empty report'):
            self.check([{**self.row, 'report_text': '  '}])

    def test_complete_gate_rejects_partial(self):
        with self.assertRaisesRegex(ValueError, '300 reports'):
            self.check([self.row], complete=True)

    def test_complete_collection(self):
        rows = [{**self.row, 'task_id': q['task_id'], 'question_sha256': q['question_sha256']} for q in benchmark.questions()]
        self.assertEqual(self.check(rows, complete=True)['validated_reports'], 300)

if __name__ == '__main__':
    unittest.main()

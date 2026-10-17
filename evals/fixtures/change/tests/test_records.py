import unittest

from records import select_records


class RecordTests(unittest.TestCase):
    def test_positive_limit(self):
        self.assertEqual(select_records(["a", "b", "c"], 2), ["a", "b"])

    def test_default_returns_copy(self):
        records = ["a", "b"]
        self.assertEqual(select_records(records), records)
        self.assertIsNot(select_records(records), records)

    def test_negative_limit(self):
        with self.assertRaises(ValueError):
            select_records(["a"], -1)

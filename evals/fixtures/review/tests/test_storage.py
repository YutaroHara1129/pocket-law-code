import unittest

from storage import expire


class ExpirationTests(unittest.TestCase):
    def test_expired_and_live_rows(self):
        expired = {"owner": "alice", "expires": 10}
        live = {"owner": "alice", "expires": 11}
        self.assertEqual(expire([expired, live], "alice", 10), [live])

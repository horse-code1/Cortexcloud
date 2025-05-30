# tests/test_ethics_resolver.py

import unittest
from modules.ethics_resolver import rewrite_unethical_fork

class TestEthicsResolver(unittest.TestCase):
    def test_rewrite(self):
        fork = {"mutation": {"proposed_change": "violate ethics", "ethics_violation": True}}
        revised = rewrite_unethical_fork(fork)
        self.assertIn("resolved", revised)

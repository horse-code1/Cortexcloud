# tests/test_fingerprint_engine.py

import unittest
from modules.fingerprint_engine import hash_file

class TestFingerprintEngine(unittest.TestCase):
    def test_hash_file(self):
        hash_val = hash_file("cortex_brain/soul.yaml")
        self.assertEqual(len(hash_val), 64)

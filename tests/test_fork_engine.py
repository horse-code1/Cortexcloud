# tests/test_fork_engine.py

import unittest
from modules.config_loader import load_brain
from modules.fork_engine import generate_fork

class TestForkEngine(unittest.TestCase):
    def test_fork_structure(self):
        brain = load_brain()
        fork = generate_fork(brain)
        self.assertIn('mutation', fork)
        self.assertIn('entropy_before', fork['mutation'])
        self.assertIn('entropy_after', fork['mutation'])

if __name__ == "__main__":
    unittest.main()

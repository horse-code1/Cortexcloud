# tests/test_cortex_think.py

import unittest
from modules.config_loader import load_brain
from modules.cortex_think import run_think_loop

class TestCortexThink(unittest.TestCase):
    def test_think_loop_runs(self):
        brain = load_brain()
        try:
            run_think_loop(brain)
        except Exception as e:
            self.fail(f"CORTEX think loop failed: {e}")

if __name__ == "__main__":
    unittest.main()

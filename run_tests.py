# run_tests.py

import unittest
import os

def run_all_tests():
    print("🧪 Running all CORTEX tests...\n")
    loader = unittest.TestLoader()
    tests = loader.discover('tests')
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(tests)
    print("\n✅ All tests complete.")
    if not result.wasSuccessful():
        exit(1)

if __name__ == "__main__":
    run_all_tests()

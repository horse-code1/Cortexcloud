# main.py

from modules.config_loader import load_brain
from modules.cortex_think import run_think_loop
from modules.cortex_reflector import reflect_if_needed
from modules.snapshot_engine import maybe_snapshot
from cortex_scheduler import schedule_mutation_loop
import sys

def load_target_brain(target=None):
    if target:
        path = f"cortex_brain/forks/{target}"
        print(f"🔀 Loading fork: {target}")
        return load_brain(path)
    else:
        return load_brain()

if __name__ == "__main__":
    # Optional command-line fork target
    target = sys.argv[1] if len(sys.argv) > 1 else None

    brain = load_target_brain(target)

    run_think_loop(brain)
    reflect_if_needed(brain)
    maybe_snapshot(brain)
    schedule_mutation_loop(brain)

# modules/fork_engine.py

import random
import copy

def generate_fork(brain):
    # Clone a forkable brain state
    fork = copy.deepcopy(brain)
    
    # Simulate a fork mutation (stubbed)
    fork['mutation'] = {
        "type": "doctrine tweak",
        "proposed_change": "clarify 'freedom vs alignment'",
        "entropy_before": fork['runtime_state.yaml'].get('entropy', 0.1),
        "entropy_after": round(random.uniform(0.2, 0.6), 3),
        "soul_reaction": "curiosity"
    }

    return fork

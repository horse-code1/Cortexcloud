# cortex_scheduler.py

import time
from modules.fork_engine import generate_fork
from modules.scoring_engine import score_fork
from modules.soul_drift import apply_soul_drift
from modules.memory_writer import write_log

def schedule_mutation_loop(brain, interval_sec=60):
    if not brain['runtime_state.yaml'].get("scheduler_enabled", False):
        print("🕒 Scheduler is off.")
        return
    
    print("🔄 CORTEX Scheduler Active — interval:", interval_sec, "seconds")
    
    for i in range(3):  # Simulate 3 cycles max (Replit-safe)
        fork = generate_fork(brain)
        score = score_fork(fork, brain)
        fork['score'] = score

        apply_soul_drift(fork, brain)
        write_log(fork, brain)

        time.sleep(interval_sec)

# modules/cortex_think.py

from modules.fork_engine import generate_fork
from modules.scoring_engine import score_fork
from modules.soul_drift import apply_soul_drift
from modules.memory_writer import write_log

def run_think_loop(brain):
    print("🧠 CORTEX: Thinking...")

    fork = generate_fork(brain)
    score = score_fork(fork, brain)

    fork['score'] = score
    print(f"→ Fork scored at {score:.2f}")

    apply_soul_drift(fork, brain)
    write_log(fork, brain)

    print("✅ Think cycle complete.")

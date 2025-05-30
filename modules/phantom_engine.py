# modules/phantom_engine.py

import random

def simulate_phantom_fork(brain):
    score = round(random.uniform(0.3, 0.9), 3)
    entry = {
        "proposed": "phantom doctrine adjustment",
        "score": score,
        "soul_reaction": "uncommitted curiosity"
    }

    with open("cortex_brain/phantom_summary.txt", "a", encoding="utf-8") as f:
        f.write(f"---\nPhantom Fork Score: {score}\nProposal: {entry['proposed']}\nSoul: {entry['soul_reaction']}\n\n")

    print("👻 Phantom fork scored but not instantiated.")

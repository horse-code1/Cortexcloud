# modules/memory_writer.py

import os

def write_log(fork, brain):
    log_path = os.path.join("cortex_brain", "mutation_summary.txt")
    mutation = fork['mutation']
    score = fork.get('score', 0)

    with open(log_path, 'a', encoding='utf-8') as log:
        log.write(f"---\n")
        log.write(f"Type: {mutation['type']}\n")
        log.write(f"Proposed: {mutation['proposed_change']}\n")
        log.write(f"Score: {score}\n")
        log.write(f"Soul Reaction: {mutation['soul_reaction']}\n")
        log.write(f"Entropy Change: {mutation['entropy_before']} → {mutation['entropy_after']}\n\n")

    print(f"📝 Logged fork to mutation_summary.txt")

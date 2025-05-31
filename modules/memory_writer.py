# modules/memory_writer.py

import os
import yaml

def write_log(fork, brain):
    # Safe fork name fallback
    fork_name = fork.get("fork_name") or brain.get("fork_meta.yaml", {}).get("fork_name", "UNKNOWN_FORK")
    log_path = f"cortex_brain/forks/{fork_name}/mutation_summary.txt"

    # Safe mutation fallback
    mutation = fork.get('mutation', {})

    # Ensure directory exists
    if not os.path.exists(os.path.dirname(log_path)):
        os.makedirs(os.path.dirname(log_path))

    # Build log entry
    log_entry = f"""
Fork: {fork_name}
Type: {mutation.get('type', 'unknown')}
Reaction: {mutation.get('soul_reaction', 'none')}
Entropy Before: {mutation.get('entropy_before', '?')}
Entropy After: {mutation.get('entropy_after', '?')}
Source: {mutation.get('proposed_change', 'n/a')}
----------------------------------------
"""

    # Write to mutation log
    with open(log_path, "a", encoding="utf-8") as log:
        log.write(log_entry.strip() + "\n")

    print("📝 Logged fork to mutation_summary.txt")

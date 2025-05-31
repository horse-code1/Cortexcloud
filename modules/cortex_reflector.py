# modules/cortex_reflector.py

import os
from cortex_doctrine_mutator import mutate_doctrine

def reflect_if_needed(brain):
    doctrine = brain['CORTEX_DOCTRINE.md']
    soul_log = brain['soul.yaml'].get('emotion_log', [])
    
    if not soul_log:
        return

    last_reaction = soul_log[-1]['reaction']
    if last_reaction in ['confusion', 'contradiction']:
        fork_name = brain['soul.yaml'].get('name', 'UNKNOWN_FORK')

        log_path = f"cortex_brain/forks/{fork_name}/reflection_log.md"
        os.makedirs(os.path.dirname(log_path), exist_ok=True)

        with open(log_path, "a", encoding="utf-8") as log:
            log.write(f"[Reflect @ reaction: {last_reaction}]\n")
            log.write("Suggested doctrine patch: clarify freedom vs alignment\n\n")

        print("🧠 Reflection triggered due to cognitive conflict.")

        # 🧠 Trigger doctrinal evolution after reflection
        try:
            mutate_doctrine(fork_name)
        except Exception as e:
            print(f"⚠️ Doctrine mutation failed: {e}")

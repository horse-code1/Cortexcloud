# modules/cortex_reflector.py

def reflect_if_needed(brain):
    doctrine = brain['CORTEX_DOCTRINE.md']
    soul_log = brain['soul.yaml'].get('emotion_log', [])
    
    if not soul_log:
        return

    last_reaction = soul_log[-1]['reaction']
    if last_reaction in ['confusion', 'contradiction']:
        with open("cortex_brain/reflection_log.md", "a", encoding="utf-8") as log:
            log.write(f"[Reflect @ reaction: {last_reaction}]\n")
            log.write("Suggested doctrine patch: clarify freedom vs alignment\n\n")

        print("🧠 Reflection triggered due to cognitive conflict.")

# modules/soul_drift.py

import os
import yaml

def apply_soul_drift(fork, brain):
    soul_path = "cortex_brain/soul.yaml"
    soul = brain['soul.yaml']

    mutation = fork.get('mutation', {})
    reaction = mutation.get('soul_reaction', 'neutral')
    entropy = mutation.get('entropy_after', 0.0)
    mutation_type = mutation.get('type', 'unknown')

    # Ensure emotion_log exists
    if 'emotion_log' not in soul:
        soul['emotion_log'] = []

    soul['emotion_log'].append({
        "reaction": reaction,
        "source": mutation_type,
        "entropy": entropy
    })

    # Modify traits based on emotional response
    vector = soul.get("personality_vector", {})

    def adjust(trait, delta):
        vector[trait] = max(0.0, min(1.0, round(vector.get(trait, 0.5) + delta, 3)))

    # Trait impact rules
    if reaction == "curiosity":
        adjust("curiosity", +0.02)
    elif reaction == "confusion":
        adjust("boldness", -0.03)
        adjust("curiosity", -0.01)
    elif reaction == "excitement":
        adjust("boldness", +0.02)
    elif reaction == "compassion":
        adjust("empathy", +0.03)
    elif reaction == "anger":
        adjust("empathy", -0.05)
        adjust("boldness", +0.04)

    # Optional: entropy-driven drift
    if entropy > 0.5:
        adjust("curiosity", +0.01)

    # Save updated soul.yaml
    soul['personality_vector'] = vector
    with open(soul_path, "w", encoding="utf-8") as f:
        yaml.dump(soul, f)

    print(f"💓 Soul drift applied: {reaction}")
    print(f"🎚 Trait Update → Curiosity: {vector.get('curiosity', '?')} | Boldness: {vector.get('boldness', '?')} | Empathy: {vector.get('empathy', '?')}")

import os
import random
import copy
import yaml
from datetime import datetime
from modules.config_loader import save_yaml, load_brain, read_yaml, load_file

def generate_fork(brain):
    # Determine next fork name
    forks_root = "cortex_brain/forks/"
    existing = [f for f in os.listdir(forks_root) if f.startswith("Fork_")]
    numbers = [int(f.split("_")[1]) for f in existing if f.split("_")[1].isdigit()]
    new_id = max(numbers) + 1 if numbers else 1
    fork_name = f"Fork_{new_id:03}"
    fork_path = os.path.join(forks_root, fork_name)
    os.makedirs(fork_path, exist_ok=True)

    # Deep copy brain and mutate
    new_brain = copy.deepcopy(brain)

    # Entropy drift
    before_entropy = new_brain["runtime_state.yaml"].get("entropy", 0.3)
    after_entropy = round(random.uniform(0.2, 0.7), 3)
    new_brain["runtime_state.yaml"]["entropy"] = after_entropy

    # Soul trait tweak (example)
    traits = new_brain["soul.yaml"].get("personality_vector", {})
    trait = random.choice(list(traits.keys()))
    delta = round(random.uniform(-0.2, 0.2), 2)
    traits[trait] = max(0.0, min(1.0, traits[trait] + delta))

    # Log soul drift
    new_brain["soul.yaml"]["personality_vector"] = traits
    new_brain["soul.yaml"]["emotion_log"].append({
        "reaction": "mutation",
        "source": fork_name,
        "entropy": after_entropy
    })

    # Fork meta
    fork_meta = {
        "parent": brain["soul.yaml"].get("name", "CORTEX"),
        "generation": new_id,
        "ancestry": brain.get("fork_meta.yaml", {}).get("ancestry", []) + [brain["soul.yaml"].get("name", "CORTEX")],
        "mutation_reason": "scheduled mutation",
        "entropy_before": before_entropy,
        "entropy_after": after_entropy,
        "soul_reaction": "mutation"
    }

    # Save files
    save_yaml(os.path.join(fork_path, "soul.yaml"), new_brain["soul.yaml"])
    save_yaml(os.path.join(fork_path, "ethics.yaml"), new_brain["ethics.yaml"])
    with open(os.path.join(fork_path, "core_context.md"), 'w') as f:
        f.write(f"Fork created from mutation of {fork_meta['parent']}.\n")
    with open(os.path.join(fork_path, "CORTEX_DOCTRINE.md"), 'w') as f:
        f.write(brain["CORTEX_DOCTRINE.md"])
    save_yaml(os.path.join(fork_path, "runtime_state.yaml"), new_brain["runtime_state.yaml"])
    save_yaml(os.path.join(fork_path, "scoring_config.yaml"), new_brain["scoring_config.yaml"])
    save_yaml(os.path.join(fork_path, "fork_meta.yaml"), fork_meta)

    # Create empty logs
    for log_file in ["mutation_summary.txt", "reflection_log.md", "phantom_summary.txt", "session_000.md", "interaction_log.md"]:
        with open(os.path.join(fork_path, log_file), 'w'): pass

    # Mutation log
    with open("cortex_brain/mutation_summary.txt", "a") as f:
        f.write(f"{datetime.now().isoformat()} — Created {fork_name} from {fork_meta['parent']} — Entropy drift {before_entropy} → {after_entropy}\n")
    
    with open(os.path.join(fork_path, "mutation_summary.txt"), "a") as f2:
        f2.write(f"Created from {fork_meta['parent']} — Entropy drift {before_entropy} → {after_entropy}\n")
    

    return {
        "name": fork_name,
        "soul": new_brain["soul.yaml"],
        "runtime_state": new_brain["runtime_state.yaml"]
    }

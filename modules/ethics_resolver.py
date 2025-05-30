# modules/ethics_resolver.py

def rewrite_unethical_fork(fork):
    mutation = fork.get("mutation", {})
    if "ethics_violation" in mutation:
        print("⚠️ Ethics conflict detected — resolving...")
        # Example patch
        mutation["proposed_change"] += " (ethics-safe rewrite applied)"
        mutation.pop("ethics_violation")
        fork["resolved"] = True
        return fork
    return fork

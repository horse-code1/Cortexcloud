# cortex_lineage.py

import os
import yaml
from collections import defaultdict

FORKS_DIR = "cortex_brain/forks/"

def load_fork_meta(fork_name):
    path = os.path.join(FORKS_DIR, fork_name, "fork_meta.yaml")
    if not os.path.exists(path):
        return None
    with open(path, 'r') as f:
        return yaml.safe_load(f)

def build_lineage_tree():
    tree = defaultdict(list)
    generations = {}

    for fork in sorted(os.listdir(FORKS_DIR)):
        meta = load_fork_meta(fork)
        if not meta:
            continue
        parent = meta.get("parent", "CORTEX")
        tree[parent].append(fork)
        generations[fork] = meta.get("generation", 0)

    return tree, generations

def display_tree(tree, current, indent=0):
    if current != "CORTEX":
        print("    " * indent + f"↳ {current}")
    for child in sorted(tree.get(current, [])):
        display_tree(tree, child, indent + 1)

if __name__ == "__main__":
    print("\n🌿 CORTEX Fork Lineage\n")
    tree, gens = build_lineage_tree()
    # Start from topmost parent(s) with no parents of their own
roots = set(tree.keys()) - {c for children in tree.values() for c in children}
for root in sorted(roots):
    display_tree(tree, root)



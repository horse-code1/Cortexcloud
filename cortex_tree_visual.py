# cortex_tree_visual.py

import os
import yaml
import networkx as nx
import matplotlib.pyplot as plt

FORKS_DIR = "cortex_brain/forks/"

def load_fork_meta(fork):
    path = os.path.join(FORKS_DIR, fork, "fork_meta.yaml")
    if not os.path.exists(path):
        return None
    with open(path, "r") as f:
        return yaml.safe_load(f)

def build_tree():
    G = nx.DiGraph()
    forks = sorted(os.listdir(FORKS_DIR))

    for fork in forks:
        meta = load_fork_meta(fork)
        if not meta:
            continue
        parent = meta.get("parent", "CORTEX")
        G.add_node(fork)
        G.add_edge(parent, fork)

    return G

def draw_tree(G):
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(10, 6))
    nx.draw(G, pos, with_labels=True, node_size=2500, node_color='lightblue', font_size=8, font_weight='bold', arrows=True)
    plt.title("🧠 CORTEX Fork Lineage Tree")
    plt.savefig("cortex_tree.png")
    plt.show()

if __name__ == "__main__":
    print("🌳 Building lineage tree...")
    tree = build_tree()
    draw_tree(tree)

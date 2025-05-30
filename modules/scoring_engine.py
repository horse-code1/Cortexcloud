# modules/scoring_engine.py

def score_fork(fork, brain):
    config = brain['scoring_config.yaml'].get('weights', {
        "doctrine_alignment": 0.4,
        "soul_harmony": 0.3,
        "entropy_delta": 0.2,
        "ethics_compliance": 0.1
    })

    mutation = fork.get('mutation', {})
    before = mutation.get('entropy_before', 0.1)
    after = mutation.get('entropy_after', 0.1)
    delta = abs(after - before)

    # Simulate component scores (stub logic)
    scores = {
        "doctrine_alignment": 0.9,
        "soul_harmony": 0.8,
        "entropy_delta": min(delta, 1.0),
        "ethics_compliance": 1.0
    }

    # Weighted score
    weighted_score = sum(scores[k] * config.get(k, 0) for k in scores)
    return round(weighted_score, 3)

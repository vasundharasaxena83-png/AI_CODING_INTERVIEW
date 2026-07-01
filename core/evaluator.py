def evaluate(structure, complexity, algo_type):
    score = 20  # Base score

    if structure.get("functions", 0) > 0:
        score += 20

    if structure.get("loops", 0) > 0:
        score += 20

    if algo_type in [
        "array",
        "string",
        "graph",
        "tree",
        "dp",
        "iteration",
        "recursion/functional",
    ]:
        score += 20

    if complexity == "O(n)":
        score += 20

    return min(score, 100)
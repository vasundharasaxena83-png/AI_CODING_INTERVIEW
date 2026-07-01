def estimate_complexity(features):

    loops = features.get("loops", 0)
    recursion = features.get("recursion", False)

    # 🟢 TRIVIAL CASE
    if loops == 0 and not recursion:
        return "O(1)"

    if recursion and loops == 0:
        return "O(n)"

    if loops == 1:
        return "O(n)"

    if loops > 1:
        return "O(n^2)"

    return "O(1)"
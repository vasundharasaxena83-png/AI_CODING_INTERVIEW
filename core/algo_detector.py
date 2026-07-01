import ast


def detect_algorithm_type(code):
    """
    Detects the most likely DSA pattern from Python code.
    """

    code = code.lower()

    try:
        tree = ast.parse(code)
    except SyntaxError:
        return "Unknown"

    # -------------------------
    # Recursion Detection
    # -------------------------
    for node in ast.walk(tree):

        if isinstance(node, ast.FunctionDef):

            func_name = node.name

            for child in ast.walk(node):

                if isinstance(child, ast.Call):

                    if isinstance(child.func, ast.Name):

                        if child.func.id == func_name:
                            return "Recursion"

    # -------------------------
    # Graph
    # -------------------------
    graph_keywords = [
        "bfs",
        "dfs",
        "visited",
        "queue",
        "stack",
        "adj",
        "graph"
    ]

    if any(k in code for k in graph_keywords):
        return "Graph"

    # -------------------------
    # Tree
    # -------------------------
    tree_keywords = [
        "left",
        "right",
        "node",
        "root"
    ]

    if any(k in code for k in tree_keywords):
        return "Tree"

    # -------------------------
    # Dynamic Programming
    # -------------------------
    dp_keywords = [
        "dp",
        "memo",
        "cache"
    ]

    if any(k in code for k in dp_keywords):
        return "Dynamic Programming"

    # -------------------------
    # Binary Search
    # -------------------------
    binary_keywords = [
        "mid",
        "low",
        "high",
        "left",
        "right"
    ]

    if all(k in code for k in ["low", "high", "mid"]):
        return "Binary Search"

    # -------------------------
    # Sliding Window
    # -------------------------
    if "window" in code:
        return "Sliding Window"

    # -------------------------
    # Two Pointer
    # -------------------------
    if "left" in code and "right" in code:
        return "Two Pointer"

    # -------------------------
    # String
    # -------------------------
    string_keywords = [
        "[::-1]",
        "split",
        "join",
        "replace",
        "lower",
        "upper",
        "strip"
    ]

    if any(k in code for k in string_keywords):
        return "String"

    # -------------------------
    # Array
    # -------------------------
    array_keywords = [
        "append",
        "sort",
        "max",
        "min",
        "enumerate"
    ]

    if any(k in code for k in array_keywords):
        return "Array"

    # -------------------------
    # Loop Based
    # -------------------------
    if "for" in code or "while" in code:
        return "Iteration"

    # -------------------------
    # Function
    # -------------------------
    if "def " in code:
        return "Function"

    return "Trivial"
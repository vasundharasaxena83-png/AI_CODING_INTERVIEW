import ast

def analyze_code_structure(code):
    tree = ast.parse(code)

    loops = 0
    functions = 0
    recursion = False
    if_statements = 0

    for node in ast.walk(tree):

        if isinstance(node, ast.For) or isinstance(node, ast.While):
            loops += 1

        if isinstance(node, ast.FunctionDef):
            functions += 1

        if isinstance(node, ast.If):
            if_statements += 1

        # REAL recursion detection
        if isinstance(node, ast.FunctionDef):
            for child in ast.walk(node):
                if isinstance(child, ast.Call):
                    if getattr(child.func, 'id', None) == node.name:
                        recursion = True

    return {
        "loops": loops,
        "functions": functions,
        "recursion": recursion,
        "if_statements": if_statements
    }
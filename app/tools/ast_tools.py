import ast

def analyze_python_ast(code: str):
    tree = ast.parse(code)
    issues = []

    for node in ast.walk(tree):

        # Bare except
        if isinstance(node, ast.ExceptHandler) and node.type is None:
            issues.append({
                "line": node.lineno,
                "message": "Bare except detected",
                "severity": "high",
                "category": "reliability",
            })

        # print() in production
        if isinstance(node, ast.Call) and getattr(node.func, "id", None) == "print":
            issues.append({
                "line": node.lineno,
                "message": "print() used in code",
                "severity": "low",
                "category": "style",
            })

    return issues

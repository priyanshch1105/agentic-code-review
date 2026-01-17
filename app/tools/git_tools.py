import os

EXCLUDE = {".git", "__pycache__", "node_modules", "venv", ".venv", "tests"}

def build_repo_tree(root: str) -> str:
    lines = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE]
        for f in filenames:
            if f.endswith((".py", ".js", ".ts", ".java", ".go")):
                lines.append(os.path.join(dirpath, f))
    return "\n".join(lines)

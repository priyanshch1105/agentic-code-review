import json
import re
from pathlib import Path
from app.schemas.refactor import RefactorOutput
from app.models.ollama import get_llm

BASE_DIR = Path(__file__).resolve().parents[2]
PROMPT_PATH = BASE_DIR / "app" / "prompts" / "refactor.txt"

class RefactorAgent:
    def __init__(self, llm=None):
        self.llm = llm
        self.prompt = PROMPT_PATH.read_text()

    def run(
        self,
        file_path: str,
        code: str,
        issues: list[dict],
    ) -> RefactorOutput:
        llm = self.llm or get_llm()

        payload = {
            "file": file_path,
            "issues": issues,
            "code": code,
        }

        response = llm.invoke(
            self.prompt + "\n\nInput:\n" + json.dumps(payload, indent=2)
        )

        match = re.search(r"\{[\s\S]*\}", response.content)
        if not match:
            raise ValueError("RefactorAgent did not return JSON")

        data = json.loads(match.group())

        # HARD SAFETY CHECK
        if not data["diff"].startswith(("diff --git", "---", "+++")):
            raise ValueError("Output is not a unified diff")

        return RefactorOutput(**data)

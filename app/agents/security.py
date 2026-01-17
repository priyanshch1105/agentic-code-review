import json
import re
from pathlib import Path
from app.schemas.security import SecurityOutput
from app.models.ollama import get_llm

BASE_DIR = Path(__file__).resolve().parents[2]
PROMPT_PATH = BASE_DIR / "app" / "prompts" / "security.txt"

class SecurityAgent:
    def __init__(self, llm=None):
        self.llm = llm
        self.prompt = PROMPT_PATH.read_text()

    def run(self, raw_issues: list[dict]) -> SecurityOutput:
        if not raw_issues:
            return SecurityOutput(issues=[])

        llm = self.llm or get_llm()

        response = llm.invoke(
            self.prompt + "\n\nInput:\n" + json.dumps(raw_issues, indent=2)
        )

        match = re.search(r"\{[\s\S]*\}", response.content)
        if not match:
            raise ValueError("SecurityAgent did not return JSON")

        return SecurityOutput(**json.loads(match.group()))

import json
import re
from pathlib import Path
from app.schemas.analyzer import AnalyzerOutput
from app.models.ollama import get_llm

BASE_DIR = Path(__file__).resolve().parents[2]
PROMPT_PATH = BASE_DIR / "app" / "prompts" / "analyzer.txt"

class CodeAnalyzerAgent:
    def __init__(self, llm=None):
        self.llm = llm
        self.prompt = PROMPT_PATH.read_text()

    def run(self, file_path: str, ast_issues: list) -> AnalyzerOutput:
        if not ast_issues:
            return AnalyzerOutput(issues=[])

        llm = self.llm or get_llm()

        payload = {
            "file": file_path,
            "findings": ast_issues,
        }

        response = llm.invoke(
            self.prompt + "\n\nInput:\n" + json.dumps(payload, indent=2)
        )

        match = re.search(r"\{[\s\S]*\}", response.content)
        if not match:
            raise ValueError("AnalyzerAgent did not return JSON")

        return AnalyzerOutput(**json.loads(match.group()))

import json
import re
from pathlib import Path
from app.schemas.planner import PlannerOutput
from app.models.ollama import get_llm

BASE_DIR = Path(__file__).resolve().parents[2]
PROMPT_PATH = BASE_DIR / "app" / "prompts" / "planner.txt"

class PlannerAgent:
    def __init__(self, llm=None):
        self.llm = llm
        self.prompt = PROMPT_PATH.read_text()

    def run(self, repo_tree: str) -> PlannerOutput:
        llm = self.llm or get_llm()

        response = llm.invoke(
            self.prompt + "\n\nRepository Tree:\n" + repo_tree
        )

        match = re.search(r"\{[\s\S]*\}", response.content)
        if not match:
            raise ValueError("PlannerAgent did not return JSON")

        data = json.loads(match.group())
        return PlannerOutput(**data)

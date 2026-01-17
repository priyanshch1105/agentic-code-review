from pydantic import BaseModel

class RefactorOutput(BaseModel):
    diff: str          # unified diff only
    rationale: str     # short explanation (no markdown)

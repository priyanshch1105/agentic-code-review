from pydantic import BaseModel
from typing import List

class SecurityIssue(BaseModel):
    tool: str
    file: str
    line: int | None
    severity: str   # low | medium | high | critical
    message: str

class SecurityOutput(BaseModel):
    issues: List[SecurityIssue]

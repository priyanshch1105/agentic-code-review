from pydantic import BaseModel
from typing import List

class CodeIssue(BaseModel):
    file: str
    line: int | None
    severity: str  # low | medium | high
    message: str
    category: str  # bug | performance | style | reliability

class AnalyzerOutput(BaseModel):
    issues: List[CodeIssue]

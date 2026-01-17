from pydantic import BaseModel
from typing import List

class FileTask(BaseModel):
    path: str
    language: str
    priority: str  # high | medium | low

class PlannerOutput(BaseModel):
    files: List[FileTask]

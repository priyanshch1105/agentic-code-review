from pydantic import BaseModel

class VerifierOutput(BaseModel):
    status: str        # accepted | rejected
    test_output: str
    reason: str | None

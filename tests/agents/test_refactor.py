from app.agents.refactor import RefactorAgent
from app.schemas.refactor import RefactorOutput

class FakeLLM:
    def invoke(self, _):
        class R:
            content = """
            {
              "diff": "diff --git a/app/main.py b/app/main.py\\n--- a/app/main.py\\n+++ b/app/main.py\\n@@ -1,3 +1,3 @@\\n-print('hi')\\n+print('hi')",
              "rationale": "No-op refactor to demonstrate diff format"
            }
            """
        return R()

def test_refactor_agent_runs():
    agent = RefactorAgent(llm=FakeLLM())

    result = agent.run(
        file_path="app/main.py",
        code="print('hi')",
        issues=[],
    )

    assert isinstance(result, RefactorOutput)
    assert result.diff.startswith("diff --git")

from app.agents.security import SecurityAgent
from app.schemas.security import SecurityOutput

class FakeLLM:
    def invoke(self, _):
        class R:
            content = """
            {
              "issues": [
                {
                  "tool": "bandit",
                  "file": "app/main.py",
                  "line": 12,
                  "severity": "high",
                  "message": "Use of eval detected"
                }
              ]
            }
            """
        return R()

def test_security_agent_runs():
    raw = [{
        "tool": "bandit",
        "file": "app/main.py",
        "line": 12,
        "severity": "high",
        "message": "Use of eval detected"
    }]

    agent = SecurityAgent(llm=FakeLLM())
    result = agent.run(raw)

    assert isinstance(result, SecurityOutput)
    assert result.issues[0].severity == "high"

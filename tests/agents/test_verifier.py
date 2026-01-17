from app.agents.verifier import VerifierAgent

def test_verifier_accepts(monkeypatch):
    monkeypatch.setattr(
        "app.agents.verifier.apply_patch",
        lambda *_: None,
    )
    monkeypatch.setattr(
        "app.agents.verifier.run_tests",
        lambda *_: "PASSED",
    )
    monkeypatch.setattr(
        "app.agents.verifier.reset_repo",
        lambda *_: None,
    )

    agent = VerifierAgent()
    result = agent.run("/fake/repo", "diff --git a b")

    assert result.status == "accepted"


def test_verifier_rejects(monkeypatch):
    monkeypatch.setattr(
        "app.agents.verifier.apply_patch",
        lambda *_: None,
    )
    monkeypatch.setattr(
        "app.agents.verifier.run_tests",
        lambda *_: "FAILED",
    )
    monkeypatch.setattr(
        "app.agents.verifier.reset_repo",
        lambda *_: None,
    )

    agent = VerifierAgent()
    result = agent.run("/fake/repo", "diff --git a b")

    assert result.status == "rejected"

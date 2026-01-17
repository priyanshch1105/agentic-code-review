from app.schemas.verifier import VerifierOutput
from app.tools.patch_tool import apply_patch, reset_repo
from app.tools.test_runner import run_tests


class VerifierAgent:
    def run(self, repo_path: str, diff: str) -> VerifierOutput:
        try:
            apply_patch(repo_path, diff)
            test_output = run_tests(repo_path)

            if "FAILED" in test_output or "ERROR" in test_output:
                reset_repo(repo_path)
                return VerifierOutput(
                    status="rejected",
                    test_output=test_output,
                    reason="Tests failed after refactor",
                )

            return VerifierOutput(
                status="accepted",
                test_output=test_output,
                reason=None,
            )

        except Exception as e:
            reset_repo(repo_path)
            return VerifierOutput(
                status="rejected",
                test_output="",
                reason=str(e),
            )

from app.services.repo_service import clone_repo, cleanup_repo
from app.tools.git_tools import build_repo_tree
from app.tools.ast_tools import analyze_python_ast
from app.tools.bandit_tool import run_bandit
from app.tools.semgrep_tool import run_semgrep

from app.agents.planner import PlannerAgent
from app.agents.analyzer import CodeAnalyzerAgent
from app.agents.security import SecurityAgent
from app.agents.refactor import RefactorAgent
from app.agents.verifier import VerifierAgent


class ReviewService:
    def run(self, repo_url: str) -> dict:
        repo_path = clone_repo(repo_url)

        try:
            # 1. Planner
            tree = build_repo_tree(repo_path)
            planner = PlannerAgent()
            plan = planner.run(tree)

            analyzer = CodeAnalyzerAgent()
            security = SecurityAgent()
            refactor = RefactorAgent()
            verifier = VerifierAgent()

            results = []

            for task in plan.files:
                if task.language != "python":
                    continue

                file_path = f"{repo_path}/{task.path}"

                try:
                    code = open(file_path, encoding="utf-8").read()
                except FileNotFoundError:
                    continue

                # 2. Static Analysis
                ast_issues = analyze_python_ast(code)
                analysis = analyzer.run(task.path, ast_issues)

                # 3. Security Scan
                bandit_issues = run_bandit(file_path)
                semgrep_issues = run_semgrep(file_path)
                security_result = security.run(
                    bandit_issues + semgrep_issues
                )

                issues = [
                    *[i.dict() for i in analysis.issues],
                    *[i.dict() for i in security_result.issues],
                ]

                if not issues:
                    continue

                # 4. Refactor
                refactor_result = refactor.run(
                    task.path,
                    code,
                    issues,
                )

                # 5. Verify
                verify = verifier.run(
                    repo_path,
                    refactor_result.diff,
                )

                results.append({
                    "file": task.path,
                    "status": verify.status,
                    "rationale": refactor_result.rationale,
                })

                if verify.status == "rejected":
                    break

            return {
                "status": "completed",
                "results": results,
            }

        finally:
            cleanup_repo(repo_path)

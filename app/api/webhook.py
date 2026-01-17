from fastapi import APIRouter, Request
from app.services.review_service import ReviewService

router = APIRouter(prefix="/webhook")

@router.post("/github")
async def github_webhook(req: Request):
    payload = await req.json()

    if payload.get("action") != "opened":
        return {"ignored": True}

    repo = payload["repository"]["full_name"]
    pr = payload["pull_request"]["number"]
    clone_url = payload["repository"]["clone_url"]

    service = ReviewService()
    result = service.run(clone_url)

    # TODO: post PR comment using GitHub token
    return result

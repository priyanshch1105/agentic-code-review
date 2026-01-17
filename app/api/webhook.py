from fastapi import APIRouter
from pydantic import BaseModel
from app.services.review_service import ReviewService

router = APIRouter()

class ReviewRequest(BaseModel):
    repo_url: str

@router.post("/review")
def review_repo(payload: ReviewRequest):
    service = ReviewService()
    return service.run(payload.repo_url)

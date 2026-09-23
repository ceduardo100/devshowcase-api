from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.repositories import feedback_repository
from app.schemas.feedback import FeedbackCreate, FeedbackResponse


router = APIRouter(
    prefix="/api/feedbacks",
    tags=["Feedbacks"]
)


@router.post("/", response_model=FeedbackResponse)
def create_feedback(
    feedback_data: FeedbackCreate,
    db: Session = Depends(get_db)
):
    feedback = feedback_repository.create_feedback(
        db,
        feedback_data
    )
    return feedback


@router.get("/", response_model=list[FeedbackResponse])
def get_all_feedbacks(
    db: Session = Depends(get_db)
):
    return feedback_repository.get_all_feedbacks(db)
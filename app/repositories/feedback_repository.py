from sqlalchemy.orm import Session

from app.models.feedback import Feedback
from app.schemas.feedback import FeedbackCreate


def create_feedback(db: Session, feedback_data: FeedbackCreate):
    feedback = Feedback(
        rating=feedback_data.rating,
        message=feedback_data.message,
        project_id=feedback_data.project_id,
    )

    db.add(feedback)
    db.commit()
    db.refresh(feedback)

    return feedback


def get_all_feedbacks(db: Session):
    return db.query(Feedback).all()
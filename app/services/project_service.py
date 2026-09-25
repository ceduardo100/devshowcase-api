from sqlalchemy.orm import Session

from app.models.feedback import Feedback
from app.models.project import Project


def add_feedback(
    db: Session,
    project_id: int,
    rating: int,
    message: str,
):
    project = db.query(Project).filter(Project.id == project_id).first()

    if project is None:
        return None

    feedback = Feedback(
        rating=rating,
        message=message,
        project_id=project_id,
    )

    db.add(feedback)
    db.flush()

    feedbacks = (
        db.query(Feedback)
        .filter(Feedback.project_id == project_id)
        .all()
    )

    total_rating = sum(feedback.rating for feedback in feedbacks)
    project.average_rating = total_rating / len(feedbacks)

    db.commit()
    db.refresh(feedback)
    db.refresh(project)

    return feedback


def add_upvote(
    db: Session,
    project_id: int,
):
    project = db.query(Project).filter(Project.id == project_id).first()

    if project is None:
        return None

    project.upvotes += 1

    db.commit()
    db.refresh(project)

    return project
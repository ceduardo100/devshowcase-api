from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.repositories import project_repository
from app.schemas.project import ProjectCreate, ProjectResponse
from app.schemas.feedback import FeedbackCreate, FeedbackResponse
from app.services.project_service import add_feedback, add_upvote


router = APIRouter(
    prefix="/api/projects",
    tags=["Projects"],
)


@router.post("/", response_model=ProjectResponse)
def create_project(
    project_data: ProjectCreate,
    db: Session = Depends(get_db),
):
    project = project_repository.create_project(
        db,
        project_data,
    )

    return project


@router.get("/", response_model=list[ProjectResponse])
def get_all_projects(
    technology_id: int | None = None,
    page: int = Query(1),
    limit: int = Query(10),
    db: Session = Depends(get_db),
):
    if page < 1 or limit < 1:
        raise HTTPException(
            status_code=400,
            detail="page e limit devem ser maiores que zero",
        )

    return project_repository.get_all_projects(
        db=db,
        technology_id=technology_id,
        page=page,
        limit=limit,
    )


@router.post(
    "/{project_id}/feedbacks",
    response_model=FeedbackResponse,
)
def create_project_feedback(
    project_id: int,
    feedback_data: FeedbackCreate,
    db: Session = Depends(get_db),
):
    feedback = add_feedback(
        db=db,
        project_id=project_id,
        rating=feedback_data.rating,
        message=feedback_data.message,
    )

    if feedback is None:
        raise HTTPException(
            status_code=404,
            detail="Projeto não encontrado",
        )

    return feedback


@router.put(
    "/{project_id}/upvote",
    response_model=ProjectResponse,
)
def upvote_project(
    project_id: int,
    db: Session = Depends(get_db),
):
    project = add_upvote(
        db=db,
        project_id=project_id,
    )

    if project is None:
        raise HTTPException(
            status_code=404,
            detail="Projeto não encontrado",
        )

    return project
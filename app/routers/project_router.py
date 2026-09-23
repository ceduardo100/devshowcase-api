from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.repositories import project_repository
from app.schemas.project import ProjectCreate, ProjectResponse


router = APIRouter(
    prefix="/api/projects",
    tags=["Projects"]
)


@router.post("/", response_model=ProjectResponse)
def create_project(
    project_data: ProjectCreate,
    db: Session = Depends(get_db)
):
    project = project_repository.create_project(db, project_data)

    return project


@router.get("/", response_model=list[ProjectResponse])
def get_all_projects(
    db: Session = Depends(get_db)
):
    return project_repository.get_all_projects(db)
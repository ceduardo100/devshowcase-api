from sqlalchemy.orm import Session

from app.models.project import Project
from app.schemas.project import ProjectCreate


def create_project(db: Session, project_data: ProjectCreate):
    project = Project(
        title=project_data.title,
        description=project_data.description,
        github_url=str(project_data.github_url) if project_data.github_url else None,
        profile_id=project_data.profile_id,
    )

    db.add(project)
    db.commit()
    db.refresh(project)

    return project


def get_all_projects(db: Session):
    return db.query(Project).all()
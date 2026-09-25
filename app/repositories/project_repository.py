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


def get_all_projects(
    db: Session,
    technology_id: int | None = None,
    page: int = 1,
    limit: int = 10,
):
    query = db.query(Project)

    if technology_id is not None:
        query = query.filter(
            Project.technologies.any(id=technology_id)
        )

    offset = (page - 1) * limit

    return (
        query
        .offset(offset)
        .limit(limit)
        .all()
    )
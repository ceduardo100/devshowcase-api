from sqlalchemy.orm import Session

from app.models.technology import Technology
from app.schemas.technology import TechnologyCreate


def create_technology(db: Session, technology: TechnologyCreate):
    db_technology = Technology(
        name=technology.name
    )

    db.add(db_technology)
    db.commit()
    db.refresh(db_technology)

    return db_technology


def get_all_technologies(db: Session):
    return db.query(Technology).all()

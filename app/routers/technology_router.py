from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.repositories.technology_repository import (
    create_technology,
    get_all_technologies,
)
from app.schemas.technology import TechnologyCreate, TechnologyResponse


router = APIRouter(
    prefix="/api/technologies",
    tags=["Technologies"]
)


@router.post("/", response_model=TechnologyResponse)
def create(technology: TechnologyCreate, db: Session = Depends(get_db)):
    return create_technology(db, technology)


@router.get("/", response_model=list[TechnologyResponse])
def get_all(db: Session = Depends(get_db)):
    return get_all_technologies(db)
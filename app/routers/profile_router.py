from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.repositories import profile_repository
from app.schemas.profile import ProfileCreate, ProfileResponse


router = APIRouter(
    prefix="/api/profiles",
    tags=["Profiles"]
)


@router.post("/", response_model=ProfileResponse)
def create_profile(
    profile_data: ProfileCreate,
    db: Session = Depends(get_db)
):
    profile = profile_repository.create_profile(db, profile_data)

    return profile


@router.get("/{profile_id}", response_model=ProfileResponse)
def get_profile(
    profile_id: int,
    db: Session = Depends(get_db)
):
    profile = profile_repository.get_profile_by_id(db, profile_id)

    if profile is None:
        raise HTTPException(
            status_code=404,
            detail="Perfil não encontrado"
        )

    return profile

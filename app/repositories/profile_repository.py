from sqlalchemy.orm import Session

from app.models.profile import Profile
from app.schemas.profile import ProfileCreate


def create_profile(db: Session, profile_data: ProfileCreate):
    profile = Profile(
        name=profile_data.name,
        email=profile_data.email,
        bio=profile_data.bio,
        github_url=str(profile_data.github_url) if profile_data.github_url else None,
        linkedin_url=str(profile_data.linkedin_url) if profile_data.linkedin_url else None,
    )

    db.add(profile)
    db.commit()
    db.refresh(profile)

    return profile


def get_profile_by_id(db: Session, profile_id: int):
    return db.query(Profile).filter(Profile.id == profile_id).first()

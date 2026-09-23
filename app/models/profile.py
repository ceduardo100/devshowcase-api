from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship

from app.database import Base
from app.models.profile_technology import profile_technologies


class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(150), nullable=False, unique=True)
    bio = Column(Text, nullable=True)
    github_url = Column(String(255), nullable=True)
    linkedin_url = Column(String(255), nullable=True)

    technologies = relationship(
        "Technology",
        secondary=profile_technologies,
        back_populates="profiles",
    )

    projects = relationship(
        "Project",
        back_populates="profile",
        cascade="all, delete-orphan",
    )

    feedbacks = relationship(
        "Feedback",
        back_populates="profile",
        cascade="all, delete-orphan",
    )
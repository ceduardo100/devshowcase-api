from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base
from app.models.project_technology import project_technologies


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(150), nullable=False)
    description = Column(Text, nullable=True)
    github_url = Column(String(255), nullable=True)

    profile_id = Column(
        Integer,
        ForeignKey("profiles.id", ondelete="CASCADE"),
        nullable=False,
    )

    profile = relationship(
        "Profile",
        back_populates="projects",
    )

    technologies = relationship(
        "Technology",
        secondary=project_technologies,
        back_populates="projects",
    )

    feedbacks = relationship(
        "Feedback",
        back_populates="project",
        cascade="all, delete-orphan",
    )
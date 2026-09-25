from sqlalchemy import Column, Integer, String, Text, ForeignKey, Float
from sqlalchemy.orm import relationship

from app.database import Base
from app.models.project_technology import project_technologies


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(150), nullable=False)
    description = Column(Text, nullable=True)
    github_url = Column(String(255), nullable=True)

    upvotes = Column(Integer, nullable=False, default=0)
    average_rating = Column(Float, nullable=False, default=0.0)

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
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base
from app.models.profile_technology import profile_technologies


class Technology(Base):
    __tablename__ = "technologies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)

    profiles = relationship(
        "Profile",
        secondary=profile_technologies,
        back_populates="technologies",
    )
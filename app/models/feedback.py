from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class Feedback(Base):
    __tablename__ = "feedbacks"

    id = Column(Integer, primary_key=True, index=True)
    message = Column(Text, nullable=False)

    profile_id = Column(
        Integer,
        ForeignKey("profiles.id", ondelete="CASCADE"),
        nullable=False,
    )

    profile = relationship(
        "Profile",
        back_populates="feedbacks",
    )
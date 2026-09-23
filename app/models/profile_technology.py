from sqlalchemy import Table, Column, Integer, ForeignKey

from app.database import Base


profile_technologies = Table(
    "profile_technologies",
    Base.metadata,
    Column(
        "profile_id",
        Integer,
        ForeignKey("profiles.id", ondelete="CASCADE"),
        primary_key=True,
    ),
    Column(
        "technology_id",
        Integer,
        ForeignKey("technologies.id", ondelete="CASCADE"),
        primary_key=True,
    ),
)
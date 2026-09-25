from pydantic import BaseModel, Field, HttpUrl


class ProjectCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=150)
    description: str | None = None
    github_url: HttpUrl | None = None
    profile_id: int


class ProjectResponse(BaseModel):
    id: int
    title: str
    description: str | None = None
    github_url: HttpUrl | None = None
    profile_id: int
    upvotes: int
    average_rating: float

    class Config:
        from_attributes = True
from pydantic import BaseModel, EmailStr, HttpUrl, Field


class ProfileCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    bio: str | None = None
    github_url: HttpUrl | None = None
    linkedin_url: HttpUrl | None = None


class ProfileResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    bio: str | None = None
    github_url: HttpUrl | None = None
    linkedin_url: HttpUrl | None = None

    class Config:
        from_attributes = True
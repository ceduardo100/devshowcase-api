from pydantic import BaseModel, Field


class FeedbackCreate(BaseModel):
    message: str = Field(..., min_length=1)
    profile_id: int


class FeedbackResponse(BaseModel):
    id: int
    message: str
    profile_id: int

    class Config:
        from_attributes = True
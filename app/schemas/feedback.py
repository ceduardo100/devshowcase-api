from pydantic import BaseModel, Field


class FeedbackCreate(BaseModel):
    rating: int = Field(..., ge=1, le=5)
    message: str = Field(..., min_length=1)


class FeedbackResponse(BaseModel):
    id: int
    rating: int
    message: str
    project_id: int

    class Config:
        from_attributes = True
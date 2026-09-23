from pydantic import BaseModel, Field


class TechnologyCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)


class TechnologyResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True
        
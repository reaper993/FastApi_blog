from typing import Optional
from pydantic import BaseModel, model_validator
from datetime import datetime

class CreateBlog(BaseModel):
    title: str
    slug: str
    content: Optional[str] = None

    @model_validator(mode="before")
    def generate_slug(cls, values):
        if values.get("title") and not values.get("slug"):
            values["slug"] = values.get("title").replace(" ", "-").lower()
        return values

class UpdateBlog(CreateBlog):
    pass

class DeleteBlog(BaseModel):
    pass

class ShowBlog(BaseModel):
    title: str
    content: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True
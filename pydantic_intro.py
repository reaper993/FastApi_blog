from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum
from datetime import datetime

class Language(str, Enum):
    PY = "python"
    JAVA = "java"
    GO = "golang"

class Comment(BaseModel):
    text : Optional[str] = None

class Blog(BaseModel):
    title: str = Field(min_length=5, max_length=20)
    is_active: bool
    description: Optional[str] = None
    language: Language = Language.PY
    created_at: datetime = Field(default_factory=datetime.now)
    comments: Optional[List[Comment]] = None

first_blog = Blog(title="Blog Title", is_active=True, comments=[{"text": "This is a comment"}])
print(first_blog)

import time
time.sleep(5)
second_blog = Blog(title="Blog Title", is_active=True)
print(second_blog)
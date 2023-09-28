from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.session import get_db
from schemas.blog import CreateBlog, ShowBlog
from db.repository.blog import create_new_blog


router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ShowBlog)
def create_blog(blog: CreateBlog, db: Session = Depends(get_db)):
    blog = create_new_blog(db=db, blog=blog, author_id=1)
    return blog
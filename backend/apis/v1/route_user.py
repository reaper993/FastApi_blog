from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from schemas.user import UserCreate
from db.session import get_db
from db.repository.user import create_new_user

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user = create_new_user(db=db, user=user)
    return user
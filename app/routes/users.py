from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from .. import schemas, crud
from ..database import get_db

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=schemas.UserResponse)
def create(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@router.get("/", response_model=list[schemas.UserResponse])
def read_all(db: Session = Depends(get_db)):
    return crud.get_users(db)

@router.get("/{id}", response_model=schemas.UserResponse)
def read_one(id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{id}")
def update(id: int, updated: schemas.UserUpdate, db: Session = Depends(get_db)):
    user = crud.update_user(db, id, updated)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User successfully updated"}

@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    user = crud.delete_user(db, id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}


from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from .. import schemas, crud
from ..database import get_db

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/", response_model=schemas.TaskResponse)
def create(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task)

@router.get("/", response_model=list[schemas.TaskResponse])
def read_all(db: Session = Depends(get_db)):
    return crud.get_tasks(db)

@router.get("/{id}", response_model=schemas.TaskResponse)
def read_one(id: int, db: Session = Depends(get_db)):
    task = crud.get_task(db, id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/{id}")
def update(id: int, updated: schemas.TaskCreate, db: Session = Depends(get_db)):
    task = crud.update_task(db, id, updated)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task successfully updated"}

@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    task = crud.delete_task(db, id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted"}

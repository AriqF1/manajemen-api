from sqlalchemy.orm import Session
from . import models, schemas

def get_tasks(db: Session):
    return db.query(models.Task).all()

def get_task(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()

def create_task(db: Session, task: schemas.TaskCreate):
    db_task = models.Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def update_task(db: Session, task_id: int, updated: schemas.TaskCreate):
    task = get_task(db, task_id)
    if task:
        task.title = updated.title
        task.description = updated.description
        db.commit()
    return {"message": "Task updated successfully"} if task else {"message": "Task not found"}

def delete_task(db: Session, task_id: int):
    task = get_task(db, task_id)
    if task:
        db.delete(task)
        db.commit()
    return {"message": "Task deleted successfully"} if task else {"message": "Task not found"}

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
    return task

# operasi crud untuk user ---
def get_users(db: Session):
    return db.query(models.User).all()

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"message": "User created successfully"}

def update_user(db: Session, user_id: int, updated: schemas.UserUpdate):
    user = get_user(db, user_id)
    if user:
        user.username = updated.username
        user.email = updated.email
        user.full_name = updated.full_name
        user.password = updated.password
        db.commit()
    return user

def delete_user(db: Session, user_id: int):
    user = get_user(db, user_id)
    if user:
        db.delete(user)
        db.commit()
    return user
    return {"message": "Task deleted successfully"} if task else {"message": "Task not found"}


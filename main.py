from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,Session
from pydantic import BaseModel
from sqlalchemy.future import select

# Setup FastAPI
app = FastAPI()

# Setup SQLAlchemy database
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root@127.0.0.1:3306/api-management"

# Setup SQLAlchemy
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_size=5, max_overflow=10)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base untuk deklarasi model
Base = declarative_base()

# Model untuk tabel tasks
class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)

# Pydantic Schema untuk validasi data
class TaskCreate(BaseModel):
    title: str
    description: str

# Dependency untuk mendapatkan sesi database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint untuk membuat tugas baru
@app.post("/tasks/", response_model=TaskCreate)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    db_task = Task(title=task.title, description=task.description)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

# Endpoint untuk mendapatkan semua tugas
@app.get("/tasks/")
def get_tasks(db: Session = Depends(get_db)):
    tasks = db.query(Task).all()
    return tasks

# Endpoint untuk mendapatkan tugas berdasarkan ID
@app.get("/tasks/{id}")
def get_task(id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

# Membuat tabel di database
Base.metadata.create_all(bind=engine)

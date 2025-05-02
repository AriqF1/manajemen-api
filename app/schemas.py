from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    description: str

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    title: str
    description: str

    class Config:
        orm_mode = True

class TaskDelete(BaseModel):
    id: int

    class Config:
        orm_mode = True
        
class TaskResponse(TaskBase):
    id: int

    class Config:
        orm_mode = True

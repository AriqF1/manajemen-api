from pydantic import BaseModel

#class untuk login request
class LoginBase(BaseModel):
    username: str
    password: str

#class untuk crud task ---
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

#class untuk crud user ---
class UserBase(BaseModel):
    username: str
    email: str
    full_name: str
    password: str

    class Config:
        orm_mode = True 

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    username: str
    email: str
    full_name: str
    hashed_password: str

    class Config:
        orm_mode = True

class UserDelete(BaseModel):
    id: int

    class Config:
        orm_mode = True

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    full_name: str

    class Config:
        orm_mode = True 
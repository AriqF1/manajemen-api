from fastapi import FastAPI
from . import models
from .database import engine
from .routes import tasks
from .routes import users

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

# Register routes
app.include_router(tasks.router)
app.include_router(users.router)

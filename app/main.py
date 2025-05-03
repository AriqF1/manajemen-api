from fastapi import FastAPI
from . import models
from .database import engine
from .routes import tasks, users
from .auth import router as auth_router  # Pastikan kamu menggunakan alias yang benar

app = FastAPI()

# Pastikan model Base sudah terhubung dengan benar untuk membuat tabel
models.Base.metadata.create_all(bind=engine)

# Register routes
app.include_router(auth_router, tags=["Authentication"])  # Gunakan auth_router, bukan auth.router
app.include_router(tasks.router, tags=["Tasks"])  # Jika ada rute terkait tasks
app.include_router(users.router, tags=["Users"])  # Jika ada rute terkait users

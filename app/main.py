from fastapi import FastAPI, Depends
from typing import List
from .models import Task, TaskCreate
from .repositories import InMemoryTaskRepository, ITaskRepository, SqlTaskRepository
from .services import TaskService
from .database import SessionLocal
from sqlalchemy.orm import Session
from .database import engine
from . import models_orm

# สร้าง Table ใน Database
models_orm.Base.metadata.create_all(bind=engine)

# สร้างแอปพลิเคชันแค่ครั้งเดียวพอครับ
app = FastAPI()

# Singleton Repository สำหรับ In-Memory (ถ้าจะใช้)
task_repo = InMemoryTaskRepository()

# Dependency สำหรับเปิด-ปิด Database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Dependency สำหรับเรียกใช้ Service
def get_task_service(db: Session = Depends(get_db)):
    repo = SqlTaskRepository(db)
    return TaskService(repo)

# --- Routes ---

@app.get("/") 
def read_root():
    return {"message": "Hello World - Week 10 API is ready!"}

@app.get("/tasks", response_model=List[Task])
def read_tasks(service: TaskService = Depends(get_task_service)):
    return service.get_tasks()

@app.post("/tasks", response_model=Task)
def create_task(task: TaskCreate, service: TaskService = Depends(get_task_service)):
    return service.create_task(task)
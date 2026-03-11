from fastapi import FastAPI, HTTPException, Depends
from database_models import Tasks
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from database import Base
from models import TaskCreate

app = FastAPI()
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def greet():
    return "Welcome to Task Manager"

@app.get("/tasks")
def get_all_tasks(db : Session = Depends(get_db)):
    tasks = db.query(Tasks).all()
    return tasks

@app.get("/tasks/{id}")
def get_task_by_id(id : int , db : Session = Depends(get_db)):

    task = db.query(Tasks).filter(Tasks.task_id == id).first()
    if task:
        return task
    raise HTTPException(status_code = 404, detail = f"Task with id {id} does not exist")

    #Inefficient 
    # tasks = db.query(Tasks).all()
    # for task in tasks:
    #     if task.id == id:
    #         return task
    # raise HTTPException(status_code= 404, detail = f"Task with id {id} does not exist")

@app.post("/tasks")
def add_task(task: TaskCreate , db:Session = Depends(get_db)):

    new_task = Tasks(
        task_title = task.task_title,
        task_description = task.task_description,
        task_priority = task.task_priority,
        task_status = task.task_status
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@app.put("/tasks/{id}")
def update_task(id: int, task_update: TaskCreate ,db: Session = Depends(get_db)):

    task = db.query(Tasks).filter(Tasks.task_id == id).first()
    if task:
        task.task_title = task_update.task_title
        task.task_description = task_update.task_description
        task.task_priority = task_update.task_priority
        task.task_status = task_update.task_status
        db.commit()
        db.refresh(task)
        return task
    raise HTTPException(status_code = 404, detail = f"No task found with id: {id}")


@app.delete("/tasks/{id}")
def delete_task(id:int, db: Session = Depends(get_db)):
    task = db.query(Tasks).filter(Tasks.task_id == id).first()

    if task:
        print(task)
        db.delete(task)
        db.commit()
        return "Task deleted successfully"
    raise HTTPException(status_code = 404, detail = 'Task not found')
from fastapi import FastAPI , HTTPException
from models import Tasks


app = FastAPI()

@app.get("/")
def greet():
    return "Hello There"
tasks = [
    Tasks(task_id = 1, task_title = "Laundry", task_description = "Collect and put in washing machine", task_priority = "medium", task_status = "TO-DO"),
    Tasks(task_id = 2, task_title = "Study", task_description = "Machine Learning", task_priority = "high", task_status = "In-Progress"),
    Tasks(task_id = 3, task_title = "Gym", task_description = "Shoulder Workout", task_priority = "high", task_status = "TO-DO")
]

@app.get("/tasks")
def get_tasks():
    return tasks


@app.get("/tasks/{id:int}")
def get_task_by_id(id):
    for task in tasks:
        if task.task_id == id:
            return task, "Completed"
        else:
            raise HTTPException(status = 404, detail = "Task not found")

        
@app.post("/tasks")
def add_task(task : Tasks):
    tasks.append(task)
    return task


@app.put("/tasks/{task_id}")
def update_task(task_id : int, updated_task : Tasks):
    for task in tasks:
        if task.task_id == task_id:
            task.task_title = updated_task.task_title
            task.task_description = updated_task.task_description
            task.task_priority = updated_task.task_priority
            task.task_status = updated_task.task_status
            return task
    raise HTTPException(status_code = 404, detail = "Task not found")

@app.delete("/tasks/{task_id}")
def delete_task(task_id : int):
    for task in tasks:
        if task.task_id == task_id:
            tasks.remove(task)
            return f"Deleted task: {task}"
        
    raise HTTPException(status_code = 404, detail ="Task not found" )
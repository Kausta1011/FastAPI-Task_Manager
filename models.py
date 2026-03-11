from pydantic import BaseModel

class Tasks(BaseModel):
    

    task_id : int
    task_title : str
    task_description : str
    task_priority : str
    task_status : str

class TaskCreate(BaseModel):

    task_title : str
    task_description : str
    task_priority : str
    task_status : str
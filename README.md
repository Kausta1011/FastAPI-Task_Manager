# FastAPI Task Manager

A REST API for task management built with FastAPI, PostgreSQL, and SQLAlchemy.

## Tech Stack
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- python-dotenv

## How to Run Locally
1. Clone the repo
2. Create a virtual environment and activate it
3. Run `pip install -r requirements.txt`
4. Create a `.env` file in the root directory with the following:
   DATABASE_URL=postgresql://your_username:your_password@localhost:5432/task_manager
5. Run `uvicorn main:app --reload`
6. Open `http://localhost:8000/docs` to test the API

## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /tasks | Get all tasks |
| GET | /tasks/{id} | Get task by ID |
| POST | /tasks | Create a new task |
| PUT | /tasks/{id} | Update a task |
| DELETE | /tasks/{id} | Delete a task |
| GET | /tasks/status/{status} | Filter tasks by status |

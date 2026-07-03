from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Inicializa o aplicativo FastAPI
app = FastAPI(title="Task Management API", version="1.0.0")

# Definimos a estrutura dos dados usando o Pydantic. 
# Isso garante a validação dos dados (se alguém enviar um texto onde deveria ser número, a API bloqueia).
class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

# Banco de dados simulado em memória (uma lista Python vazia)
tasks_db: List[Task] = []

# Rota inicial de boas-vindas
@app.get("/")
def read_root():
    return {"message": "Welcome to the Task Management API! Go to /docs for testing."}

# 1. CRIAR UMA TAREFA (POST)
@app.post("/tasks", response_model=Task, status_code=201)
def create_task(task: Task):
    # Verifica se já existe uma tarefa com o mesmo ID
    for t in tasks_db:
        if t.id == task.id:
            raise HTTPException(status_code=400, detail="Task with this ID already exists.")
    tasks_db.append(task)
    return task

# 2. LISTAR TODAS AS TAREFAS (GET)
@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks_db

# 3. BUSCAR UMA TAREFA POR ID (GET)
@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    for task in tasks_db:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

# 4. ATUALIZAR UMA TAREFA (PUT)
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: Task):
    for index, task in enumerate(tasks_db):
        if task.id == task_id:
            tasks_db[index] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")

# 5. DELETAR UMA TAREFA (DELETE)
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for index, task in enumerate(tasks_db):
        if task.id == task_id:
            tasks_db.pop(index)
            return {"message": f"Task {task_id} successfully deleted"}
    raise HTTPException(status_code=404, detail="Task not found")
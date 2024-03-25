from fastapi import FastAPI, HTTPException, Depends
from typing import Optional, List, Dict
from pydantic import BaseModel
from uuid import UUID, uuid4

app = FastAPI()

# MODEL - usually put in a seperate file
class TodoItem(BaseModel):
    id: UUID
    title: str
    completed: bool = False

class UpdateTodo(BaseModel):
    id: Optional[UUID] = None
    title: Optional[str] = None
    completed: Optional[bool] = None

# STATIC/DUMMY DATA - try uncommenting it!
# todos = {UUID('8ffadce6-60d4-431f-afdb-3c53aac9d3c1'): TodoItem(id=UUID('8ffadce6-60d4-431f-afdb-3c53aac9d3c1'), title='cook', completed=False), 
#      UUID('33d1f1c4-1ce4-46f5-9b88-dc42b86a0083'): TodoItem(id=UUID('33d1f1c4-1ce4-46f5-9b88-dc42b86a0083'), title='clean', completed=True)}
    
# EMPTY STRING
todos = {}

# To do methods
# - fetch all todos
@app.get('/todos')
def get_all_todos():
    print(todos)
    return list(todos.values())

# - fetch by id
@app.get('/todos/{id}')
def get_todo(id: UUID):
    if id not in todos:
        return {"error":"title not found"}
    return todos[id]

# - post new todo
@app.post('/todos/new')
def post_todo(todo: TodoItem) -> dict:
    todos[todo.id] = todo
    return {
        "data": { "Todo added." }
    }

# - updates todo
@app.put("/todos/edit/{id}")
async def update_todo(id: UUID, todo: UpdateTodo):
    if id not in todos:
        return {'error':'ID not found'}

    if todo.title != None:
        todos[id].title = todo.title
    if todo.completed != None:
        todos[id].completed = todo.completed
    
    return todos[id]

# - removes an existing todo
@app.delete("/todos/delete/{id}")
async def delete_todo(id: UUID):
    if id not in todos:
        return {"error":"ID not found"}
    del todos[id]
    return {"msg":"todo has been deleted successfully"}
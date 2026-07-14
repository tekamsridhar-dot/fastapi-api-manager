from fastapi import FastAPI, Depends,HTTPException
from sqlalchemy.orm import Session
from .database import Base, engine,get_db
from .import models,schemas,crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task Manager API",
    description="This Simple and FastAPI CRUD Application allows users to manage daily task ",
    version="1.0.0"
)

@app.post("/tasks", response_model=schemas.TaskResponse, status_code=201)
def add_task(task: schemas.TaskCreate, db:Session = Depends(get_db)):
    return crud.create_task(db,task)

@app.get("/tasks", response_model=list[schemas.TaskResponse])
def get_all_tasks(db: Session=Depends(get_db)):
    return crud.get_tasks(db)

@app.put("/tasks/{task_id}",response_model=schemas.TaskResponse)
def update_task(
    task_id:int,
    task:schemas.Taskupdate,
    db:Session=Depends(get_db)
):
    updated = crud.update_task(db,task_id,task)
    if not updated:
        raise HTTPException(status_code=404,detail=" Task NOT Updated")
    
    return updated

@app.delete("/tasks/{task_id}")
def delete_task(task_id:int,db: Session = Depends(get_db)):
    deleted=crud.delete_task(db,task_id)
    if not deleted:
        raise HTTPException(status_code=404,details="Task not Deleted")
    
    return deleted





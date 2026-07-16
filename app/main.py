from fastapi import FastAPI, Depends,HTTPException,status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from .database import SessionLocal,engine
from .import models,schemas,crud
from app.auth import create_access_token
from .dependencies import get_current_user
 
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task Manager API",
    description="This Simple and FastAPI CRUD Application allows users to manage daily task ",
    version="2.0.1"
)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post(
        "/auth/signup",
        response_model=schemas.UserResponse,
        status_code=status.HTTP_201_CREATED
)
def signup(
    user:schemas.usercreate,
    db:Session=Depends(get_db)
):
    try:
        new_user=crud.create_user(db,user)
        if new_user is None:
            raise HTTPException(
                status_code=400,
                detail="user already exit"
        )
        return new_user
    except Exception as e:
        print("error:",repr(e))
        raise

@app.post("/auth/login",
          response_model=schemas.Token
)
def login(
    form_data:OAuth2PasswordRequestForm=Depends(),
    db:Session=Depends(get_db)
):
    user=crud.authenticate_user(
        db,
        form_data.username,
        form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="invalid email or password"
        )
    access_token=create_access_token(
        data={"sub":user.email}
    )
    return{
        "access_token":access_token,
        "token_type":"bearer"
    }
@app.get(
    "/auth/me",
    response_model=schemas.UserResponse
)
def get_me(current_user: models.user = Depends(get_current_user)):
    return current_user

@app.post(
    "/tasks",
    response_model=schemas.TaskResponse,
    status_code=status.HTTP_201_CREATED
)
def create_task(
    task:schemas.TaskCreate,
    db:Session=Depends(get_db),
    current_user:models.user=Depends(get_current_user)
):
    return crud.create_task(
        db,task,current_user.id)
    
@app.get("/task",
         response_model=list[schemas.TaskResponse])
def get_tasks(
    db:Session=Depends(get_db),
    current_user:models.user=Depends(get_current_user)
):
    return crud.get_tasks(
        db,current_user.id)
    
@app.get(
    "/tasks/{task_id}",
    response_model=schemas.TaskResponse
)
def get_task(
    task_id:int,
    db:Session=Depends(get_db),
    current_user:models.user=Depends(get_current_user)
):
    task=crud.get_task(db,task_id,current_user.id)
    if task is None:
        raise HTTPException(status_code=404,detail="task not found")
    return task
@app.put("/tasks/{task_id}",
         response_model=schemas.TaskResponse)
def update_task(task_id:int,
                task:schemas.Taskupdate,
                db:Session=Depends(get_db),
                current_user:models.user=Depends(get_current_user)):
    updated_task=crud.update_task(
        db,task_id,task,current_user.id)
    if updated_task is None:
        raise HTTPException(status_code=404,
                            detail="task not found")
    return updated_task
@app.delete("/tasks/{task_id}")
def delete_task(task_id:int,
                db:Session=Depends(get_db),
                current_user:models.user=Depends(get_current_user)):
    deleted_task=crud.delete_task(
        db,task_id,current_user.id)
    if deleted_task is None:
        raise HTTPException(
            status_code=404,
            detail="task not deleted"
        )
    return{"The task is deleted successfully"}
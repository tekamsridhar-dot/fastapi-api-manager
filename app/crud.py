from sqlalchemy.orm import Session
from .import models,schemas

def create_task(db:Session,task: schemas.TaskCreate):
    db_task = models.Task(
        title=task.title,
        description=task.description,
        status=task.status       
    )

    db.add(db_task)
    db.commit()
    db.refresh(db_task)

    return db_task

def get_tasks(db:Session,
              title:str=None,
              description:str=None,
              status:str=None,
              skip: int=0,
              limit:int=10):
            query=db.query(models.Task)
            if title:
                 query=query.filter(models.Task.title.ilike(f"%{title}%"))
            if status:
                 query=query.filter(models.task.status == status)
            tasks=query=query.offset(skip).limit(limit).all()
            return tasks

def update_task(db:Session,task_id:int,task: schemas.Taskupdate):
    db_task =db.query(models.Task).filter(
        models.Task.id == task_id
    ).first()

    if not db_task:
        return None
    
    db_task.title=task.title
    db_task.description=task.description
    db_task.status=task.status

    db.commit()
    db.refresh(db_task)

    return db_task

def delete_task(db:Session,task_id:int):
    db_task = db.query(models.task).filter(
        models.Task.id == task_id).first()

    if not db_task:
        return None
    db.delete(db_task)
    db.commit()

    return db_task

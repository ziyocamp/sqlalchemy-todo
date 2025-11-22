from sqlalchemy import (
    insert, select, update, delete
)
from database import engine
from tables import tasks_tabe


def create_task(name: str, description: str | None = None):
    stmt = insert(tasks_tabe).values(name=name, description=description)
    with engine.connect() as connection:
        connection.execute(stmt)
        connection.commit()

def get_tasks():
    stmt = select(tasks_tabe)
    with engine.connect() as connection:
        tasks = connection.execute(stmt)
        return list(tasks)

def get_one_task(pk: int):
    stmt = select(tasks_tabe).where(tasks_tabe.columns.id==pk)
    with engine.connect() as connection:
        existing_task = connection.execute(stmt).first()
        if existing_task is None:
            raise Exception('task not found.')
        return existing_task

def update_task(pk: int, name: str | None = None, description: str | None = None):
    if name is None and description is None:
        return
    elif name is not None and description is None:
        stmt = (
            update(tasks_tabe)
            .values(name=name)
            .where(tasks_tabe.columns.id==pk)
        )
    elif name is None and description is not None:
        stmt = (
            update(tasks_tabe)
            .values(description=description)
            .where(tasks_tabe.columns.id==pk)
        )
    else:
        stmt = (
            update(tasks_tabe)
            .values(name=name, description=description)
            .where(tasks_tabe.columns.id==pk)
        )
    with engine.connect() as connection:
        connection.execute(stmt)
        connection.commit()

def delete_task(pk: int):
    stmt = delete(tasks_tabe).where(tasks_tabe.columns.id==pk)
    with engine.connect() as connection:
        connection.execute(stmt)
        connection.commit()

def mark_as_complated(pk: int):
    stmt = update(tasks_tabe).values(complated=True).where(tasks_tabe.columns.id==pk)
    with engine.connect() as connection:
        connection.execute(stmt)
        connection.commit()

def mark_as_incomplated(pk: int):
    stmt = update(tasks_tabe).values(complated=False).where(tasks_tabe.columns.id==pk)
    with engine.connect() as connection:
        connection.execute(stmt)
        connection.commit()

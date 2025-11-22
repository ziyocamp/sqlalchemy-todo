import hashlib
from sqlalchemy import (
    insert, select, update, delete
)
from database import engine
from tables import tasks_tabe, users_table, genre_table, movie_table, genre_movie_table


def make_password(password: str):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def create_user(username: str, password: str):
    hashed_password = make_password(password)
    stmt = insert(users_table).values(username=username, hashed_password=hashed_password)
    with engine.connect() as connection:
        connection.execute(stmt)
        connection.commit()

def check_user(username: str, password: str):
    hashed_password = make_password(password)
    stmt = (
        select(users_table)
        .where(
            users_table.columns.username==username, 
            users_table.columns.hashed_password==hashed_password
        )
    )
    with engine.connect() as connection:
        return connection.execute(stmt).first()

def create_task(user_id: int, name: str, description: str | None = None):
    stmt = insert(tasks_tabe).values(name=name, description=description, user_id=user_id)
    with engine.connect() as connection:
        connection.execute(stmt)
        connection.commit()

def get_tasks(user_id: int):
    stmt = select(tasks_tabe).where(tasks_tabe.columns.user_id==user_id)
    with engine.connect() as connection:
        tasks = connection.execute(stmt)
        return list(tasks)

def get_one_task(user_id: int, pk: int):
    stmt = select(tasks_tabe).where(tasks_tabe.columns.id==pk, tasks_tabe.columns.user_id==user_id)
    with engine.connect() as connection:
        existing_task = connection.execute(stmt).first()
        if existing_task is None:
            raise Exception('task not found.')
        return existing_task

def update_task(user_id: int, pk: int, name: str | None = None, description: str | None = None):
    if name is None and description is None:
        return
    elif name is not None and description is None:
        stmt = (
            update(tasks_tabe)
            .values(name=name)
            .where(tasks_tabe.columns.id==pk, tasks_tabe.columns.user_id==user_id)
        )
    elif name is None and description is not None:
        stmt = (
            update(tasks_tabe)
            .values(description=description)
            .where(tasks_tabe.columns.id==pk, tasks_tabe.columns.user_id==user_id)
        )
    else:
        stmt = (
            update(tasks_tabe)
            .values(name=name, description=description)
            .where(tasks_tabe.columns.id==pk, tasks_tabe.columns.user_id==user_id)
        )
    with engine.connect() as connection:
        connection.execute(stmt)
        connection.commit()

def delete_task(user_id: int, pk: int):
    stmt = delete(tasks_tabe).where(tasks_tabe.columns.id==pk, tasks_tabe.columns.user_id==user_id)
    with engine.connect() as connection:
        connection.execute(stmt)
        connection.commit()

def mark_as_complated(user_id: int, pk: int):
    stmt = update(tasks_tabe).values(complated=True).where(tasks_tabe.columns.id==pk, tasks_tabe.columns.user_id==user_id)
    with engine.connect() as connection:
        connection.execute(stmt)
        connection.commit()

def mark_as_incomplated(user_id: int, pk: int):
    stmt = update(tasks_tabe).values(complated=False).where(tasks_tabe.columns.id==pk, tasks_tabe.columns.user_id==user_id)
    with engine.connect() as connection:
        connection.execute(stmt)
        connection.commit()

def get_movie_by_genre(genre: str):
    stmt = select(genre_table).where(genre_table.columns.name==genre)
    with engine.connect() as conn:
        genre = conn.execute(stmt).first()

    if not genre:
        return []
    
    genre_id = genre[0]
    
    stmt = select(genre_movie_table).where(genre_movie_table.columns.genre_id==genre_id)
    with engine.connect() as conn:
        genre_movies = conn.execute(stmt)

    movies = []
    for genre_movie in genre_movies:
        stmt = select(movie_table).where(movie_table.columns.id==genre_movie[2])
        with engine.connect() as conn:
            movies.append(list(conn.execute(stmt)))

    return movies

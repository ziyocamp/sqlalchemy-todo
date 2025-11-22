from datetime import datetime
from sqlalchemy import (
    Table, Column,
    Integer, String, Text, Boolean, DateTime,
    ForeignKey,
)
from database import metadata_obj


users_table = Table(
    'users',
    metadata_obj,
    Column('id', Integer, primary_key=True, unique=True, nullable=False),
    Column('username', String(length=64), nullable=False, unique=Table),
    Column('hashed_password', String(length=255))
)

profile_table = Table(
    'profile',
    metadata_obj,
    Column('id', Integer, primary_key=True, unique=True, nullable=False),
    Column('bio', String(length=255)),
    Column('user_id', ForeignKey('users.id'), nullable=False, unique=True)
)

tasks_tabe = Table(
    'tasks',
    metadata_obj,
    Column('id', Integer, primary_key=True, unique=True, nullable=False),
    Column('name', String(length=32), nullable=False),
    Column('complated', Boolean, nullable=False, default=False),
    Column('description', Text),
    Column('create_at', DateTime, nullable=False, default=datetime.now),
    Column('user_id', ForeignKey('users.id'), nullable=False)
)

posts_table = Table(
    'posts',
    metadata_obj,
    Column('id', Integer, primary_key=True, unique=True, nullable=False),
    Column('content', String(length=255), nullable=False),
    Column('user_id', ForeignKey('users.id'), nullable=False)
)

comments_table = Table(
    'comments',
    metadata_obj,
    Column('id', Integer, primary_key=True, unique=True, nullable=False),
    Column('comment', String(length=127), nullable=False),
    Column('user_id', ForeignKey('users.id'), nullable=False),
    Column('post_id', ForeignKey('posts.id'), nullable=False)
)





genre_table = Table(
    'genre',
    metadata_obj,
    Column('id', Integer, primary_key=True, unique=True, nullable=False),
    Column('name', String(length=127), nullable=False),
)

movie_table = Table(
    'movie',
    metadata_obj,
    Column('id', Integer, primary_key=True, unique=True, nullable=False),
    Column('name', String(length=127), nullable=False),
)

genre_movie_table = Table(
    'genre_movie',
    metadata_obj,
    Column('id', Integer, primary_key=True, unique=True, nullable=False),
    Column('genre_id', ForeignKey('genre.id'), nullable=False),
    Column('movie_id', ForeignKey('movie.id'), nullable=False)
)


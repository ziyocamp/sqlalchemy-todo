from datetime import datetime
from sqlalchemy import (
    Table, Column,
    Integer, String, Text, Boolean, DateTime,
)
from database import metadata_obj


tasks_tabe = Table(
    'tasks',
    metadata_obj,
    Column('id', Integer, primary_key=True, unique=True, nullable=False),
    Column('name', String(length=32), nullable=False),
    Column('complated', Boolean, nullable=False, default=False),
    Column('description', Text),
    Column('create_at', DateTime, nullable=False, default=datetime.now)
)

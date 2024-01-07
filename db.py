from sqlalchemy.ext.asyncio import create_async_engine
from dotenv import load_dotenv
from sqlalchemy.orm import DeclarativeBase
from decouple import config
import os

load_dotenv

engine = create_async_engine(
    url=config("DATABASE_URL"),
    echo=True
)

class Base(DeclarativeBase):
    pass
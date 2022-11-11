# Create the SQLAlchemy parts

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

"""Create a database URL for SQLAlchemy"""
SQLALCHEMY_DATABASE_URL = "sqlite:///sql_app.db"

"""connect_args={"check_same_thread": False} is only needed for SQLite because
by default SQLite will only allow one thread to communicate with it, assuming
that each thread would handle an independent request."""
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
    )

"""Each instance of the SessionLocal class will be a database session."""
SessionLocal = sessionmaker(autocommit=False,
        autoflush=False,
        bind=engine
        )

"""declarative_base() that returns a class"""
Base = declarative_base()

"""
Configuración de la base de datos para la aplicación.

Este módulo inicializa la conexión a la base de datos SQLite usando SQLAlchemy
y proporciona los componentes necesarios (engine, SessionLocal, Base) para
interactuar con ella.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./movies.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
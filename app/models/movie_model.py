"""
Define el modelo de la tabla 'movies' para la base de datos.

Este módulo utiliza SQLAlchemy para mapear la clase `Movie` a la tabla
'movies' en la base de datos, definiendo cada columna y su tipo.
"""
from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Movie(Base):
    """
    Representa una película en la tabla de la base de datos.

    Atributos:
        id (int): Clave primaria.
        title (str): Título de la película.
        overview (str): Resumen de la película.
        year (int): Año de lanzamiento.
        rating (float): Calificación de la película.
        category (str): Categoría de la película.
    """
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    overview = Column(String)
    year = Column(Integer)
    rating = Column(Float)
    category = Column(String, index=True)
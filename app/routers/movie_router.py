"""
Define los endpoints de la API para el recurso de películas.

Este módulo crea un APIRouter que agrupa todas las rutas relacionadas
con las películas (CRUD) y las expone bajo el prefijo '/movies'.
"""
from typing import List
from fastapi import APIRouter, status, Path, Query, HTTPException, Depends
from sqlalchemy.orm import Session

from app.services.movie_service import MovieService
from app.schemas.movie_schema import Movie, MovieCreate, MovieUpdate
from app.dependencies import get_db

movie_router = APIRouter()

@movie_router.get(
    '/',
    tags=['Películas'],
    response_model=List[Movie],
    status_code=status.HTTP_200_OK,
    summary="Obtener todas las películas"
)
def get_movies(db: Session = Depends(get_db)) -> List[Movie]:
    """
    Devuelve una lista de todas las películas almacenadas en la base de datos.
    """
    movies = MovieService().get_movies(db)
    return movies

@movie_router.get(
    '/{movie_id}',
    tags=['Películas'],
    response_model=Movie,
    status_code=status.HTTP_200_OK,
    summary="Obtener una película por su ID"
)
def get_movie(movie_id: int = Path(gt=0), db: Session = Depends(get_db)) -> Movie:
    """
    Devuelve una única película basada en su ID.
    Si la película no se encuentra, devuelve un error 404.
    """
    movie = MovieService().get_movie_by_id(db, movie_id)
    if not movie:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Película no encontrada")
    return movie

@movie_router.get(
    '/by_category/',
    tags=['Películas'],
    response_model=List[Movie],
    status_code=status.HTTP_200_OK,
    summary="Obtener películas por categoría"
)
def get_movies_by_category(category: str = Query(min_length=3, max_length=20), db: Session = Depends(get_db)) -> List[Movie]:
    """
    Devuelve todas las películas que coinciden con una categoría dada.
    Si no se encuentran películas para esa categoría, devuelve una lista vacía.
    """
    movies = MovieService().get_movies_by_category(db, category)
    return movies

@movie_router.post(
    '/',
    tags=['Películas'],
    response_model=Movie,
    status_code=status.HTTP_201_CREATED,
    summary="Crear una nueva película"
)
def create_movie(movie_data: MovieCreate, db: Session = Depends(get_db)) -> Movie:
    """
    Crea una nueva película y la almacena en la base de datos.
    Devuelve la película recién creada.
    """
    new_movie = MovieService().create_movie(db, movie_data)
    return new_movie

@movie_router.put(
    '/{movie_id}',
    tags=['Películas'],
    response_model=Movie,
    status_code=status.HTTP_200_OK,
    summary="Actualizar una película existente"
)
def update_movie(movie_id: int, movie_data: MovieUpdate, db: Session = Depends(get_db)) -> Movie:
    """
    Actualiza una película existente con nuevos datos.
    Si la película no se encuentra, devuelve un error 404.
    """
    updated_movie = MovieService().update_movie(db, movie_id, movie_data)
    if not updated_movie:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Película no encontrada")
    return updated_movie

@movie_router.delete(
    '/{movie_id}',
    tags=['Películas'],
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Eliminar una película"
)
def delete_movie(movie_id: int, db: Session = Depends(get_db)):
    """
    Elimina una película de la base de datos por su ID.
    Si la película no se encuentra, devuelve un error 404.
    """
    was_deleted = MovieService().delete_movie(db, movie_id)
    if not was_deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Película no encontrada")
    return
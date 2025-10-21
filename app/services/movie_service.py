"""
Capa de servicio que encapsula la lógica de negocio para las películas.

Este módulo contiene todas las operaciones de lógica de negocio relacionadas
con las películas, interactuando directamente con la capa de la base de datos.
No contiene lógica de HTTP.
"""
from sqlalchemy.orm import Session
from typing import List

from app.models.movie_model import Movie as MovieModel
from app.schemas.movie_schema import MovieCreate, MovieUpdate

class MovieService:
    """Clase de servicio para la lógica de negocio de las películas."""

    def get_movies(self, db: Session) -> List[MovieModel]:
        """Obtiene todas las películas de la base de datos."""
        return db.query(MovieModel).all()

    def get_movie_by_id(self, db: Session, movie_id: int) -> MovieModel | None:
        """Obtiene una película por su ID."""
        return db.query(MovieModel).filter(MovieModel.id == movie_id).first()

    def get_movies_by_category(self, db: Session, category: str) -> List[MovieModel]:
        """Filtra y obtiene películas por su categoría."""
        return db.query(MovieModel).filter(MovieModel.category == category).all()

    def create_movie(self, db: Session, movie_data: MovieCreate) -> MovieModel:
        """Crea una nueva película y la guarda en la base de datos."""
        new_movie = MovieModel(**movie_data.model_dump())
        db.add(new_movie)
        db.commit()
        db.refresh(new_movie)
        return new_movie

    def update_movie(self, db: Session, movie_id: int, movie_data: MovieUpdate) -> MovieModel | None:
        """Actualiza una película existente en la base de datos."""
        movie = self.get_movie_by_id(db, movie_id)
        if movie:
            movie.title = movie_data.title
            movie.overview = movie_data.overview
            movie.year = movie_data.year
            movie.rating = movie_data.rating
            movie.category = movie_data.category
            db.commit()
            db.refresh(movie)
            return movie
        return None

    def delete_movie(self, db: Session, movie_id: int) -> bool:
        """Elimina una película de la base de datos por su ID."""
        movie = self.get_movie_by_id(db, movie_id)
        if movie:
            db.delete(movie)
            db.commit()
            return True
        return False

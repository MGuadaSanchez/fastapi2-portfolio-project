"""
Define los esquemas de Pydantic para la validación de datos de la API.

Estos esquemas se utilizan para validar los datos de entrada (payloads) en las
peticiones y para dar forma a los datos de salida en las respuestas.
"""
import datetime
from pydantic import BaseModel, Field

class Movie(BaseModel):
    """Esquema base para una película, usado principalmente para respuestas de la API."""
    id: int
    title: str
    overview: str
    year: int
    rating: float
    category: str

    class Config:
        from_attributes = True

class MovieCreate(BaseModel):
    """Esquema para la creación de una nueva película."""
    id: int
    title: str = Field(min_length=5, max_length=15)
    overview: str = Field(min_length=15, max_length=50)
    year: int = Field(le=datetime.date.today().year, ge=1900)
    rating: float = Field(ge=0, le=10)
    category: str = Field(min_length=5, max_length=15)
    
    model_config = {
        'json_schema_extra': {
            'example':{
                'id': 1,
                'title': 'Mi película',
                'overview': 'La película trata sobre...',
                'year': 2022,
                'rating': 8.0,
                'category': 'Acción'
            }          
        }
    }
    
class MovieUpdate(BaseModel):
    """Esquema para actualizar una película existente."""
    title: str
    overview: str
    year: int
    rating: float
    category: str

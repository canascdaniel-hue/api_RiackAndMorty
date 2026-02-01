"""
=============================================================================
DTOs PARA RICK AND MORTY API
=============================================================================

Modelos de datos para la API de Rick and Morty.

Autor: Ing. Daniel Issac Cañas
Fecha: Enero 2026
=============================================================================
"""

from pydantic import BaseModel
from typing import List

class CharacterResponseDTO(BaseModel):
    """DTO para la respuesta de un personaje"""
    
    id: int
    name: str
    status: str
    species: str
    type: str
    gender: str
    origin: str
    location: str
    image: str
    episode_count: int
    created: str

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "Rick Sanchez",
                "status": "Alive",
                "species": "Human",
                "type": "",
                "gender": "Male",
                "origin": "Earth (C-137)",
                "location": "Citadel of Ricks",
                "image": "https://rickandmortyapi.com/api/character/avatar/1.jpeg",
                "episode_count": 51,
                "created": "2017-11-04T18:48:46.250Z"
            }
        }

class SearchResultDTO(BaseModel):
    """DTO para los resultados de búsqueda"""
    
    total: int
    result: List[CharacterResponseDTO]

    class Config:
        json_schema_extra = {
            "example": {
                "total": 2,
                "result": [
                    {
                        "id": 1,
                        "name": "Rick Sanchez",
                        "status": "Alive",
                        "species": "Human",
                        "type": "",
                        "gender": "Male",
                        "origin": "Earth (C-137)",
                        "location": "Citadel of Ricks",
                        "image": "https://rickandmortyapi.com/api/character/avatar/1.jpeg",
                        "episode_count": 51,
                        "created": "2017-11-04T18:48:46.250Z"
                    }
                ]
            }
        }

class StatusesResponseDTO(BaseModel):
    """DTO para la respuesta de estados de personajes"""
    
    statuses: List[str]

    class Config:
        json_schema_extra = {
            "example": {
                "statuses": ["alive", "dead", "unknown"]
            }
        }

class ErrorResponseDTO(BaseModel):
    """DTO para respuestas de error"""
    
    error: str
    message: str
    status_code: int

    class Config:
        json_schema_extra = {
            "example": {
                "error": "Bad Request",
                "message": "La búsqueda debe tener al menos 2 caracteres",
                "status_code": 400
            }
        }
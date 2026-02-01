"""
=============================================================================
CONTROLADOR DE RICK AND MORTY
=============================================================================

Controlador para los endpoints de Rick and Morty.

Autor: Ing. Daniel Issac Cañas
Fecha: Enero 2026
=============================================================================
"""

import httpx
from fastapi import APIRouter, Query, Path
from services.rickMortyServices import RickMortyService
from DTOs.rickMortyDtos import CharacterResponseDTO, SearchResultDTO, StatusesResponseDTO

router = APIRouter(prefix="/api")

@router.get("/test")
async def test_endpoint():
    """Endpoint de prueba simple"""
    return {
        "message": "🛸 Rick and Morty API funcionando correctamente!",
        "status": "OK",
        "endpoints": {
            "random_character": "/api/character/random",
            "character_statuses": "/api/character/statuses",
            "character_by_status": "/api/character/status/{status}",
            "search_characters": "/api/character/search?q={query}"
        }
    }

@router.get("/character/mock")
async def get_mock_character():
    """Obtiene un personaje mock para pruebas"""
    return {
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

@router.get("/character/random", response_model=CharacterResponseDTO)
async def get_random_character():
    """Obtiene un personaje aleatorio de Rick and Morty"""
    
    async with httpx.AsyncClient() as http_client:
        rick_service = RickMortyService()
        character = await rick_service.get_random_character(http_client)
        return character

@router.get("/character/statuses", response_model=StatusesResponseDTO)
async def get_character_statuses():
    """Obtiene todos los estados de personajes disponibles"""
    
    async with httpx.AsyncClient() as http_client:
        rick_service = RickMortyService()
        statuses = await rick_service.get_character_statuses(http_client)
        return statuses

@router.get("/character/status/{status}", response_model=CharacterResponseDTO)
async def get_character_by_status(
    status: str = Path(..., description="Estado del personaje (alive, dead, unknown)")
):
    """Obtiene un personaje aleatorio por estado"""
    
    async with httpx.AsyncClient() as http_client:
        rick_service = RickMortyService()
        character = await rick_service.get_character_by_status(status, http_client)
        return character

@router.get("/character/search", response_model=SearchResultDTO)
async def search_characters(
    q: str = Query(..., min_length=2, description="Término de búsqueda (mínimo 2 caracteres)")
):
    """Busca personajes que contengan una palabra específica en el nombre"""
    
    async with httpx.AsyncClient() as http_client:
        rick_service = RickMortyService()
        results = await rick_service.search_characters(q, http_client)
        return results
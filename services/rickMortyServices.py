"""
=============================================================================
SERVICIO DE RICK AND MORTY
=============================================================================

Servicio para obtener personajes de Rick and Morty.

Autor: Ing. Daniel Issac Cañas
Fecha: Enero 2026
=============================================================================
"""

import httpx
from clients.rickMortyClient import RickMortyClient
from DTOs.rickMortyDtos import CharacterResponseDTO, SearchResultDTO, StatusesResponseDTO

class RickMortyService:
    """Servicio para obtener personajes de Rick and Morty"""

    def __init__(self):
        self.client = RickMortyClient()

    def _transform_character(self, character_data: dict) -> CharacterResponseDTO:
        """Transforma un personaje de la API en DTO"""
        
        return CharacterResponseDTO(
            id=character_data["id"],
            name=character_data["name"],
            status=character_data["status"],
            species=character_data["species"],
            type=character_data.get("type", ""),
            gender=character_data["gender"],
            origin=character_data["origin"]["name"],
            location=character_data["location"]["name"],
            image=character_data["image"],
            episode_count=len(character_data.get("episode", [])),
            created=character_data["created"]
        )

    async def get_random_character(self, http_client: httpx.AsyncClient) -> CharacterResponseDTO:
        """Obtiene un personaje aleatorio"""
        
        character_data = await self.client.get_random_character(http_client)
        return self._transform_character(character_data)

    async def get_character_by_status(self, status: str, http_client: httpx.AsyncClient) -> CharacterResponseDTO:
        """Obtiene un personaje aleatorio por estado (alive, dead, unknown)"""
        
        character_data = await self.client.get_character_by_status(status, http_client)
        return self._transform_character(character_data)

    async def get_character_statuses(self, http_client: httpx.AsyncClient) -> StatusesResponseDTO:
        """Obtiene todos los estados disponibles"""
        
        statuses = await self.client.get_character_statuses(http_client)
        return StatusesResponseDTO(statuses=statuses)

    async def search_characters(self, query: str, http_client: httpx.AsyncClient) -> SearchResultDTO:
        """Busca personajes que contengan una palabra específica en el nombre"""
        
        search_data = await self.client.search_characters(query, http_client)
        
        characters = []
        for character_data in search_data.get("results", []):
            characters.append(self._transform_character(character_data))
        
        return SearchResultDTO(
            total=len(characters),
            result=characters
        )
"""
=============================================================================
CLIENTE HTTP PARA RICK AND MORTY API
=============================================================================

Cliente para interactuar con la API de Rick and Morty (rickandmortyapi.com).

Autor: Ing. Daniel Issac Cañas
Fecha: Enero 2026
=============================================================================
"""

import httpx
from fastapi import HTTPException
from appsettings import settings

class RickMortyClient:
    """Cliente HTTP para Rick and Morty API"""

    async def get_random_character(self, http_client: httpx.AsyncClient) -> dict:
        """Obtiene un personaje aleatorio de Rick and Morty"""
        
        try:
            # Obtener un personaje aleatorio (hay 826 personajes)
            import random
            character_id = random.randint(1, 826)
            
            timeout_config = httpx.Timeout(
                connect=settings.CONNECT_TIMEOUT,
                read=settings.REQUEST_TIMEOUT,
                write=settings.REQUEST_TIMEOUT,
                pool=settings.REQUEST_TIMEOUT
            )
            
            response = await http_client.get(
                f"{settings.RICK_MORTY_CHARACTER_URL}/{character_id}",
                timeout=timeout_config
            )

            if response.status_code != 200:
                raise HTTPException(
                    status_code=response.status_code,
                    detail="Error al obtener personaje de Rick and Morty"
                )

            return response.json()
        
        except httpx.ConnectTimeout:
            raise HTTPException(
                status_code=504,
                detail="Timeout al conectar con la API de Rick and Morty. Intenta de nuevo."
            )
        except httpx.RequestError as e:
            raise HTTPException(
                status_code=503,
                detail=f"Error de conexión: {str(e)}"
            )
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Error inesperado: {str(e)}"
            )

    async def get_character_by_status(self, status: str, http_client: httpx.AsyncClient) -> dict:
        """Obtiene personajes filtrados por estado (alive, dead, unknown)"""
        
        try:
            timeout_config = httpx.Timeout(
                connect=settings.CONNECT_TIMEOUT,
                read=settings.REQUEST_TIMEOUT,
                write=settings.REQUEST_TIMEOUT,
                pool=settings.REQUEST_TIMEOUT
            )
            
            response = await http_client.get(
                settings.RICK_MORTY_CHARACTER_URL,
                params={"status": status},
                timeout=timeout_config
            )

            if response.status_code != 200:
                raise HTTPException(
                    status_code=response.status_code,
                    detail=f"Error al obtener personajes con estado {status}"
                )

            data = response.json()
            if data.get("results"):
                import random
                return random.choice(data["results"])
            else:
                raise HTTPException(
                    status_code=404,
                    detail=f"No se encontraron personajes con estado {status}"
                )
        
        except httpx.ConnectTimeout:
            raise HTTPException(
                status_code=504,
                detail="Timeout al conectar con la API de Rick and Morty. Intenta de nuevo."
            )
        except httpx.RequestError as e:
            raise HTTPException(
                status_code=503,
                detail=f"Error de conexión: {str(e)}"
            )

    async def get_character_statuses(self, http_client: httpx.AsyncClient) -> list:
        """Obtiene las categorías disponibles (estados de personajes)"""
        
        # Rick and Morty API tiene estados fijos
        return ["alive", "dead", "unknown"]

    async def search_characters(self, query: str, http_client: httpx.AsyncClient) -> dict:
        """Busca personajes que contengan una palabra específica en el nombre"""
        
        if not query or len(query.strip()) < 2:
            raise HTTPException(
                status_code=400,
                detail="La búsqueda debe tener al menos 2 caracteres"
            )
        
        try:
            timeout_config = httpx.Timeout(
                connect=settings.CONNECT_TIMEOUT,
                read=settings.REQUEST_TIMEOUT,
                write=settings.REQUEST_TIMEOUT,
                pool=settings.REQUEST_TIMEOUT
            )
            
            response = await http_client.get(
                settings.RICK_MORTY_CHARACTER_URL,
                params={"name": query.strip()},
                timeout=timeout_config
            )

            if response.status_code != 200:
                raise HTTPException(
                    status_code=response.status_code,
                    detail="Error al buscar personajes"
                )

            return response.json()
        
        except httpx.ConnectTimeout:
            raise HTTPException(
                status_code=504,
                detail="Timeout al conectar con la API de Rick and Morty. Intenta de nuevo."
            )
        except httpx.RequestError as e:
            raise HTTPException(
                status_code=503,
                detail=f"Error de conexión: {str(e)}"
            )
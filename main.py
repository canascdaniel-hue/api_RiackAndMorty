"""
=============================================================================
APLICACIÓN FASTAPI - RICK AND MORTY API
=============================================================================

API para explorar el universo de Rick and Morty.

Autor: Ing. Daniel Issac Cañas
Fecha: Enero 2026
=============================================================================
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from appsettings import settings
from controllers.rickMortyController import router as rick_router

# Crear aplicación FastAPI
app = FastAPI(
    title=settings.API_TITLE,
    description=settings.API_DESCRIPTION,
    version=settings.API_VERSION,
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=settings.ALLOWED_METHODS,
    allow_headers=settings.ALLOWED_HEADERS,
)

# Incluir rutas de Rick and Morty
app.include_router(rick_router, tags=["Rick and Morty"])

# Endpoint de bienvenida
@app.get("/")
async def home():
    """Endpoint de bienvenida"""
    return {
        "message": "🛸 ¡Bienvenido a Rick and Morty API!",
        "description": "La API más científica para explorar el universo de Rick and Morty",
        "version": settings.API_VERSION,
        "docs": "/docs",
        "endpoints": {
            "random_character": "/api/character/random",
            "character_statuses": "/api/character/statuses",
            "character_by_status": "/api/character/status/{status}",
            "search_characters": "/api/character/search?q={query}"
        },
        "fun_fact": "Wubba Lubba Dub Dub! - Rick Sanchez"
    }

# Ejecutar aplicación
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(
#         "main:app",
#         host=settings.HOST,
#         port=settings.PORT,
#         reload=settings.DEBUG
#     )

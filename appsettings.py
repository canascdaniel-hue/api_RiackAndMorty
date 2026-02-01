"""
=============================================================================
CONFIGURACIÓN DE VARIABLES DE ENTORNO - RICK AND MORTY API
=============================================================================

Este archivo centraliza la carga y configuración de todas las variables
de entorno de la aplicación Rick and Morty.

Autor: Ing. Daniel Issac Cañas
Fecha: Enero 2026
=============================================================================
"""

import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

class AppSettings:
    """Configuración centralizada de la aplicación Rick and Morty"""
    
    # =============================================================================
    # CONFIGURACIÓN DEL SERVIDOR
    # =============================================================================
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", "8000"))
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
    
    # =============================================================================
    # CONFIGURACIÓN DE LA API
    # =============================================================================
    API_TITLE = "Rick and Morty API"
    API_DESCRIPTION = "API para explorar el universo de Rick and Morty"
    API_VERSION = "1.0.0"
    
    # =============================================================================
    # RICK AND MORTY API (COMPLETAMENTE GRATUITA)
    # =============================================================================
    RICK_MORTY_BASE_URL = "https://rickandmortyapi.com/api"
    RICK_MORTY_CHARACTER_URL = f"{RICK_MORTY_BASE_URL}/character"
    RICK_MORTY_LOCATION_URL = f"{RICK_MORTY_BASE_URL}/location"
    RICK_MORTY_EPISODE_URL = f"{RICK_MORTY_BASE_URL}/episode"
    
    # =============================================================================
    # CONFIGURACIÓN HTTP
    # =============================================================================
    REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", "30"))
    MAX_RETRIES = int(os.getenv("MAX_RETRIES", "3"))
    CONNECT_TIMEOUT = int(os.getenv("CONNECT_TIMEOUT", "10"))
    
    # =============================================================================
    # CONFIGURACIÓN CORS
    # =============================================================================
    ALLOWED_ORIGINS = ["*"]
    ALLOWED_METHODS = ["GET", "POST", "PUT", "DELETE"]
    ALLOWED_HEADERS = ["*"]
    
    # =============================================================================
    # MÉTODOS DE UTILIDAD
    # =============================================================================
    
    @classmethod
    def print_config_summary(cls):
        """Imprime un resumen de la configuración actual"""
        print("=" * 60)
        print("🛸 RICK AND MORTY API - CONFIGURACIÓN")
        print("=" * 60)
        print(f"🌐 Servidor: {cls.HOST}:{cls.PORT}")
        print(f"🔧 Debug: {'Activado' if cls.DEBUG else 'Desactivado'}")
        print("🧪 Rick and Morty API: disponible (gratuita)")
        print(f"⏱️  Timeout: {cls.REQUEST_TIMEOUT}s")
        print(f"🔄 Reintentos: {cls.MAX_RETRIES}")
        print("=" * 60)
        print("✅ API completamente funcional sin configuración adicional")
        print("=" * 60)

# Instancia global de configuración
settings = AppSettings()

# Imprimir resumen de configuración al importar (solo en modo debug)
if settings.DEBUG:
    settings.print_config_summary()
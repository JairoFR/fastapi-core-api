from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    """
    Configuración central de la aplicación.
    Lee automáticamente desde el archivo .env
    """
    # Datos básicos de la API
    app_name: str = "Motor Facturas API"
    version: str = "1.0.0"
    description: str = "API profesional para gestión de facturas"
    debug: bool = False

    class Config:
        # Le dice a Pydantic dónde está el archivo de configuración
        env_file = ".env"

# lru_cache = guarda la configuración en memoria
# evita leer el archivo .env en cada petición
# es como un singleton — solo se crea una vez
@lru_cache()
def get_settings() -> Settings:
    return Settings()
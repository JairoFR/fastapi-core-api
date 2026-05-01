from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.routers import facturas
from app.core.config import get_settings

# Carga la configuración
settings = get_settings()

# Crea la aplicación con metadata profesional
app = FastAPI(
    title=settings.app_name,
    version=settings.version,
    description=settings.description,
)

# ── Manejo global de errores ──────────────────────────
# Captura CUALQUIER error no manejado en toda la API
# En vez de explotar devuelve JSON limpio
@app.exception_handler(Exception)
async def error_global(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "error": "Error interno del servidor",
            "detalle": str(exc)
        }
    )

# ── Healthcheck ───────────────────────────────────────
# Endpoint que usan los servidores para saber
# si tu API está viva
# Docker, Railway, AWS lo llaman automáticamente
@app.get("/health", tags=["Sistema"])
def health():
    return {
        "estado": "ok",
        "version": settings.version,
        "app": settings.app_name
    }

# ── Registrar routers ─────────────────────────────────
# Conecta los endpoints de facturas a la app principal
app.include_router(facturas.router)
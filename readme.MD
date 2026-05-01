#  FastAPI Core API

API REST profesional para gestión de facturas construida con FastAPI.

##  Stack tecnológico

- **Python 3.11**
- **FastAPI** — framework para APIs REST
- **Pydantic v2** — validación de datos
- **Docker** — contenedorización
- **Uvicorn** — servidor ASGI

##  Estructura del proyecto

```
app/
├── core/        # configuración central
├── models/      # modelos Pydantic
├── routers/     # endpoints por módulo
└── main.py      # entrada principal
```

##  Cómo correr el proyecto

### Con Docker
```bash
docker build -t fastapi-core-api .
docker run -p 8000:8000 fastapi-core-api
```

### Sin Docker
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

##  Endpoints

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | /health | Estado del servidor |
| GET | /facturas | Listar todas |
| POST | /facturas | Crear nueva |
| GET | /facturas/{numero} | Buscar una |
| PUT | /facturas/{numero} | Actualizar |
| DELETE | /facturas/{numero} | Eliminar |

##  Documentación

Accede al Swagger UI en:

```
http://localhost:8000/docs
```
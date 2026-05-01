from fastapi import APIRouter, HTTPException
from typing import List
from app.models.factura import FacturaCreate, FacturaUpdate, FacturaResponse
from datetime import datetime

# APIRouter = mini aplicación FastAPI
# agrupa endpoints relacionados
# se registra en main.py
router = APIRouter(
    prefix="/facturas",     # todas las rutas empiezan con /facturas
    tags=["Facturas"],      # agrupa en Swagger
)

# Base de datos en memoria por ahora
# después será PostgreSQL
facturas_db: List[dict] = []
contador_id: int = 0

@router.get("/", response_model=List[FacturaResponse])
def obtener_facturas():
    """Retorna todas las facturas"""
    return facturas_db

@router.post("/", response_model=FacturaResponse, status_code=201)
def crear_factura(factura: FacturaCreate):
    """Crea una nueva factura"""
    global contador_id
    contador_id += 1
    nueva = {
        **factura.model_dump(),  # desempaca el modelo
        "id": contador_id,
        "creado_en": datetime.now()
    }
    facturas_db.append(nueva)
    return nueva

@router.get("/{numero}", response_model=FacturaResponse)
def obtener_factura(numero: str):
    """Busca una factura por número"""
    for f in facturas_db:
        if f["numero"] == numero:
            return f
    # Si no existe lanza error 404 automáticamente
    raise HTTPException(status_code=404, detail=f"Factura {numero} no encontrada")

@router.put("/{numero}", response_model=FacturaResponse)
def actualizar_factura(numero: str, datos: FacturaUpdate):
    """Actualiza una factura existente"""
    for f in facturas_db:
        if f["numero"] == numero:
            # Solo actualiza los campos que llegaron
            actualizacion = datos.model_dump(exclude_none=True)
            f.update(actualizacion)
            return f
    raise HTTPException(status_code=404, detail=f"Factura {numero} no encontrada")

@router.delete("/{numero}")
def eliminar_factura(numero: str):
    """Elimina una factura"""
    for i, f in enumerate(facturas_db):
        if f["numero"] == numero:
            facturas_db.pop(i)
            return {"mensaje": f"Factura {numero} eliminada ✅"}
    raise HTTPException(status_code=404, detail=f"Factura {numero} no encontrada")
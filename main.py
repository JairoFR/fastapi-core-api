from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

# Modelo de datos
class Factura(BaseModel):
    numero: str
    cliente: str
    monto: float
    pagado: bool = False

# Base de datos falsa por ahora
facturas_db = []

@app.get("/")
def inicio():
    return {"mensaje": "Mi primera API funcionando ✅"}

@app.get("/facturas")
def obtener_facturas():
    return {"total": len(facturas_db), "facturas": facturas_db}

@app.post("/facturas")
def crear_factura(factura: Factura):
    facturas_db.append(factura.model_dump())
    return {"mensaje": "Factura creada ✅", "factura": factura}

@app.get("/facturas/{numero}")
def buscar_factura(numero: str):
    for f in facturas_db:
        if f["numero"] == numero:
            return f
    return {"error": f"Factura {numero} no encontrada"}


@app.put("/facturas/{numero}")
def actualizar_factura(numero: str, factura: Factura):
    for i, f in enumerate(facturas_db):
        if f["numero"] == numero:
            facturas_db[i] = factura.model_dump()
            return {"mensaje": "Factura actualizada ✅", "factura": factura}
    return {"error": f"Factura {numero} no encontrada"}

@app.delete("/facturas/{numero}")
def eliminar_factura(numero: str):
    for i, f in enumerate(facturas_db):
        if f["numero"] == numero:
            facturas_db.pop(i)
            return {"mensaje": f"Factura {numero} eliminada ✅"}
    return {"error": f"Factura {numero} no encontrada"}
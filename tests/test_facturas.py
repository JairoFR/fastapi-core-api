from fastapi.testclient import TestClient
from app.main import app

# Cliente de prueba — simula peticiones HTTP
# sin levantar el servidor real
client = TestClient(app)

# ── Healthcheck ───────────────────────────────────────
def test_health():
    """El servidor debe responder ok"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["estado"] == "ok"

# ── Crear factura ─────────────────────────────────────
def test_crear_factura():
    """Debe crear una factura y devolver id"""
    response = client.post("/facturas/", json={
        "numero": "F-001",
        "cliente": "Empresa ABC",
        "monto": 150000,
        "pagado": False
    })
    assert response.status_code == 201
    data = response.json()
    assert data["numero"] == "F-001"
    assert data["id"] == 1

# ── Obtener facturas ──────────────────────────────────
def test_obtener_facturas():
    """Debe retornar lista de facturas"""
    response = client.get("/facturas/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# ── Buscar factura existente ──────────────────────────
def test_buscar_factura_existe():
    """Debe encontrar la factura F-001"""
    response = client.get("/facturas/F-001")
    assert response.status_code == 200
    assert response.json()["numero"] == "F-001"

# ── Buscar factura inexistente ────────────────────────
def test_buscar_factura_no_existe():
    """Debe retornar 404 si no existe"""
    response = client.get("/facturas/F-999")
    assert response.status_code == 404

# ── Actualizar factura ────────────────────────────────
def test_actualizar_factura():
    """Debe actualizar el monto"""
    response = client.put("/facturas/F-001", json={
        "monto": 200000
    })
    assert response.status_code == 200
    assert response.json()["monto"] == 200000

# ── Eliminar factura ──────────────────────────────────
def test_eliminar_factura():
    """Debe eliminar la factura"""
    response = client.delete("/facturas/F-001")
    assert response.status_code == 200
    assert "eliminada" in response.json()["mensaje"]
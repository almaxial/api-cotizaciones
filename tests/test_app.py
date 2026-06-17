from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_raiz_responde_ok():
    respuesta = client.get("/")

    assert respuesta.status_code == 200

def test_dolar_devuelve_compra_y_venta():
    r = client.get("/dolar/blue")
    assert r.status_code == 200
    datos = r.json()
    assert "compra" in datos
    assert "venta" in datos
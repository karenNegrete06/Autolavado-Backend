import pytest
from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)

def test_create_user():
    payload = {
        "rol_id": 1,
        "nombre": "Test",
        "papellido": "Test",
        "sapellido": "Test",
        "direccion": "Test",
        "telefono": "123456789",
        "correo": "test@example.com",
        "password": "testpassword",
        "estatus": True,
        "fecha_registro": "2026-02-25T00:00:00",
        "fecha_modificacion": "2026-02-25T00:00:00"
    }

    response = client.post("/user/", json=payload)

    assert response.status_code in [200, 201]

    data = response.json()

    assert data["correo"] == payload["correo"]
    assert data["nombre"] == "Test"
    assert "password" not in data


def test_crear_usuario_invalidos():
    payload_invalido = {
        "rol_id": "no-es-un-numero",
        "nombre": "Error"
    }

    response = client.post("/user/", json=payload_invalido)

    assert response.status_code == 422
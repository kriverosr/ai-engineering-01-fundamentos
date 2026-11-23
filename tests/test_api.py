from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health():
    respuesta = client.get("/health")

    assert respuesta.status_code == 200
    assert respuesta.json() == {"status": "ok"}


def test_incidente_urgente():
    respuesta = client.post(
        "/clasificar",
        json={
            "cliente": "Empresa ABC",
            "mensaje": "El sistema está caído y no puedo facturar.",
            "canal": "web",
        },
    )

    assert respuesta.status_code == 200
    resultado = respuesta.json()
    assert resultado["categoria"] == "incidente"
    assert resultado["prioridad"] == "alta"
    assert resultado["requiere_atencion"] is True


def test_rechaza_mensaje_corto():
    respuesta = client.post(
        "/clasificar",
        json={
            "cliente": "Empresa ABC",
            "mensaje": "Hola",
            "canal": "correo",
        },
    )

    assert respuesta.status_code == 422
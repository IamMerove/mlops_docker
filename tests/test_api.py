from fastapi.testclient import TestClient
from app_api.main import app  # Importe ton instance FastAPI

client = TestClient(app)


# --- Test de la logique mathématique ---
def test_math_logic():
    # Remplace par le nom de ta fonction réelle
    from maths.mon_module import square

    assert square(5) == 25
    assert square(0) == 0


# --- Test de l'API (Routes) ---
def test_read_main():
    # Teste si ton API est en vie
    response = client.get("/")
    assert response.status_code == 200


def test_post_data():
    # Teste l'envoi d'un calcul
    payload = {"operation": "square", "value": 5}
    response = client.get("/data")
    assert response.status_code in [200, 201]  # Dépend de ton code

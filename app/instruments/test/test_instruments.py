from fastapi.testclient import TestClient
from ...main import app


client = TestClient(app)

INSTRUMENTS = [
    "iris_scissor",
    "needle_holder",
    "bip_fx",
    "speculum",
    "con_scissor",
    "spatula",
    "cap_fx",
    "suction_cannula",
    "curved_cannula",
]


def test_get_single_data():
    for instrument in INSTRUMENTS:
        response = client.get(f"/instrument/get/{instrument}")
        assert response.status_code == 200


def test_get_single_data_not_found():
    response = client.get("/instrument/get/random_instrument")
    assert response.status_code == 404


def test_get_all_data():
    response = client.get("/instrument/get_all")
    assert response.status_code == 200


def test_get_image():
    for instrument in INSTRUMENTS:
        response = client.get(f"/instrument/image/{instrument}")
        assert response.status_code == 200


def test_get_image_not_found():
    response = client.get("/instrument/image/random_text")
    assert response.status_code == 404

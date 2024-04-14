import base64
from fastapi.testclient import TestClient
from ...main import app
from os import path


client = TestClient(app)


def test_prediction():
    # Open the image
    file = path.dirname(path.realpath(__file__)) + "/test.jpg"
    with open(file, "rb") as img_file:
        # Encode the image to base64
        img_str = base64.b64encode(img_file.read())

    # Send a POST request to the API
    response = client.post(
        "/predict/",
        json={
            "image": img_str.decode("utf-8"),
        },
    )

    # Decode the image from base64
    img = base64.b64decode(response.json()["image"])

    # Save the image
    with open(path.dirname(path.realpath(__file__)) + "/output.jpg", "wb") as img_file:
        img_file.write(img)

    # Assert the status code
    assert response.status_code == 200
    # Assert the detected objects
    # assert response.json()["objects"] == [
    #     [8, "con_scissor"],
    #     [7, "spatula"],
    #     [6, "suction_cannula"],
    #     [5, "curved_cannula"],
    #     [4, "cap_fx"],
    #     [2, "iris_scissor"],
    #     [3, "needle_holder"],
    #     [0, "speculum"],
    #     [1, "bip_fx"],
    # ]


def test_prediction_no_image():
    # Send a POST request to the API
    response = client.post(
        "/predict/",
        json={
            "image": "",
        },
    )

    # Assert the status code
    assert response.status_code == 422


def test_prediction_no_image_key():
    # Send a POST request to the API
    response = client.post(
        "/predict/",
        json={},
    )

    # Assert the status code
    assert response.status_code == 422

from fastapi.testclient import TestClient

from main_fast_api import app

client = TestClient(app)


def test_get_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "All right, there is a connection."}


def test_post_predict_one():
    response = client.post(
        "/predict/", json={"text": "Не ищи счастье – оно всегда у тебя внутри"}
    )
    json_data = response.json()

    assert response.status_code == 200
    assert json_data == "Яна заўсёды ў цябе ўнутры"


def test_post_predict_two():
    response = client.post("/predict/", json={"text": "Отличная сегодня погода!"})
    json_data = response.json()

    assert response.status_code == 200
    assert json_data == "Выдатная сёння надвор'е!"

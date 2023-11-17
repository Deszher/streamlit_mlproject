import pytest
from fastapi.testclient import TestClient
from main_fast_api import app

client = TestClient(app)

translate_testdata = [
    ("Не ищи счастье – оно всегда у тебя внутри", "Яна заўсёды ў цябе ўнутры"),
    ("Отличная сегодня погода!", "Выдатная сёння надвор'е!"),
]


def test_get_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.text.find("/docs") != -1


@pytest.mark.parametrize("input,expected_output", translate_testdata)
def test_post_predict(input, expected_output):
    response = client.post(
        "/predict/", json={"text": input}
    )
    json_data = response.json()

    assert response.status_code == 200
    assert "result" in json_data
    assert json_data["result"] == expected_output

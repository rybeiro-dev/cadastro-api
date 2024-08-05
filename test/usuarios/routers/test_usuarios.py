from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_must_list_user():
    response = client.get('/usuarios')

    assert response.status_code == 200
    print(response.json())
    assert response.json() == [
        {'id': 1, 'nome': 'Fabio', 'email': 'fabio@fabio.com'}
    ]


def test_must_create_user():
    user = {
        "nome": "Lala",
        "email": "lala@lala.com"
    }

    user_copy = user.copy()
    user_copy["id"] = 2

    response = client.post("/usuarios", json=user)

    assert response.status_code == 201

    assert response.json() == user_copy


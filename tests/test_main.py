# test_main.py
from fastapi.testclient import TestClient
from main import app  # Импортируем приложение из main.py

client = TestClient(app)

def test_read_hello():
    """Тест для маршрута /hello"""
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello world from Python with love"}

def test_favicon():
    """Тест для маршрута /favicon.ico"""
    response = client.get("/favicon.ico")
    assert response.status_code == 200
    assert response.json() == {"message": "No favicon provided"}

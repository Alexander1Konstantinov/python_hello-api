# test_main.py
from fastapi.testclient import TestClient
from main import app, MessageService


class TestMessageService:
    def test_get_hello_message(self):
        message_service = MessageService()

        result = message_service.get_hello_message()
        assert result == {"message": "Hello world from Python with love"}


class TestFastAPI:
    def setup_method(self):
        self.client = TestClient(app)

    def test_read_hello(self):
        response = self.client.get("/hello")

        assert response.status_code == 200
        assert response.json() == {"message": "Hello world from Python with love"}

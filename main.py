from fastapi import FastAPI

app = FastAPI()

# Игнорируем запрос на /favicon.ico
@app.get("/favicon.ico")
def favicon():
    return {"message": "No favicon provided"}

class MessageService:
    def get_hello_message(self):
        return {"message": "Hello World"}

message_service = MessageService()

@app.get("/hello")
def read_hello():
    return message_service.get_hello_message()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=3033)

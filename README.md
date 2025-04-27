
# FastAPI Application Instructions

## Requirements
Make sure you have Python 3.7+ installed on your system.

### Install dependencies
To get started with this FastAPI application, first install the necessary dependencies:

```bash
pip install fastapi uvicorn
```

### Create `.env` File (Optional)
If you want to specify a custom port, create a `.env` file in the project directory with the following content:

```
PORT=3033
```

### Run the Application
To run the FastAPI application, use the following command:

```bash
uvicorn main:app --reload --host 127.0.0.1 --port 3033
```

- `main:app` refers to the `main.py` file where the FastAPI app is defined.
- `--reload` enables auto-reloading during development.
- `--host 127.0.0.1` specifies that the server will run on your local machine.
- `--port 3033` defines the port to use. You can change it as needed.

After running the command, you should see something like this:

```
INFO:     Will watch for changes in these directories: ['.']
INFO:     Uvicorn running on http://127.0.0.1:3033 (Press CTRL+C to quit)
```

### Accessing the Application
Once the server is running, you can access the endpoint at:

```
http://127.0.0.1:3033/hello
```

You should get a response like this:

```json
{
  "message": "Hello world"
}
```

### Accessing Swagger Documentation (Optional)
FastAPI automatically generates interactive API documentation. You can access it at:

```
http://127.0.0.1:3033/docs
```

### Stopping the Server
To stop the server, press `CTRL+C` in the terminal where the server is running.

---

## Troubleshooting

- If you encounter an error regarding the missing favicon (404 or 500), this is expected as browsers attempt to fetch a favicon.ico file. If you don’t want to provide a favicon, simply ignore these requests.

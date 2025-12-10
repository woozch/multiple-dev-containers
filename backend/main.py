from fastapi import FastAPI

app = FastAPI(title="Hello World API")

@app.get("/hello")
def read_hello():
    return {"message": "Hello World"}
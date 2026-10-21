from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Привет! Это твой первый сервер на FastAPI!"}

import uvicorn
from fastapi import FastAPI
from usuarios.router import usuarios

app = FastAPI(title="Cadastro de usuários")

app.include_router(usuarios.router)


@app.get("/")
def index():
    return {"message": "Api para cadastro de usuários."}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, workers=1)

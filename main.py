import uvicorn
from fastapi import FastAPI
from usuarios.routers import usuarios_router
from databases.connection import Base, engine

# from usuarios.models.usuario_model import Usuario
# Base.metadata.drop_all(bind=engine)
# Base.metadata.create_all(bind=engine)

app = FastAPI(title="Cadastro de usuários")

app.include_router(usuarios_router.router)


@app.get("/")
def index():
    return {"message": "Api para cadastro de usuários."}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, workers=1)

# unit_1_API/main.py

from fastapi import FastAPI
from routers.director import router as directors_router
from routers.film import router as films_router
from routers.auth_user import router as auth_users_router
from fastapi.staticfiles import StaticFiles

# Inicializamos la aplicación
app = FastAPI()

# Incluimos los routers
app.include_router(directors_router)
app.include_router(films_router)
app.include_router(auth_users_router)

app.mount("/static", StaticFiles(directory="static"),name="static")

# Ruta raíz de bienvenida
@app.get("/")
def read_root():
    return {"hello": "world"}


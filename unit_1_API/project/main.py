# unit_1_API/main.py

from fastapi import FastAPI
from routers.book import router as books_router
from routers.author import router as authors_router
from routers.auth_users import router as auth_users_router
from fastapi.staticfiles import StaticFiles
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

# Inicializamos la aplicación
app = FastAPI()

# Incluimos los routers
app.include_router(books_router)
app.include_router(authors_router)
app.include_router(auth_users_router)
app.include_router()
app.mount("/static", StaticFiles(directory="static"),name="static")

# Ruta raíz de bienvenida
@app.get("/")
def read_root():
    return {"hello": "world"}
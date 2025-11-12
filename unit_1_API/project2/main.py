from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# --- CORRECCIÓN CRÍTICA DE IMPORTACIÓN ---
# Usamos "." para indicar que 'routers' está dentro del paquete actual (unit_1_API).
from routers.director import router as directors_router
from routers.film import router as films_router
from routers.auth_user import router as auth_users_router
# ----------------------------------------

# Inicializamos la aplicación
app = FastAPI()

# Incluimos los routers
app.include_router(directors_router)
app.include_router(films_router)
app.include_router(auth_users_router)

# Montamos los archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Ruta raíz de bienvenida
@app.get("/")
def read_root():
    return {"hello": "world"}
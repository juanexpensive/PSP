import datetime
from pydantic import BaseModel
from fastapi import Depends, FastAPI, HTTPException, APIRouter

import jwt

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt.exceptions import InvalidTokenError
from pwdlib import PasswordHash



router= APIRouter()
oauth2 = OAuth2PasswordBearer(tokenUrl="login")

#Definimos el algoritmo de encriptacion
ALGORITHIM = "HS256"

#Duracion del token
ACCESS_TOKEN_EXPIRE_MINUTES = 1

#Clave que se utilizara como semilla para generar el token
#openssl rand -hex 32 

SECRET_KEY = "f21d90bab26a85de30ff95b2ad9c946b36530dec062cfad0aee4cd852b15ed5e"

#Objeto que se utilizara para el calculo del hash y
#la verificacion de las contraseñas

password_hash = PasswordHash.recommended()

class User(BaseModel):
    username : str
    fullname : str
    email : str
    disable : bool


class UserDB (User):
    password: str


users_db = {
    "juanclassy" : {
        "username" : "juanclassy",
        "fullname" : "Juan Caro",
        "email" : "carovaquerojuan@gmail.com",
        "disable" : False,
        "password" : "mayapayo",
     },
    "mayica" : {
        "username" : "mayica",
        "fullname" : "Maya Mayez",
        "email" : "maphergame@game.es",
        "disable" : False,
        "password" : "juanpayo",
    },
    "mayica3":  {
        "username" : "mayica3",
        "fullname" : "Maya Mayez",
        "email" : "maphergame@game.es",
        "disable" : False,
        "password" : "juanpayo"
  }
}

@router.post("/register",status_code=201 )
def register(user: UserDB):
    if user.username not in users_db:
        hashed_password = password_hash.hash(user.password)
        user.password = hashed_password
        users_db[user.username] = user
        return user
    else:
        raise HTTPException (status_code = 409, detail = "User already exists")
    
@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    username = users_db.get(form.username)
    if username:
        #Si el usuario eiste en la base de datos
        #comprobamos las contraseñas
        if password_hash.verify(form.password,username["password"]):
            expire = datetime.now(datetime.timezone.utc)+datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
            access_token = {"sub":form.username, "exp":expire}
            token = jwt.encode(access_token,SECRET_KEY,algorithm=ALGORITHIM)
            return{"access_token":token, "token_type":"bearer"}
    raise HTTPException (status_code=401, detail="Usuario o contraseña incorrectos")

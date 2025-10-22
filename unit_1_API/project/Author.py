from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Author (BaseModel):
    id: int  
    dni: str
    name: str 
    surname: str 

authors_list = [
    Author(id=1, dni="50481240X", name="Juan", surname="Caro"),
    Author(id=2, dni="12345678A", name="Maria", surname="Gomez"),
    Author(id=3, dni="98765432B", name="Pedro", surname="Lopez"),
]




@app.get ("/Author/{id}")
def getAuthors_List(id:int):
    Author = [Author for Author in authors_list if Author.id == id]

    if len(Author) != 0:
        return Author[0]
    else:
        raise HTTPException (status_code = 404, detail="Author not found")
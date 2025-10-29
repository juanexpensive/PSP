
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional

# Router con prefijo plural
router = APIRouter(prefix="/films", tags=["films"])

# --- MODELO Y DATOS ---
class Film(BaseModel):
    id: Optional[int] = None
    title: str
    duration: int
    idDirector: int 

films_list = [
    Film(id=10, title="El Padrino", duration=175, idDirector=5),
    Film(id=25, title="Cadena Perpetua", duration=142, idDirector=1),
    Film(id=40, title="Pulp Fiction", duration=154, idDirector=12),
    Film(id=55, title="Interestelar", duration=169, idDirector=2),
    Film(id=70, title="Parásitos", duration=132, idDirector=8),
    Film(id=99, title="Matrix", duration=136, idDirector=100)
]

@router.get("/")
def film():
    return films_list

@router.get("/{id}")
def film (id:int):
    films = [film for film in films_list if film.id == id]

    if len(films) != 0:
        return films [0]
    raise HTTPException(status_code=404,detail="film not found")

def search_film (id:int):
    films = [film for film in films_list if film.id == id]

    if len(films) != 0:
        return films[0]
    else:
        return {"error" : "No film found"}
    
def next_id():
    return (max(films_list,key=id).id+1)
    
@router.post ("/films",status_code=201,response_model=film)
def add_film (film: film):
    film.id = next_id()
    films_list.append(film)
    return film

@router.put("/films/{id}",response_model=film)
def modify_film (id: int, film: film):
    for index, saved_film in enumerate (films_list):
        if saved_film.id == id:
            film.id = id
            films_list[index] = film
            return film
        raise HTTPException(status_code=404, detail="film not found")
    
@router.delete("/films/{id}")
def delete_film (id:int):
    for saved_film in films_list:
        if saved_film.id == id:
            films_list.remove(saved_film)
            return {}
        raise HTTPException(status_code=404, detail="film not found")
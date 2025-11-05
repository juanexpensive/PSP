
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional

# Router con prefijo plural
router = APIRouter(prefix="/directors", tags=["directors"])

# --- MODELO Y DATOS ---
class Director(BaseModel):
    id: Optional[int] = None
    dni: str
    name: str 
    surname: str 
    nationality: str

directors_list = [
    Director(id=1, dni="12345678A", name="Pedro", surname="Almodóvar", nationality="Española"),
    Director(id=None, dni="P9876543Z", name="Chloé", surname="Zhao", nationality="China"),
    Director(id=105, dni="G4567890B", name="Greta", surname="Gerwig", nationality="Estadounidense"),
    Director(id=200, dni="L1122334F", name="Lana", surname="Wachowski", nationality="Estadounidense"),
    Director(id=None, dni="K6789012R", name="Kiyoshi", surname="Kurosawa", nationality="Japonesa")
]
def search_director_exists(id: int, director_list: list[Director]) -> bool:
    """Verifica si un director existe en la lista dada."""
    return any(d.id == id for d in director_list)
    
def next_id() -> int:
    """Calcula el siguiente ID disponible para un nuevo director."""
    return max(directors_list, key=lambda director: director.id).id + 1 if directors_list else 1

# 1. READ ALL (GET)
@router.get("/")
def get_directors():
    return directors_list

# 2. READ ONE (GET by ID)
@router.get("/{id}", response_model=Director) 
def get_director(id: int):
    directors = [director for director in directors_list if director.id == id]

    if directors:
        return directors[0]
    raise HTTPException(status_code=404, detail="Director not found")

# 3. CREATE (POST)
@router.post("/", status_code=201, response_model=Director) 
def add_director(director: Director):
    director.id = next_id()
    directors_list.append(director)
    return director

# 4. UPDATE (PUT)
@router.put("/{id}", response_model=Director)
def modify_director(id: int, director: Director):
    for index, saved_director in enumerate(directors_list):
        if saved_director.id == id:
            director.id = id
            directors_list[index] = director
            return director
    raise HTTPException(status_code=404, detail="Director not found")
    
# 5. DELETE (DELETE)
@router.delete("/{id}", status_code=200)
def delete_director(id: int):
    for saved_director in directors_list:
        if saved_director.id == id:
            directors_list.remove(saved_director)
            return {}
        raise HTTPException(status_code=404, detail="Director not found")
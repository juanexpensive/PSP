
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

@router.get("/")
def director():
    return directors_list

@router.get("/directors/{id}")
def director (id:int):
    directors = [director for director in directors_list if director.id == id]

    if len(directors) != 0:
        return directors [0]
    raise HTTPException(status_code=404,detail="Director not found")

def search_director (id:int):
    directors = [director for director in directors_list if director.id == id]

    if len(directors) != 0:
        return directors[0]
    else:
        return {"error" : "No director found"}
    
def next_id():
    return (max(directors_list,key=id).id+1)
    
@router.post ("/directors",status_code=201,response_model=Director)
def add_director (director: Director):
    director.id = next_id()
    directors_list.append(director)
    return director

@router.put("/directors/{id}",response_model=Director)
def modify_director (id: int, director: Director):
    for index, saved_director in enumerate (directors_list):
        if saved_director.id == id:
            director.id = id
            directors_list[index] = director
            return director
        raise HTTPException(status_code=404, detail="Director not found")
    
@router.delete("/directors/{id}")
def delete_director (id:int):
    for saved_director in directors_list:
        if saved_director.id == id:
            directors_list.remove(saved_director)
            return {}
        raise HTTPException(status_code=404, detail="Director not found")
    


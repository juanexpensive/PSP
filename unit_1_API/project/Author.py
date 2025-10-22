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

def next_id():
    return (max(authors_list,key=id).id+1)

@app.get ("/Author/{id}")
def getAuthors_List(id:int):
    Author = [Author for Author in authors_list if Author.id == id]

    if len(Author) != 0:
        return Author[0]
    
    raise HTTPException (status_code = 404, detail="Author not found")
    
@app.post ("/Author", status_code=201, response_model=Author)
def add_author(author: Author):
    author.id = next_id()
    authors_list.append(author)
    return author

@app.put ("/Author/{id}", response_model=Author)
def modify_author(id: int, author: Author):
    for index, saved_author in enumerate(authors_list):
        if saved_author.id == id:
            author.id = id
            authors_list[index] = author
            return author
        raise HTTPException(status_code=404, detail = "User not found")
    
@app.delete("/Author/{id}")
def delete_author (id:int):
    for saved_author in authors_list:
        if saved_author.id == id:
            authors_list.remove(saved_author)
            return {}
        raise HTTPException (status_code=404, detail="User not found")
    

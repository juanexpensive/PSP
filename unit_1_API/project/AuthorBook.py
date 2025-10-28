from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
app = FastAPI()

class Author(BaseModel):
    id: Optional[int] = None
    dni: str
    name: str 
    surname: str 

authors_list = [
    Author(id=1, dni="50481240X", name="Juan", surname="Caro"),
    Author(id=2, dni="12345678A", name="Maria", surname="Gomez"),
    Author(id=3, dni="98765432B", name="Pedro", surname="Lopez"),
]

def next_id():
    if not authors_list:
        return 1
    return max(authors_list, key=lambda author: author.id).id + 1

@app.get("/Author/{id}")
def getAuthors_List(id: int):
    author = [a for a in authors_list if a.id == id]
    if len(author) != 0:
        return author[0]
    raise HTTPException(status_code=404, detail="Author not found")
    
@app.post("/Author", status_code=201, response_model=Author)
def add_author(author: Author):
    author.id = next_id()
    authors_list.append(author)
    return author

@app.put("/Author/{id}", response_model=Author)
def modify_author(id: int, author: Author):
    for index, saved_author in enumerate(authors_list):
        if saved_author.id == id:
            author.id = id
            authors_list[index] = author
            return author
    raise HTTPException(status_code=404, detail="User not found")
    
@app.delete("/Author/{id}")
def delete_author(id: int):
    for saved_author in authors_list:
        if saved_author.id == id:
            authors_list.remove(saved_author)
            return {}
    raise HTTPException(status_code=404, detail="User not found")
    
class Book(BaseModel):
    id: Optional[int] = None
    isbn: str 
    title: str 
    pages: int 
    author_id: int 

books_list = [
    Book(id=1, isbn="978-3-16-148410-0", title="Cien años de soledad", pages=417, author_id=1),
    Book(id=2, isbn="978-0-7432-7356-5", title="El Gran Gatsby", pages=180, author_id=2),
    Book(id=3, isbn="978-0-06-112008-4", title="Matar a un ruiseñor", pages=281, author_id=1), 
]

def next_book_id():
    if not books_list:
        return 1
    return max(books_list, key=lambda book: book.id).id + 1

@app.get("/Book/{id}", response_model=Book)
def get_book(id: int):
    book = next((b for b in books_list if b.id == id), None)
    if book:
        return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.post("/Book", status_code=201, response_model=Book)
def add_book(book: Book):
    author_exists = any(a.id == book.author_id for a in authors_list)
    if not author_exists:
         raise HTTPException(status_code=400, detail="Author ID not found")
    
    book.id = next_book_id()
    books_list.append(book)
    return book

@app.put("/Book/{id}", response_model=Book)
def modify_book(id: int, book: Book):
    author_exists = any(a.id == book.author_id for a in authors_list)
    if not author_exists:
         raise HTTPException(status_code=400, detail="Author ID not found")
    for index, saved_book in enumerate(books_list):
        if saved_book.id == id:
            book.id = id
            books_list[index] = book
            return book
    raise HTTPException(status_code=404, detail="Book not found")
    
@app.delete("/Book/{id}")
def delete_book(id: int):
    for index, saved_book in enumerate(books_list):
        if saved_book.id == id:
            books_list.pop(index)
            return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=404, detail="Book not found")
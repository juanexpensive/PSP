from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Book (BaseModel):
    id: int  
    isbn: str
    npages: int 
    author_id: int 

book_list = [
    Book(id=1, isbn="978-84-339-6616-2", npages=420, ),
    Book(id=2, isbn="978-84-9989-980-6", npages=666, ),
    Book(id=3, isbn="978-607-31-8979-3", npages=500, ),
]

def next_id():
    return (max(book_list,key=id).id+1)

@app.get ("/Book/{id}")
def getBook_list(id:int):
    Book = [Book for Book in book_list if Book.id == id]

    if len(Book) != 0:
        return Book[0]
    
    raise HTTPException (status_code = 404, detail="Book not found")
    
@app.post ("/Book", status_code=201, response_model=Book)
def add_book(book: Book):
    Book.id = next_id()
    book_list.append(book)
    return book

@app.put ("/Book/{id}", response_model=Book)
def modify_book(id: int, book: Book):
    for index, saved_book in enumerate(book_list):
        if saved_book.id == id:
            book.id = id
            book_list[index] = book
            return book
        raise HTTPException(status_code=404, detail = "Book not found")
    
@app.delete("/Book/{id}")
def delete_book (id:int):
    for saved_book in book_list:
        if saved_book.id == id:
            book_list.remove(saved_book)
            return {}
        raise HTTPException (status_code=404, detail="Book not found")
    

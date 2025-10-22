from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Book (BaseModel):
    id: int  
    isbn: int
    npages: int 
 

book_list = [
    Book(id=1, isbn= 9788433966162, npages=420,  ),
    Book(id=2, isbn= 9788499899806, npages=666,  ),
    Book(id=3, isbn= 9786073189793, npages=500,  ),
    Book(id=1, isbn= 9788433966162, npages=420, ) , 
    Book(id=2, isbn= 9788499899806, npages=666, ), 
    Book(id=3, isbn= 9786073189793, npages=500, ), 
    Book(id=4, isbn= 9780061120084, npages=208, ), 
    Book(id=5, isbn= 9780743273565, npages=300, ), 
    Book(id=6, isbn= 9788437604947, npages=150, ), 
    Book(id=7, isbn= 9780345339683, npages=900, ), 
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
    book.id = next_id()
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
    

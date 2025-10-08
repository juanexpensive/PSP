"""
Crea una clase llamada Libro que guarde la información de cada uno de los libros de una biblioteca. 
La clase debe guardar el título del libro, autor, número de ejemplares del libro y número de ejemplares prestados.
La clase contendrá los siguientes métodos:
Constructor con todos los parámetros (se le indica valores para todos los atributos).
prestamo(): incrementa el atributo correspondiente cada vez que se realice un préstamo. 
No se pueden prestar libros si no quedan ejemplares disponibles para prestar. 
Devuelve true si se ha podido realizar el préstamo y false en caso contrario.
devolucion(): decrementa el atributo correspondiente cada vez que se devuelva un libro. 
No se podrán devolver libros que no se hayan prestado. 
Devuelve true si se ha podido realizar la operación y false en caso contrario.
Crear también los métodos __str__, __eq__ y __lt__. 
Se considera que dos  libros son iguales si tienen el mismo título y el mismo autor. 
Los libros se ordenarán de menor a mayor por el nombre del autor.

"""

class Libro:
    def __init__(self, title, author, total_books, lent_books):
        self.title = title
        self.author = author
        self.total_books = total_books
        self.lent_books = lent_books
    
    def lend (self):
        if self.lent_books < self.total_books:
            self.lent_books +1
            return True
        else:
            return False
    
    def devolution (self):
        if self.lent_books < self.total_books:
            self.lent_books -1
            return True
        else:
            return False
    
    def __str__(self):
        return f"Title: {self.title} Author: {self.author} Total books: {self.total_books} Lent books: {self.lent_books}"
    
    def __eq__(self, other):
        other = False
        if self.author == other.author and self.title == other.title:
            return True
        else:
            return False
        
    def __lt__ (self, other):
        order = False
        if self.author < other.author:
            order = True
            return order
        else:
            return order
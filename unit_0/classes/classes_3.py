"""
Crea una clase llamada Punto que representará un punto de dos dimensiones en un plano. 
Solo contendrá dos atributos enteros llamados x e y (coordenadas). 
Debe tener los siguientes métodos:
Un constructor con parámetros que copie las coordenadas pasadas como argumento a los atributos del objeto.
__str__(): Devuelve una cadena con el formato “(x, y)”. Ejemplo: “(7, -5)”
setXY(x,y): Modifica ambas coordenadas.
desplaza(dx, dy): Desplaza el punto la cantidad (dx,dy) indicada. 
Ejemplo: Si el punto (1,1) se desplaza (2,5) entonces estará en (3,6).
distancia(punto): 
Calcula y devuelve la distancia entre el propio objeto (self) y otro objeto (punto) que se pasa como parámetro (distancia entre dos coordenadas).
"""

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"
    
    def setXY (x,y):
        x = input()
        y = input()
    
    def move(dx,dy):
        return x + dx and y + dy
    
    def distance (punto):
        return x - dx and y - dx


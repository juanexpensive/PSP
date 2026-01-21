#Realiza el ejercicio anterior pero esta vez va a haber otra función que lea los números de un fichero. 
#En el fichero habrá un número por línea. En este caso, tienes que llevar a cabo una comunicación entre los dos procesos utilizando colas (Queue), 
#de forma que la función que se encarga de leer los números los guarde en la cola, y la función que realiza la suma, recibirá la cola y tomará de ahí los números. 
#La función que lee el fichero, una vez haya terminado de leer y de añadir elementos a la cola,
# debe añadir un objeto None para que el receptor sepa cuándo terminar de leer de la cola.
from multiprocessing import Process, Queue

def leer(cola):
    fichero =  open("Ejercicio3.txt")
    for linea in fichero:
        numero = int(linea.strip())
        cola.put(numero)
    cola.put(None)

def suma(cola, resultado_cola):
    total = 0
    item = cola.get()
    while item  is not None:
        total +=item
        item = cola.get()
    resultado_cola.put(total)
    


def main():
    cola = Queue()


    p1 = Process(target=leer, args=(cola,))
    p2 = Process(target=suma, args=(cola,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    total = cola.get()
    print (f"Resultado es: {total}")
    print ("Se han terminado ambos procesos")

if __name__ == "__main__":
    main()
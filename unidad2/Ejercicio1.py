from multiprocessing import Process  # Importa la clase Process para crear procesos en paralelo

# Función que suma todos los números desde 1 hasta x
def suma(x):
    total = sum(range(1, x + 1))  
    print(f"Suma hasta {x}: {total}")  

if __name__ == '__main__':
    numeros = [10, 20, 50, 100]  
    procesos = []  

    # Creamos un proceso por cada número de la lista
    for n in numeros:
        p = Process(target=suma, args=(n,))  # La coma convierte (n,) en una tupla de un elemento
        procesos.append(p)  # Guardamos el proceso en la lista
        p.start()  # Iniciamos el proceso, se ejecuta suma(n) en paralelo

    # Esperamos a que todos los procesos terminen antes de continuar
    for p in procesos:
        p.join()  # join() bloquea el programa principal hasta que el proceso p termine

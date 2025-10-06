"""
Crea un programa que cree una lista de enteros de tamaño 
100 y lo rellene con valores enteros aleatorios entre 1 y 10. Luego pedirá un valor N y mostrará cuántas veces aparece N. 

"""
import random
def main():
    random_list = [random.randint(1, 10) for _ in range(100)]
    print("Generated list of random integers between 1 and 10:", random_list)

    try:
        n = int(input("Enter an integer value N between 1 and 10: "))
        if n < 1 or n > 10:
            raise ValueError("N must be between 1 and 10.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return

    count_n = random_list.count(n)
    print(f"The number {n} appears {count_n} times in the list.")

if __name__ == "__main__":
    main()
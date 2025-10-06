"""
Realiza un programa que pida 8 números enteros y 
los almacene en una lista. A continuación, recorrerá esa tabla y 
mostrará esos números junto con la palabra “par” o “impar” según proceda.

"""
def main():
    numbers = []
    for _ in range(8):
        num = int(input("Introduce un número entero: "))
        numbers.append(num)

    for n in numbers:
        if n % 2 == 0:
            print(f"{n} es par")
        else:
            print(f"{n} es impar")

if __name__ == "__main__":
    main()
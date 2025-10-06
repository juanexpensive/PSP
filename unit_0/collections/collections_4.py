"""
Escribe un programa que lea 10 números por teclado y 
que luego los muestre ordenados de mayor a menor.
"""
def main():
    numbers = []
    for _ in range(10):
        num = float(input("Input a number: "))
        numbers.append(num)

    numbers.sort(reverse=True)
    print("Numbers sorted from highest to lowest:")
    for n in numbers:
        print(n)

if __name__ == "__main__":
    main()
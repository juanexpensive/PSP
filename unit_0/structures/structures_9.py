def mostrar_rango(inicio, fin):
    # Si inicio es mayor que fin, intercambiamos
    if inicio > fin:
        inicio, fin = fin, inicio
    
    print(f"Números entre {inicio} y {fin}:")
    for i in range(inicio + 1, fin):
        print(i, end=" ")
    print()  # salto de línea


def main():
    try:
        n1 = int(input("Introduce el primer número entero: "))
        n2 = int(input("Introduce el segundo número entero: "))
        mostrar_rango(n1, n2)
    except ValueError:
        print("❌ Debes introducir solo números enteros.")


if __name__ == "__main__":
    main()

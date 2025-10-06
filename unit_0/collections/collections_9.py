"""
Crea un diccionario donde las claves son las letras del abecedario y los valores,
 la puntuación para cada letra, como en el Scrabble. El programa le pedirá una palabra al usuario y se
   mostrará por pantalla la puntuación que tiene la palabra en total.

"""
def main():
    # Crear el diccionario de puntuaciones
    score = {
        'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8,
        'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1,
        'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
    }

    word = input("Introduce una palabra: ").lower()
    total_score = sum(score.get(letter, 0) for letter in word)

    print(f"La puntuación total de la palabra '{word}' es: {total_score}")

if __name__ == "__main__":
    main()

def main():
    # Crear el diccionario de sustitución
    sustitution = {
        'e': 'p', 'i': 'v', 'k': 'i', 'm': 'u', 'p': 'm',
        'q': 't', 'r': 'e', 's': 'r', 't': 'k', 'u': 'q',
        'v': 's'
    }

    phrase = input("Input a phrase: ").lower()
    crypted_phrase = ''.join(sustitution.get(letter, letter) for letter in phrase)

    print(f"crypted phrase: {crypted_phrase}")

if __name__ == "__main__":
    main()

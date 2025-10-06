"""
Crear una función que devuelva un tipo booleano 
que indique si el carácter que se pasa como parámetro de entrada corresponde con una vocal

"""
def is_vowel(character):
    return character.lower() in "aeiou"
def main():
    char = input("Input a character: ")
    if len(char) != 1:
        print("Please enter a single character.")
    else:
        if is_vowel(char):
            print(f"'{char}' is a vowel.")
        else:
            print(f"'{char}' is not a vowel.")

if __name__ == "__main__":
    main()  
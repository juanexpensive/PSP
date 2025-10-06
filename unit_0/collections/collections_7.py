"""
Crea un programa que permita al usuario agregar, eliminar y buscar contactos en una libreta de 
direcciones implementada como un diccionario. La clave del diccionario será el nombre del contacto
 y el valor, su número de teléfono. Crea un menú para las distintas opciones e implementa una función para cada opción.
"""
def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    contacts[name] = phone
    print(f"Contact '{name}' added.")
def delete_contact(contacts):
    name = input("Enter contact name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted.")
    else:
        print(f"Contact '{name}' not found.")
def search_contact(contacts):
    name = input("Enter contact name to search: ")
    if name in contacts:
        print(f"Contact '{name}': {contacts[name]}")
    else:
        print(f"Contact '{name}' not found.")   
def main():
    contacts = {}
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Search Contact")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            delete_contact(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")  
if __name__ == "__main__":
    main()
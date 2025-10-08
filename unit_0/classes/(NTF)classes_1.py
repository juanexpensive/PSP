"""
Diseñar la clase CuentaCorriente, que almacena los datos DNI, nombre y el saldo. 
Añade los siguientes constructores:
Con el DNI del titular de la cuenta y un saldo inicial. El nombre se inicializará a cadena vacía.
Con el DNI, nombre y el saldo inicial.
Las operaciones típicas de una cuenta corriente son:
Sacar dinero: el método debe indicar si ha sido posible llevar a cabo la operación, 
si existe saldo suficiente. Si es posible llevar a cabo la operación se resta la cantidad a sacar al saldo de la cuenta.
Ingresar dinero: se incrementa el saldo.
Crear también los métodos __str__, __eq__ y __lt__. 
Se considera que dos cuentas corrientes son iguales si tienen el mismo DNI. 
Las cuentas corrientes se ordenarán de menor a mayor por el saldo.
"""

class CuentaCorriente:
    def __init__(self, DNI, name, balance): 
        self.DNI = DNI
        self.name = name
        self.balance = balance

    def __init__(self, DNI, name, balance): 
        self.DNI = DNI
        self.name = " "
        self.balance = balance

    def withdraw (self):
        money_withdraw = int(input("How much would you like to withdraw:"))
        if money_withdraw < 1:
            print (f"You dont have enough, your current balance is: {self.balance}")
        elif money_withdraw >= 1:
            self.balance - money_withdraw
            print (f"Your current balance is now: {self.balance}")

    def deposit (self):
        money_deposit = int(input("How much would you like to deposit:"))
        self.balance + money_deposit
        print (f"Your current balance is: {self.balance}")

    def __str__(self):
        return f"Account name:  {self.name} DNI: {self.DNI} Balance: {self.balance}"
    
    def __eq__(self, other):
        if self.DNI == other.DNI:
            print("They have the same DNI")
        else:
            print("They dotn have the same DNI")

    def __lt__ (self, other):
        if self.balance < other.balance:
            print (f"{other.balance}, {self.balance}")
        else:
            print (f"{self.balance}, {other.balance}")

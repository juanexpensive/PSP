"""
Diseñar la función calculadora(), a la que se le pasan dos números reales (operandos) 
y qué operación se desea realizar con ellos. Las operaciones disponibles son sumar, restar, multiplicar o dividir. Estas se especifican mediante un número: 1 para la suma, 2 para la resta, 3 para la multiplicación y 4 para la división.
 La función devolverá el resultado de la operación mediante un número real
"""

def calculator(operand1, operand2, operation):
    if operation == 1:
        return operand1 + operand2
    elif operation == 2:
        return operand1 - operand2
    elif operation == 3:
        return operand1 * operand2
    elif operation == 4:
        if operand2 != 0:
            return operand1 / operand2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"

def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    operation = int(input("Enter operation (1/2/3/4): "))
    result = calculator(num1, num2, operation)
    print(f"The result is: {result}")

if __name__ == "__main__":
    main()
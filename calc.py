def get_user_input():
    try:
        num1 = float(input("Ingrese un numero: "))
        num2 = float(input("Ingrese otro numero: "))
        operation = input("Elija una operacion (+, -, *, /) o escriba 'exit' para salir: ")
        return num1, num2, operation
    except ValueError:
        print("Input invalido. Por favor ingrese numeros.")
        return get_user_input()

def ejecutar_operacion(user_input, callback):
    num1, num2, operation = user_input
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else "Division by zero error"
    }
    result = operations.get(operation, lambda x, y: "Operacion invalida")(num1, num2)
    print("Resultado:", result)

def main():
    operations = {'+','-','*','/'}
    while True:
        user_input = get_user_input()

        if user_input[2].lower() == 'exit':
            print("Salir.")
            break

        print("\nCalculando...\n")

        if user_input[2] in ['+', '-', '*', '/']:
            ejecutar_operacion(user_input, operations[user_input[2]])
        else:
            print("Operacion invalida. Seleccione (+, -, *, /) o escriba 'exit' para salir.")

if __name__ == "__main__":
    main()

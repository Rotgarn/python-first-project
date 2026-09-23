def listar(num1): #Funcion para listar números del 1 al número ingresado por el usuario

    num1 = int(input("Ingrese un número: "))

    for i in range(1, num1 + 1):
        print(i)
    return num1

def suma(num1, num2): #Funcion para sumar dos números

    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    resultado = num1 + num2
    print(f"Tu resultado es: {resultado}")

    return resultado

def resta(num1, num2): #Funcion para restar dos números

    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    resultado = num1 - num2
    print(f"Tu resultado es: {resultado}")

    return resultado

def multi(num1, num2): #Funcion para multiplicar dos números

    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    resultado = num1 * num2
    print(f"Tu resultado es: {resultado}")

    return resultado

def div(num1, num2): #Funcion para dividir dos números

    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    if num2 == 0:
        print("Error: No se puede dividir entre cero.")
        return None

    resultado = num1 / num2
    print(f"Tu resultado es: {resultado}")

    return resultado

menu = 0

while menu != 7: #Bucle para mostrar el menú hasta que el usuario decida salir
    num1 = 0
    num2 = 0
    print("Seleccione una opción:")
    try: #Try para manejar errores de entrada del usuario
        menu = int(input("1. Saludar\n2. Listar números\n3. Sumar dos números\n4. Restar dos números\n5. Multiplicar dos números\n6. Dividir dos números\n7. Salir\n"))
    except ValueError: # Manejo de error si el usuario ingresa un valor no numérico
        print("Opción no válida. Por favor, seleccione una opción del 1 al 7.")
        continue
    if int(menu) == 1:
        nombre = input("Ingrese su nombre: ")
        print(f"Hola, {nombre}!")
    elif int(menu) == 2:
        listar(num1)
    elif int(menu) == 3:
        suma(num1, num2)
    elif int(menu) == 4:
        resta(num1, num2)
    elif int(menu) == 5:
        multi(num1, num2)
    elif int(menu) == 6:
        div(num1, num2)
    elif int(menu) == 7:
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 7.") # Manejo de error si el usuario ingresa un número fuera del rango permitido

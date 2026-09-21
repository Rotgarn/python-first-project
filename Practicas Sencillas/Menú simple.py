opcion = "0"
saludo = "1"
mensaje = "2"
contar = "3"
salir = "4"

while opcion != salir:

    print("Seleccione una opción:")
    print("1. Saludar")
    print("2. Escribe un Mensaje")
    print("3. Contar hasta un número")
    print("4. Salir")

    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == saludo:
        print("¡Hola! ¿Cómo estás?")
    elif opcion == mensaje:
        mensaje_usuario = input("Escribe tu mensaje: ")
        print(f"Tu mensaje es: {mensaje_usuario}")
    elif opcion == contar:
        limite = int(input("Ingrese el número hasta el cual contar: "))
        for i in range(1, limite + 1):
            print(i)
    elif opcion == salir:
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")
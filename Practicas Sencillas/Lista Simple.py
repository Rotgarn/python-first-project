#print("Lista de videojuegos:")
#print(videojuegos[0])
#print(videojuegos[4])
#print(videojuegos)

#videojuegos.append("Among Us")
#print("Lista actualizada de videojuegos:")
#print(videojuegos)

#for juego in videojuegos:
#    print(juego)


videojuegos = []
personajes = []

for vnum in range(int(input("Ingrese la cantidad de videojuegos: "))): # Inicializa un bucle que se repetirá según la cantidad de videojuegos que el usuario desee ingresar
    videojuego = input("Ingrese el nombre del videojuego: ")
    videojuegos.append(videojuego)

print("Lista de videojuegos:")
for juego in videojuegos:
    print(juego)  # Imprime cada videojuego en la lista


for pnum in range(int(input("Ingrese la cantidad de personajes: "))): # Inicializa un bucle que se repetirá según la cantidad de personajes que el usuario desee ingresar

    print("Ingrese los datos del personaje:")

    nombre = input("Ingrese el nombre del personaje: ")
    if nombre == "":
        print("Error: El nombre del personaje no puede estar vacío.")
        continue
    nivel = int(input("Ingrese el nivel del personaje: "))
    if int(nivel) < 1:
        print("Error: El nivel del personaje debe ser al menos 1.")
        continue
    clase = input("Ingrese la clase del personaje: ")
    if clase == "":
        print("Error: La clase del personaje no puede estar vacía.")
        continue
    videojuego_asociado = input("Ingrese el nombre del videojuego al que pertenece el personaje: ")
    if videojuego_asociado == "":
        print("Error: El nombre del videojuego asociado no puede estar vacío.")
        continue
    arma = input("Ingrese el arma del personaje: ")
    if arma == "":
        print("Error: El nombre del arma no puede estar vacío.")
        continue

    personaje = {
        "nombre": nombre,
        "nivel": nivel,
        "clase": clase,
        "videojuego_asociado": videojuego_asociado,
        "arma": arma
    }
    
    personajes.append(personaje)

print("Lista de personajes:")
for list_personaje in personajes: # Inicializa un bucle que recorre la lista de personajes y muestra sus datos
    print(f"Nombre: {list_personaje['nombre']}, Nivel: {list_personaje['nivel']}, Clase: {list_personaje['clase']}, Videojuego: {list_personaje['videojuego_asociado']}, Arma: {list_personaje['arma']}")

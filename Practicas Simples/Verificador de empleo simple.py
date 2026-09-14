nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
salario = float(input("Ingrese su salario deseado: "))
experiencia = input("¿Tiene experiencia laboral en este rubro? (si/no): ").lower()
estudios = input("¿Tiene estudios relacionados con el puesto? (si/no): ").lower()

if (edad >= 18 and salario <= 25000) and (experiencia == "si" or estudios == "si"):
    print(f"Felicidades {nombre}, cumples para los requisitos de una entrevista.")
else:
    print(f"Lo siento {nombre}, por el momento no cumples con los requisitos para una entrevista.")
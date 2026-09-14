nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
salario = float(input("Ingrese su salario deseado: "))

print("Ayudanos confirmando tus datos:")
print(f"Nombre: {nombre}, Edad: {edad}, Expectativa salarial: {salario}")

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

if salario >= 30000:
    print("Tu expectativa salarial es alta.")
elif salario >= 20000:
    print("Tu expectativa salarial es media.")
else:
    print("Tu expectativa salarial es inicial.")

# tarifa_entrada.py
# Este programa calcula el costo de entrada a un parque según la edad.

edad = int(input("Escribe la edad de la persona: "))

if edad < 0:
    print("La edad no es válida.")

elif edad < 12:
    print("El costo de entrada es $50.")

elif edad < 18:
    print("El costo de entrada es $80.")

else:
    print("El costo de entrada es $120.")
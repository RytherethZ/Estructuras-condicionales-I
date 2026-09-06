# clasificacion_triangulos.py
# Este programa clasifica un triángulo según sus lados.

lado1 = float(input("Escribe la longitud del primer lado: "))
lado2 = float(input("Escribe la longitud del segundo lado: "))
lado3 = float(input("Escribe la longitud del tercer lado: "))

# Primero revisamos que los lados sean válidos
if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
    print("Los lados no son válidos.")

# Revisamos si los lados pueden formar un triángulo
elif lado1 + lado2 <= lado3 or lado1 + lado3 <= lado2 or lado2 + lado3 <= lado1:
    print("Los lados no forman un triángulo.")

# Clasificación del triángulo
elif lado1 == lado2 and lado2 == lado3:
    print("El triángulo es equilátero.")

elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("El triángulo es isósceles.")

else:
    print("El triángulo es escaleno.")
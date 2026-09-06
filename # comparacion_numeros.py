# comparacion_numeros.py
# Este programa compara tres números y muestra el mayor y el menor.

n1 = float(input("Escribe el primer número: "))
n2 = float(input("Escribe el segundo número: "))
n3 = float(input("Escribe el tercer número: "))

# Buscar el número mayor
if n1 >= n2 and n1 >= n3:
    mayor = n1
elif n2 >= n1 and n2 >= n3:
    mayor = n2
else:
    mayor = n3

# Buscar el número menor
if n1 <= n2 and n1 <= n3:
    menor = n1
elif n2 <= n1 and n2 <= n3:
    menor = n2
else:
    menor = n3

print("El número mayor es:", mayor)
print("El número menor es:", menor)
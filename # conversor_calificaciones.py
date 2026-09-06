# conversor_calificaciones.py
# Este programa convierte una calificación numérica a letra.

calificacion = float(input("Escribe una calificación entre 0 y 100: "))

if calificacion < 0 or calificacion > 100:
    print("La calificación no es válida.")

elif calificacion >= 90:
    print("La calificación equivale a A.")

elif calificacion >= 80:
    print("La calificación equivale a B.")

elif calificacion >= 70:
    print("La calificación equivale a C.")

elif calificacion >= 60:
    print("La calificación equivale a D.")

else:
    print("La calificación equivale a F.")
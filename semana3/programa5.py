""" Programa5
Nombre: Cesar Arath
Fecha: 31/01/2023
Descripción: Calcular el area y perimetro de cualquier triangulo
"""
print("Area del triangulo")
base = None #Asignacion  
altura = None
base = float(input("Base del triangulo: "))
altura = float(input("Altura del Triangulo: "))
area = base * altura / 2
print("Area del triangulo es igual a: {}".format(area))
print("Perimetro de Triangulo")
lado1 = float(input("lado1: "))
lado2 = float(input("lado2: "))
lado3 = float(input("lado3: "))
perimetro = lado1 + lado2 + lado3
print("El perimetro del triangulo es: {}".format(perimetro))
""" Programa5
Nombre: Cesar Arath
Fecha: 30/01/2023
Descripción: Calcular el area y perimetro de cualquier triangulo
"""
base = None
altura = None

while True:
  try:
    base = float(input("Base del triangulo: "))
    break
  except:
    print("Escribir un numero: ")

while True:
  try:
    altura = float(input("Altura del Triangulo: "))
    break
  except:
    print("Escribir un numero: ")

area = base * altura / 2
print("El area del triangulo es igual a: {}".format(area))

lado1 = float(input("lado1: "))
lado2 = float(input("lado2: "))
lado3 = float(input("lado3: "))
perimetro = lado1 + lado2 + lado3
print("El perimetro del triangulo es: {}".format(perimetro))
""" Programa6
Nombre: Cesar Arath
Fecha: 31/01/2023
Descripción: Area y Perimetro de un Circulo y un Cuadrado
"""
""" 
AREA Y PERIMETRO DE UN CIRCULO
"""
print("AREA Y PERIMETRO DE UN CIRCULO CUALQUIERA") # Imprimir texto
import math #  proporciona acceso a las funciones matemáticas definidas en el estándar de C
pi=math.pi #  Se asigna valor a pi con la funcion math para funciones matematicas
radio=float(input('Escribir el radio del circulo: ')) #   Se escribira el radio imprimiendolo como numero real con punto decimal etc.
area=pi*(radio**2) #  Formula para sacar el area de un circulo
per=2*radio*pi #  Formula para sacar el perimetro de un circulo
print("Area= ",area) #  Se imprimira el area de acuerdo al valor que le hayamos asignado a la medida del mismo
print("Perimetro= ",per) #  Se imprimira el perimetro de acuerdo al valor que le hayamos asignado a la medida del mismo
""" 
AREA Y PERIMETRO DE UN CUADRADO
"""
print("AREA Y PERIMETRO DE UN CUADRADO CUALQUIERA") #  Imprimir Texto
lado=float(input("Escribir la medida de un lado: "))  #  Se escribira un numero flotante sin importar que lleve punto decimal
per=lado*4 #  Formula para sacar el perimetro de un cuadrado
area=lado**2 # Formula para sacar el area de un cuadrado
print("Area= ",area) #  Se imprimira el area de acuerdo al valor que le hayamos asignado 
print("Perimetro= ",per) #  Se imprimira el perimetro de acuerdo al valor que le hayamos asignado
 
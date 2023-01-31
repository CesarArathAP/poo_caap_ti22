""" Programa6
Nombre: Cesar Arath
Fecha: 31/01/2023
Descripción: Area y Perimetro de un Circulo y un Cuadrado
"""
import math
print ("Area y Perimetro de un circulo")
r=float(input("Escribe el radio:"))
circunferencia=2*math.pi*r
area=math.pi*r*r
superficiearea=4*math.pi*r*r
print ( "Circunferencia:% .2f" % circunferencia)
print ( "Area del circulo:% .2f"% area)
print ( "Area de superficie del circulo:% .2f"% superficiearea)

""" 
Area y Perimetro de un cuadrado
"""
import os
print ("Area y Perimetro de un Cuadrado")
lado = float (input ('Ingresa el valor de lado: '))
area=lado*lado
perimetro=lado*4
print ('El area del cuadrado es: ' + repr (area))
print ('El perimetro del cuadrado es: ' + repr (perimetro))
print ()
os.system ('pause')


#el programa calculara el area de un circulo utilizando una funcion
import math
#este es el codigo de nuestra funcion
def calcular_area_circulo(radio):
    area=math.pi*radio**2
    return area

#este es el codigo del programa, primero se ejecutara este codigo:
radio=float(input('escribe el radio del circulo y calculare su area: '))
#aqui llamaremos a la funcion
areaCirculo=calcular_area_circulo(radio)
print(f'el are del circulo es: {round(areaCirculo,2)}')


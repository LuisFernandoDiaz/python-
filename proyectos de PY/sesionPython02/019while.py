#el programa pedira numeros y los ira sumando en una variable que 
#tecnicamente se conoce como acumulador

suma=0
numero=1
while(numero!=0):
    numero=int(input('Introduce el numero que desees sumar y 0 para salir: '))
    suma+=numero

print('la suma total es: ',suma)
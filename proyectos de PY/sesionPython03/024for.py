#en este programa recorelemos una lista (estructura sumilar a un array
# o arreglo unidimiensional)
import time
carro=['mazda','toyota','nisan','honda'] #lista llena
lista=[]#esta es una lista vacia

print('imprimiremos una lista de marcas autos.')

for car in carro:#car es una variable que recorre la lista carro
    time.sleep(1)
    print('el carro actual es: ', car)



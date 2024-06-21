#crearemos una funcion para determinar si un numero es par o impar

def es_par(num):
    if num%2==0:
        return True
    else:
        return False


numero=int(input('escribe un numero y determinare si es par o impar: '))

if(es_par(numero)):
    print(f'el numero {numero} es par')
else:
    print(f'el numero {numero} es impar')



#el programa valida entradas de tipo texto

while True:
    try:
        dato=input('ingresa tu nombre de usuario: ')
        nombre=int(dato)#operacion riesgo
        print('error, por favor ingresa solo texto, no numeros')
    except ValueError:
        break


print(f'usuario valido: {dato} ')

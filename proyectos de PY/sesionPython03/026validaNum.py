#este programa valida para que solo se introduzcan datos numericos

while True:
    try:
        datos=input('porfavor ingresa tu edad: ')
        edad=int(datos)
        if(edad<0) or(edad>100):
            print('edad no valida')
        else:
            break#se sale por que si encontro numero mayor que 0  
    except ValueError:#dato que no se referente a lo pedido se ejecutara esa except
        print('error al capturar, por favor, ingresa un dato numerico.')


print(f'edad valido: {edad}')
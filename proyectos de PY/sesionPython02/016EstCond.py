#el programa pedira una cantidad en sonles y mostrara un menu
#de opciones para convertir a dolar o a pesos mexicanos

soles=int(input('Escribe la cantidada en soles: '))
opcion=int(input('\n A cual moneda deseas convertir? '
                 '\n1. Dolares $4 \n'
                 '\n2. Pesos $5 \n'))

mensaje1='La cantidad convertida en dolares es: '
mensaje2='La cantidad convertida en Pesos es: '
ancho=40

if(opcion==1):
    total=soles/4
    mensaje1=mensaje1.center(ancho)
    print(mensaje1,round(total,3))
elif(opcion==2):
    total=soles/5
    mensaje2=mensaje2.center(ancho)
    print(mensaje2,round(total,3))
else:
    print('Elegiste una opcion no valida..')




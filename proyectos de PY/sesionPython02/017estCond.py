#Convertiremos de metros a kilometros y a centimetros
#segun lo solicite el usuario
distancia=float(input('Escribe la cantidad en metros '))
opcion=input('\n A que unidad quieres convertir?'
             '\n a. Convertir a Kilometros'
             '\n b. Convertir a centimetros\n')

mensaje1='Los metros convertidos a kilometros es: '
mensaje2='Los metros convertidos a centimetros es: '
ancho=40
if(opcion=='a'):
    total=distancia/1000
    mensaje1=mensaje1.center(ancho)
    print(mensaje1,total)
elif(opcion=='b'):
    total=distancia*100
    mensaje2=mensaje2.center(ancho)
    print(mensaje2,total)
else:
    print('No valido')




#el programa contiene un numero secreto, que el usuario debe adivinar
#tendra 3 oportunidades

numero_secreto=9
adivinado=False
intento=0
quedan=3

print('Solo tienes 3 intentos')
while not(adivinado) and (intento < 3): #while (adivinado==False)
    dato=int(input('adivina el numero (Es menor a 10): '))
    if(dato==numero_secreto):
        print('Felicidades has podido adivinar el numero....')
        adivinado=True
    else: #en caso que no alla adivinado
        intento+=1
        if ( intento==3): #Si los intentos llegan a 3
            print('El juego ha terminado')
        else: #en caso que todavia no sea igual a 3
            print('Por favor intentalo de nuevo...')
            quedan-=1
            print(f'te quedan {quedan} intentos')



        









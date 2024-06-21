clave='bolas'
opcion=''
oportunidad=5
intento=0
print('Mano tienes 5 intentos, no la kgues.')

while (opcion!=clave) and (intento<5):
    opcion=input('dinos la clave: ')
    intento+=1
    if(opcion==clave):
        print(f'Bien papi, intento: {intento}')
    else:
        print(f'vuelve a intentarlo, estas en el intento {intento}')
        if(intento==5):
            print(f'Eres un tarao, fallaste {intento} veces ctmr')
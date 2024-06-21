#create (agregar)   read (leer o buscar)   Update (actualizar)  delete (borrar o eliminar)
#transaccionales(puntos de ventas) -->CRM-->ERP-->BSC

import os #nos permite usar instrucciones de nuestro sistema operativo
import time
lista=[]

while True:
    print('---MENU PRINCIPAL---'
          '\n1. Insertar un Dato.'
          '\n2. Eliminar un Dato.'
          '\n3. Buscar un Dato.'
          '\n4. Sobreescribir un dato.'
          '\n5. Mostrar el contenido de la lista'
          '\n6. Salir.')
    opcion=int(input('Elige una opcion: '))
    if (opcion==1): #Create (inseertar)
        dato=input('ingresa el dato a insertar: ')
        lista.append(dato)#append (agreda lo del dato al array lista)
        print('dato insertado correctamente...')
        time.sleep(2)
        os.system('cls') #limpia la pantalla 
    elif(opcion==2):#DELETE (eliminar)
        dato=input('ingresa el dato a eliminar: ')
        if(dato in lista):
            lista.remove(dato)#saca el dato de la lista si este ya tiene una ahi
            time.sleep(2)
            os.system('cls') 
        else:
            print('el dato a eliminar no esta en la lista')
            time.sleep(2)
            os.system('cls')
    elif(opcion==3):#read (leer)
        dato=input('Ingresa el dato que buscaremos: ')
        if(dato in lista):
            print('el dato existe en la lista, esta en la posicion: '
                  ,lista.index(dato))#este hace una busqueda de la posicion
            time.sleep(4)
            os.system('cls')
        else:
            print('el dato no existe en la lista...')
            time.sleep(2)
            os.system('cls')
    elif(opcion==4):#update (modificar)
        datoAnterior=input('ingresa el dato a sobreescribir: ')
        if(datoAnterior in lista):
            indice=lista.index(datoAnterior)
            datoNuevo=input('Ingresa el dato nuevo: ')
            lista[indice]=datoNuevo #la busqueda que se hizo la remplaza por datoNuevo
            print('el dato se sobreescribio correctamente...')
            time.sleep(3)
            os.system('cls')
        else:
            print(f'EL dato {datoAnterior} no existente')
            time.sleep(3)
            os.system('cls')
    elif(opcion==5): #Mostrar 
        print('el contenido de la lista es: ')
        print(lista)
        input('presiona enter para continuar')
        time.sleep(2)
        os.system('cls')
    elif(opcion==6): #salir
        respuesta=input('Estas segur de que quieres salir? (s/n) ')
        if(respuesta.upper()=='S'):
            print('saliendo del sistema...')
            time.sleep(2)
            os.system('cls')
            break
        time.sleep(2)
        os.system('cls')
    else:
        print('opcion no valida, intenta de nuevo...')
        time.sleep(2)
        os.system('cls')








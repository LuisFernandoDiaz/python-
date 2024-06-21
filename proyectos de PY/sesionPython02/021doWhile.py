#El programa pedira numeros para promediar

contador=0
suma=0
numero=0

while True:  #mientas la verdad sea verdadera
    numero = float(input('Escribe un numero para sumarlo (ingresa 0 para salir): '))
    if (numero == 0):
        break       #sale de while
    suma += numero  #suma = suma + numero
    contador+=1     #contador = contador + 1

if(contador>0):
    promedio=suma/contador
    print(f'la suma de los numeros es: {suma}')
    print(f'el total de numeros ingresados es: {contador}')
    print(f'el promedio de los numeros ingresados es: {promedio}')
else:
    print(f'no se ingreso numeros')


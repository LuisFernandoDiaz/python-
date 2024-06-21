#el programa pedira numeros mientras los ingresados esten entre el 0 y 99

edad=0


while True:  #se repetira hasta que se aplique un break
    edad=int(input('escribe tu edad: '))
    if(edad > 0) and (edad <99):    # entra al if solo si el numero esta entre 0 y 99
        break                       # hace que salga de while
    print('edad no es valido, intenta de nuevo por favor...')

print('tu edad es: ', edad)
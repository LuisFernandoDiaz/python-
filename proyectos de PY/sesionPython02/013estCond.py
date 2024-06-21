#El promedio debe determinar si el usuario puede votar o no
nombre=input('Escribe tu nombre: ')
edad=int(input('Escribe tu edad: '))

if(edad>=18):
    print(f'Estimado {nombre}, si puedes votar')
else:
    print(f'Estimado {nombre}, no puedes votar')
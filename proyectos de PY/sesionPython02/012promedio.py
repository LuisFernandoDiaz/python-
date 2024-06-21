#el programa calcula y muestra el promedio de 3 calificaciones

print('El programa calcula el promedio de 3 calificaciones de un alumno\n')

nombre=input('escribe tu nombre alumno: ')
mat= float(input('Dime tu calificacion de Matematicas: '))
fis= float(input('Dime tu calificacion de Fisica: '))
quim= float(input('Dime tu calificacion de Quimica: '))

promedio=(mat + fis + quim)/3

print(nombre,'tu promedio es: ',round(promedio,2))
#ademas el programa debe avisar si esta aprobado o no el alumno

if(promedio < 13):
    print(nombre,'Estas desaprobado')
elif(promedio < 17):
    print(nombre,'Estas aprobado')
elif(promedio <=20):
    print(nombre,'Exelente!!')




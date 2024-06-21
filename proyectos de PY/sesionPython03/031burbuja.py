#el programa manipula una lista de numero y los ordena usando el 
#metodo de la burbuja

datos=[50,300,17,12,9,15]
print('la lista original es: \n', datos)
n=len(datos)  #de esta manera se ven cuantos datos hay en el array
print('la longitud de la estructura es: ',n)

for i in range(n-1):
    for j in range(n-1):
        print(f'i vale: {i} y j vale : {j} ')
        if(datos[j]>datos[j+1]):
            datos[j],datos[j+1]=datos[j+1],datos[j]
            print('actualmente la lista es: ',datos)

print('la lista ordenada es : ', datos)




#el programa manipula un arreglo bidimensiona, tambien llamado matriz
#o lista de listas
#crearemos la matriz

matriz=[[1,2,3],
        [4,5,6],
        [7,8,9]]
#como podemos acceder a un determinado elemento de la matriz
elemento=matriz[1][2]
print('el dato que esta en la fila 2, columna 3 es: ', elemento)

print('\nAhora recorremos todas la estuctura: ')
for fila in matriz:
    for elemento in fila:
        print(elemento, end=' ')
    print()








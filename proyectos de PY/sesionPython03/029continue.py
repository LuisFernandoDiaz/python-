#ejemplificamos el uso de continue
#el programa imprimira el valor de la variable unicamente cuando 
#esta se impar

for i in range(1,10):
    if i%2==0:
        print('impresion normal omitida por ser numero par...')
        continue
    print('la variable i, vale:',i)


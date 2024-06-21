#el programa imprimira un saludo, de forma particular

import time
print('Imprimiremos la cadena de texto ¡Hola mundo! usando el ciclo for')

for letra in "¡Hola mundo!":
    time.sleep(1)
    print(letra,end='',flush=True)#end = lo hace correr ....flush hace que aparesca 



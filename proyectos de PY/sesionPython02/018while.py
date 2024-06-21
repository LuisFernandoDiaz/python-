#Simularemos un conteo regresivo
import time

contador=int(input('Dinos el numero regresivo: '))
print('Inicia el conteo regresivo..')
while(contador>0):
    print(contador)
    time.sleep(1)
    contador -=1

if(contador==0):
    print('Es hora de chingar!!')

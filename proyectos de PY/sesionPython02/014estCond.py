#el programa evaluara la estatura del usuaio y 
#si la estatura es menor a 160csm imprimira: eres chaparrito  
#si la estatura esta entre 160-175 cms imprimira: eres de estaura mediana
#si la estattura es mayor a 175cms imprimira: eres alto


nombre=input('Dime tu nombre ')
estatura=int(input('Escribe tu altura en centimetros '))

if estatura < 160 :
    print(f'{nombre} eres chaparrito..')
elif (estatura >= 160) and (estatura <=175) :
    print(f'{nombre} eres de estatura mediana..')
elif estatura >=175 :
    print(f'{nombre} eres alto..')
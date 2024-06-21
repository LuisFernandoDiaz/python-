

def probemos(x,y):
        if(x < y):
                print(x, "es menor que", y)
        if(x > y):
                print(x, "es mayor que", y)
        else:
                print(x, "y", y, "son iguales")

probemos(25,6)

print('')

def comparando(e,a):
        if(e == a):
                print(e, "y", a, "son iguales")
        else:
                if(e < a):
                        print(e, "es menor que", a)
                else:
                        print(e, "es mayor que", a)

comparando(5,4)

"""probando 2 IF consecutivos"""
print('')
x=3
if(0 < x):
        if(x < 10):
                print("x es numero positivo de un digito")

print('')

if 0 < x and x < 10:
        print('x es un numero positivo de un digito.')

"""cuenta regresiba"""
print('')
def cuenta_atras(n):
        if(n == 0):
                print('desplegable!')
        else:
                print(n)
                cuenta_atras(n-1)

cuenta_atras(5)
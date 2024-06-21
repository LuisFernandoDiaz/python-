"""PRACTICANDO EN CASA. damos una funcion"""

def imprimiendoDoble(paso):
    print (paso, paso)

imprimiendoDoble('loco')

toyota = 'Es el pionero de los veiculos, el padrede los autos '
imprimiendoDoble(toyota)


"""practicas de doble funcion"""
def catDoble(parte1, parte2):
    cat = parte1 + parte2       
    imprimiendoDoble(cat)

parte1 = 'Chicas feas, '
parte2 = 'chicas bonitas. '

catDoble(parte1, parte2)
"""Cuando catDoble termina, la variable cat se destruye. Si trata asemos de impri
mirla, obtendriamos un error:"""

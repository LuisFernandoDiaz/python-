#buscar una subcadena dentro de una cadena de texto
mensaje='Bienvenidos al curso de Python desde Skill'
#las variables en python no son simples, son objetos con atributos y propiedades

subcadena = mensaje.find('Skill')   #find busca el numero de la posicion del texto
print('\n La subcadena buscada esta en la posicion: ', subcadena)
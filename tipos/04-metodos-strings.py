animal= '  chanCHito    feliz'
"""me devuelve los texto en mayuscula"""
print(animal.upper())
"""texto en miniscula"""
print(animal.lower())
"""primera letra en mayuscula"""
print(animal.strip().capitalize())
"""inicial de cada palabara en mayuscula"""
print(animal.title())
"""texto sin espacios alterales"""
print(animal.strip())
"""texto sin espacios, lado derecho"""
print(animal.rstrip())
"""texto sin espacios, lado izquierdo"""
print(animal.lstrip())
"""regresa la cuenta del texto indicado"""
print(animal.find("CH"))
"""remplaza el fragmento del texto"""
print(animal.replace("an","xx"))
"""busca si existe el minitexto"""
print("nCH" in animal)
"""busca si no existe el minitexto"""
print("nCH" not in animal)
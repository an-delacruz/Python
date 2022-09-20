#Implementar una función llamada ordenadaCiudades que reciba como argumento
#un diccionario con ciudades y su población y devolver una lista de las ciudades de mas de 200 mil
#habitantes, la lista devuelta debe estar ordenada de mayor a menor.
dicc = {"Nuevo Laredo":100000,"Monterrey":205000,"CDMX":300000}
def ordenarCiudades(**kargs):
    dictCiudades = {}
    for key in kargs:
        if kargs[key] > 200000:
            dictCiudades[key] = kargs[key]        
    sorted_tuples = sorted(dictCiudades.items(), key=lambda x: x[1],reverse=True)
    sorted_dict = {k: v for k, v in sorted_tuples}
    return list(sorted_dict.keys())
    
print(ordenarCiudades(**dicc))
"""Palabras
Hacer un programa que reciba como entrada una secuencia de palabras separadas por espacio en blanco
e imprima las palabras ordenadas alfanumericamente en mayusculas y después de haber eliminado
los duplicados"""

# palabras = input("Ingrese una frase: ").upper()
# #Lo mejor del Lenguaje Python es que es un lenguaje del que no te Aburres
# arrPalabras = palabras.split(" ")
# palabrasSet = set(arrPalabras)
# newList = list(palabrasSet)
# newList.sort()
# print(' '.join(newList))
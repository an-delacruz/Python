"""Mantener negativos
Escribir una función llamada ordenaPositivos que dada una lista de numeros enteros,
devuelva una nueva lista con los numeros positivos ordenados de menor a mayor y mantenga los
numeros negativos en la misma posición en la lista original
[6,3,-2,5,-8,2,-2] -> [2,3,-2,5,-8,6,-2]"""
 
lista = [6,3,-2,5,-8,2,-2]
def ordenaPositivos(lista):
    positiveList = []
    for i in lista:
        if i > 0:
            positiveList.append(i)
    positiveList.sort()
    resList = []
    for i in lista:
        if i > 0:
            resList.append(positiveList.pop(0))
        else:
            resList.append(i)
    return resList
print(ordenaPositivos(lista))
"""Mapa de caracteres
Implementar una función llamada mapaDeCaracteres que reciba como argumento una palabra y
devuelva un mapa de caracteres unico de una palabra, el mapa de caracteres es una lista
númerica en el que el número 0 se corresponde con el primer caracter de la palabra, el número 1
con el segundo caracter de la palabra y así sucesivamente.
palabra = abcd > mapa = [0,1,2,3]
aabbcb -> [0,0,1,1,2,1
zagzdaa -> [0,1,2,0,3,1,1]"""
palabra = 'zagzdaa'
def mapaDeCaracteres(palabra):
    palabraList = []
    for i in palabra:
        if i not in palabraList:
            palabraList.append(i)
    resList = []
    for i in list(palabra):
        resList.append(palabraList.index(i))
    return resList

print(mapaDeCaracteres(palabra))  
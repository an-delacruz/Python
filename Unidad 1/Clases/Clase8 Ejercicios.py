
def cadenaADiccionario(cadena):
    lstPalabras = cadena.split()
    dict = {}
    for p in lstPalabras:
        cantidad = lstPalabras.count(p)
        dict[p]=cantidad
    return dict
def palabraMasRepetida(dict):
    keyPalabra = list(dict.keys())[0]
    for x in dict.keys():
        if dict[keyPalabra] < dict[x]:
            keyPalabra = dict[x]
    newTuple = (keyPalabra, dict.get(keyPalabra))
    return newTuple
cadena = input('Ingrese una cadena: ')
dict = cadenaADiccionario(cadena)
resTupla = palabraMasRepetida(dict)
print(resTupla)

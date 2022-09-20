"""Condicionales
Una pizzería ofrece pizzas vegetarianas y no vegetarianas a sus clientes,
los ingredientes para cada tipo de pizza aparecen a continuación.
Ingredientes vegetarianos:
Pimiento
Toffu
Ingredientes no vegetarianos:
Peperoni 
Jamon 
Salmón
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no
en base a su respuesta le muestre un menú con los ingredientes disponibles,
solo se puede elegir un ingrediente, ademas del ingrediente seleccionado por defecto,
la mozarella y el tomate están en todas las pizzas, al final debe mostrar todos los
ingredientes de la pizza"""



pizzaElegida = input('Pizza vegetariana o Pizza no vegentariana (Vegetariana/No vegetariana): ')
ingredientes = ['Mozarella','Tomate']
if pizzaElegida == 'Vegetariana':
    ingredientes.append(input('Elija un ingrediente -> Pimiento o Toffu: '))
elif pizzaElegida == 'No vegetariana':
    ingredientes.append(input("Elija un ingrediente -> Peperoni, Jamón o Salmón: "))

print(f'La ingredientes de la pizza {pizzaElegida} son {", ".join(ingredientes)}')    



"""Bucles
Escribir un programa en el que se pregunte al usuario por una frase y una letra y mostrar en 
pantalla el numero de veces que se repite la letra"""

frase = input('Ingrese una frase: ')
letra = input('Ingrese una letra: ')

contador = 0
for l in frase:
    if l == letra:
        contador+=1
print(f'Número de {letra} en {frase}: {contador}')


"""Escriba un programa que almacene las matrices, haga el producto entre ellas dos y muestre
el resultado en una lista, para almacenar las matrices use tuplas anidadas y para mostrar el resultado
use listas ordenadas"""

matrizA = ((1,2,3),(4,5,6))
matrizB = ((-1,0),(0,1),(1,1))

matrizC = []
for i in range(len(matrizA)):
    matrizC.append([])
    for j in range(len(matrizB[0])):
        matrizC[i].append(0)
        for k in range(len(matrizB)):
            matrizC[i][i] += matrizA[i][k] * matrizB[k][j]

[print(tupla) for tupla in matrizC]

"""Escribir un programa que guarde en una diccionario los precios de las frutas en la
tabla, pregunte al usuario por una fruta, un número de kilos  y muestre en pantalla
el precio de ese número de kilos, si la fruta no esta en el diccionario debe mostrar un
mensaje acerca de esto
Plantano 1.35
Manzana 0.80
Pera 0.85
Naranja 0.70"""

diccionarioFrutas = {'Platano': 1.35,'Manzana':0.80, 'Pera':0.85, 'Naranja':0.70}

frutaIngresada = input('Ingrese una fruta: ')

existeLaFruta = False
frutasKeys = diccionarioFrutas.keys()
if not frutaIngresada  in frutasKeys:
    #print('La fruta ingresada no es valida')
    exit('La fruta ingresada no es valida')
numeroKilos = float(input('Ingrese el número de kilos: '))

print(f'El precio es: {diccionarioFrutas.get(frutaIngresada) * numeroKilos}')
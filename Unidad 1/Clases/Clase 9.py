#Tipos de datos

#Una juguetería tiene mucho exito, payasos y muñecas, suele ser su venta
#por correo y la empresa de logistica les cobra por por peso de paquete,
#debe calcular el peso de los payasos y muñecas que se daran en cada
#paquete a demanda, cada payaso peso 112g, cada muñeca 75g, escribir un programa
#que lea el  numero de payasos y muñecas, calcule el peso total del paquete
#que será enviado y el precio total el envio, si por cada 100g de payaso se cobra $2.50,
#y por cada 100g de muñeca $2.00


from decimal import Decimal


def calcularPeso(numPayasos:int, numMuñecas:int):
    return numPayasos * 112 + numMuñecas * 75
def calcularPrecio(numPayasos:int, numMuñecas:int):
    costoPayasos = numPayasos * 112 / 100 * 2.50
    costoMuñecas = numMuñecas * 75/100 * 2
    return costoPayasos + costoMuñecas


numPayasos = int(input("Ingrese la cantidad de payasos: "))
numMuñecas = int(input("Ingrese la cantidad de muñecas: "))

pesoTotal = calcularPeso(numPayasos,numMuñecas)
costoTotal = calcularPrecio(numPayasos,numMuñecas)

print(f"Peso total: {pesoTotal}, Costo total: {costoTotal}")



"""Escribir un programa que pregunte el nombre de un producto, su precio
y un número de unidades y muestre en la pantalla, una cadena con el nombre del producto
seguido de su precio unitario, 6 digitos enteros y dos decimales, numeros de unidades con 3 digitos
y el costo total con 8 digitos enteros y dos decimales"""

nombreProducto =input("Ingrese el nombre del producto: ")
precioUnitario = int(input("Ingrese el precio del producto: "))
numeroUnidades = float(input("Ingrese el número de unidades: "))

costoTotal = numeroUnidades * precioUnitario

cadenaRes = f"Precio Unitario: {'{0:.2f}'.format(precioUnitario)}, Numero Unidades: {precioUnitario}, Costo Total: {'{0:.2f}'}" 
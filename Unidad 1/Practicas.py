#1. Funciones con n parametros
"""Escribir un programa que contenga una función que reciba n parámetros de tipo numérico y calcule el
producto total."""


# def producto(*args):
#     total = 1
#     for numero in args:
#         total *= numero
#     return total

# print(producto(5, 6, 7, 8, 9, 10))

#2. Manejo y manipulación de elementos de una lista
"""Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen
posiciones múltiplos de 3, y muestre por pantalla la lista resultante."""
# abecedario = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# listaaux = []
# eliminarMultiplosDeTres = lambda lista: [listaaux.append(i) for i in lista if (lista.index(i) + 1) % 3 == 0]
# eliminarMultiplosDeTres(abecedario)
# for i in listaaux:
#     abecedario.remove(i)
# print(abecedario)


#3. Entrada de datos y manipulación
"""Escribir un programa que permita al usuario capturar su nombre completo e imprima su nombre de
manera inversa letra por letra"""
# nombreCompleto = input("Ingrese su nombre completo: ")
# for letra in nombreCompleto[::-1]:
#     print(letra)

# #4. Entrada de datos y estructuración
# """Revisar su retícula para escribir un programa que cree un diccionario vacío para que el usuario capture
# las materias y créditos de su semestre preferido (inferior a 8vo) al final imprimir en el formato
# “{asignatura}” tiene “{créditos}” créditos. Y la suma de todos los créditos del semestre"""
# diccionario = {}
# totalCreditos = 0
# for i in range(1, 8):
#     materia = input("Ingrese la materia: ")
#     creditos = input("Ingrese los creditos: ")
#     diccionario[materia] = creditos
# for materia, creditos in diccionario.items():
#     print(f"{materia} tiene {creditos} creditos")
#     totalCreditos += int(creditos)
# print(f"La suma de todos los creditos es: {totalCreditos}")

# #5. Manejo de información
# """Escribir una función que reciba n parámetros de llave valor e imprima la información en formato
# “{llave}”: “{Valor}”
# """
# def imprimir(**kwargs):
#     for llave, valor in kwargs.items():
#         print(f"{llave}: {valor}")
# imprimir(nombre="Antonio", apPaterno="De La Cruz",apMaterno="Rivera", edad=20)

# #6. Razonamiento y prueba de código
# """Escribir un programa que reciba un numero entre 0 y 20 e imprimir el numero en letra, no utilizar
# condicionales, máximo 5 líneas de código.
# """
# def numeroEnLetra(num):
#     numeros = ["cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez", "once", "doce", "trece", "catorce", "quince", "dieciseis", "diecisiete", "dieciocho", "diecinueve", "veinte"]
#     return numeros[num]

# #7. Formateo y conversiones
# """Escribir un programa que muestre un menú con 2 opciones la primera opción “1.- Imprimir
# YYYY/MM/DD” la segunda “2.- Imprimir MM/DD/YYYY” una vez seleccionada la opción imprimir la fecha
# del día de hoy en el formato seleccionado. """
# from datetime import date

from datetime import date


opcion = input("1.- Imprimir YYYY/MM/DD \n2.- Imprimir MM/DD/YYYY \nSeleccione una opcion: ")
if opcion == "1":
    print(f"{date.today():%Y/%m/%d}")
elif opcion == "2":
    print(f"{date.today():%m/%d/%Y}")
else:
    print("Opcion no valida")
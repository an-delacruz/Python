#Modulos

import csv
import random
from Clase11Modulo import suma

with open("sample.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        print(",".join(row))
    #reader = file.readlines()
    #file.close()
        
# numRandom = random.randint(1,100)
# while True:
#     numero = int(input("Adivine el numero entre 1 y 100: "))
#     if(numero == numRandom):
#         break;
#     elif(numero < numRandom):
#         print("El número es menor")
#     else:
#         print("El número es mayor")
        
# print(f"El número es: {numRandom}")

print(suma(2,5))

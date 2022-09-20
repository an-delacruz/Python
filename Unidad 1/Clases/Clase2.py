#Tupla es una coleccion ordenada e inmutable
tupla = (1,2,3)
tupla2 = 1,2,3

print(type(tupla))

lista = [1,2,3]
tupla3 = tuple(lista)
print(type(tupla3[0]))

for i in tupla3:
    print(i)
    
tupla4=(1,1,1,3,5)
print(tupla4.count(1))
tupla5=(7,7,7,3,5)
print(tupla5.index(5))
tupla6=(7,7,7,3,5)
print(tupla6.index(7,2))

#Listas
lista = [1,"Cadena",3.52,True,[1,2,3]]

print(lista)
# del lista[1]
# lista.remove("Cadena")
# lista.reverse()
print(lista[3:4])

for index,l in enumerate(lista):
    print(index,l)
    

l1 = [1,2,3]
l2 = [5,2,5]

for n1,n2 in zip (l1,l2):
    print(n1,n2)

for i in range(0,len(lista)):
    print(i)
    

#Listas
lista = [1,2,3,4]
lista2 = [5,6]
lista.extend(lista2)
lista.reverse()

index5 = lista.index(5)
lista.append(7)
lista.insert(index5,1)
lista.remove(5)
lista.sort()
print(lista,index5)





#Sets
newSet = set({1,2,3,4})
print(type(newSet))
for num in newSet:
    print(num)



#Ternario (No visto en clase)    
a = 3
b = 1 if a == 3 else 3
print(b)



#Metodos SET

newSet = {1,2,3,4,5}
newSet.add(7)
newSet2 = {1,2,5,7}
diffSet = newSet.difference(newSet2)
uniSet = newSet.union(newSet2)
intSet = newSet.intersection(newSet2)


#Discard -> Alternativa al remove(), no marca error sino existe.
diffSet.discard(3)


print(diffSet)
print(uniSet)
print(intSet)
print(intSet.__contains__(4))

#Diccionarios
mi_diccionario = {1:'A',2:'B',3:'C',4:'D'}
d2 = dict([('Nombre','Rocio'),('Edad',24),('Documento','09012022')])
d3 = dict(Nombre='Rocio',Edad=24,Documento='09012012')
keys = mi_diccionario.keys()
print(mi_diccionario[1])
print(keys)
print(d3.get('Nombre'))
d3['Nombre']='Antonio'
d3['Edad']='22'
print(d3)
for x in d3:
    print(d3[x])

# for x,y in d3:
#     print(x,y) 

print(list(d3.items())[0])
print(d3.values())
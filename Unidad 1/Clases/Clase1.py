
#Enteros
x=0
y=1
z=-1

print(type(x),x, id(x),type(y),y, id(y),type(z),z, id(z))

#Flotantes
x=0.0
y=3.5
z=-3.5
print(type(x),x, id(x),type(y),y, id(y),type(z),z, id(z))

#Complejos
x=5j
y=2+4j
print(type(x),x, id(x),type(y),y, id(y),type(z),z, id(z))

flotanteAEntero=2.5
enteroAFlontante=5
flotanteAComplejo=4.0

flotanteAEntero=int(flotanteAEntero)
enteroAFlontante=float(enteroAFlontante)
flotanteAComplejo=complex(flotanteAComplejo)

print(flotanteAEntero,enteroAFlontante,flotanteAComplejo)

#Boolean
x=True
y=False
print(type(x),x, id(x),type(y),y,id(y))

#Sets y diccionarios se declaran con brackets
#x={} Es un diccionario
#x={0} Es un set
#Tuplas usan parentesis ()
#Listas utilizan corchetes []

x ='a'
print(bool(x))

#Cadenas
saludo='Hola'
print(f"Saludo: {saludo}")

despedida='Adios'

print(despedida[::-1])

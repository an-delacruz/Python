#Funciones

def f(x):
    print(2*x)
    
f(1)

def suma(a,b):
    print(a+b)

suma(b=5,a=3)

def resta(a,b,c=1):
    print(a-b-c)
resta(5,4)

#lista = ['Rosa','Juan','Pedro']
def nombres(*nombres):
    for n in nombres:
        print(n)
nombres('Pedro','Rosa',1,2)

def suma(**knumeros):
    suma = 0
    for key,value in knumeros.items():
        print(key,value)
        suma+=value
    print(suma)
    
#suma(A=3,B=1,X=10)


d1={"a":1,"c":5}
suma(**d1)

def  sumaMedia(a,b,c):
    suma=a+b+c
    media=suma/3
    return suma,media

#sumaResultado, mediaResultado = sumaMedia(2,5,2)
sumaResultado = sumaMedia(2,5,2)[0]
print(sumaResultado)
#print(sumaResultado,mediaResultado)

def miFuncion(a:int,b:int) -> int:
    
    """Descripcion"""
    return a+b
res = miFuncion(5,4)
print(res)
help(miFuncion)
#print(miFuncion().__doc__)

def funcion(a,b,*args,**kargs,):
    print(a)
    print(b)
    for i in args:
        print(i)
    for key,value in kargs.items():
        print(key,value)
        
funcion(10,20,2,3,4,5,6,1,x='Hola',y='Adios')

def totalSuma(*args):
    total = 0
    for n in args:
        total+=n
    return total

nums = list(range(1,101,1))
total = totalSuma(*nums)
print(total)


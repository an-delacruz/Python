#lambda argument : expression
(lambda a,b: print(a+b))(1,2)
suma = lambda a,b: print(a+b)

suma(5,4)

# (lambda *a:print(suma(a )))(list(range(1,101,1)))

def multiplicador(n):
    return lambda a:print(a*n)

duplicador = multiplicador(2);
triplicador = multiplicador(3)
duplicador(11)
triplicador(11)
#input
x = int(input("Capture un numero: "))
print(type(x))
#trycatch
try:
    pass
except ZeroDivisionError as ErrorZero:
    print(f"Zero error {ErrorZero}")
except DeprecationWarning  as DeprecationError:
    print(f"Deprecation error {DeprecationError}")
except TypeError as TipoError:
    print(f"Type Error {TipoError}")
#Catch
except Exception as Error:
    print(f"Excepción general {Error}")
#Se ejecuta cuando no haya fallas.
else:
    pass
#Se ejecuta falle o no
finally:
    pass


#assert
"""Sirve para pruebas"""
#assert(1==2)

def suma(a,b):
    try:
        assert(type(a)== int)
        assert(type(b)== int)
        print(a+b)
        pass
    except AssertionError as AE:
        print(f"Se encontro un error: {AE}")
suma(5,"1")
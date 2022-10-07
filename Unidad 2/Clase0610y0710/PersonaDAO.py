#Create class PersonaDAO with methods insert, update, delete, select
from Persona import Persona
from cursorDelPool import CursorDelPool
from logger_base import log

class PersonaDAO:
    _SELECCIONAR = "SELECT * FROM public.persona ORDER BY id_persona"
    _INSERTAR = "INSERT INTO persona(nombre, apellido, email, edad) VALUES (%s,%s,%s,%s)"
    _ACTUALIZAR = "UPDATE persona SET nombre=%s, apellido=%s, email=%s, edad=%s WHERE id_persona=%s"
    _ELIMINAR = "DELETE FROM persona WHERE id_persona=%s"
    
    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            print(registros)
            personas = []                
            for r in registros:
                persona = Persona(r[0],r[1],r[2],r[3],r[4])
                personas.append(persona)
            return personas
    
    @classmethod
    def insertar(cls,persona):
        with CursorDelPool() as cursor:
            valores = (persona.nombre,persona.apellido,persona.email,persona.edad)
            cursor.execute(cls._INSERTAR,valores)
            registrosInsertados = cursor.rowcount
            return f"Se han insertado {registrosInsertados} registros"
    @classmethod
    def actualizar(cls,persona):
        with CursorDelPool() as cursor:
            valores = (persona.nombre,persona.apellido,persona.email,persona.edad,persona.id_persona)
            cursor.execute(cls._ACTUALIZAR,valores)
            registrosActualizados = cursor.rowcount
            return f"Se han actualizado {registrosActualizados} registros"
    @classmethod
    def eliminar (cls,persona):
        with CursorDelPool() as cursor:
            valores = (persona.id_persona,)
            cursor.execute(cls._ELIMINAR,valores)
            return f"Se han eliminado {cursor.rowcount} registros"
if __name__ == "__main__":
    #persona = Persona(id_persona=2,nombre='Antonio',apellido='De La Cruz',email='adlacruz00@gmail.com',edad=22)
    # print(PersonaDAO.actualizar(persona))
    print(PersonaDAO.seleccionar())
    # persona = Persona(nombre='Antonio',apellido='Rivera',email='p@email.com',edad=22)
    # print(PersonaDAO.insertar(persona))
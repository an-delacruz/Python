#Create class PersonaDAO with methods insert, update, delete, select
from Persona import Persona
from ConexionBD import Conexion
class PersonaDAO:
    _SELECCIONAR = "SELECT * FROM public.persona ORDER BY id_persona"
    _INSERTAR = "INSERT INTO persona(nombre, apellido, email, edad) VALUES (%s,%s,%s,%s)"
    _ACTUALIZAR = "UPDATE persona SET nombre=%s, apellido=%s, email=%s, edad=%s WHERE id_persona=%s"
    _ELIMINAR = "DELETE FROM persona WHERE id_persona=%s"
    
    @classmethod
    def seleccionar(cls):
        with Conexion.ObtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                print(registros)
                personas = []
                for r in registros:
                    persona = Persona(r[0],r[1],r[2],r[3],r[4])
                    print(persona)
                    personas.append(persona)
                return personas
    
    @classmethod
    def insertar(cls,persona):
        with Conexion.ObtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                valores = (persona.nombre,persona.apellido,persona.email,persona.edad)
                cursor.execute(cls._INSERTAR,valores)
                registrosInsertados = cursor.rowcount
                return f"Se han insertado {registrosInsertados} registros"

    def actualizar(cls,persona):
        with Conexion.ObtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                valores = (persona.id_persona,persona.nombre,persona.apellido,persona.email,persona.edad)
                cursor.execute(cls._ACTUALIZAR,valores)
                registrosActualizados = cursor.rowcount
                return f"Se han actualizado {registrosActualizados} registros"
    def eliminar (cls,idPersona):
        with Conexion.ObtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                valores = (idPersona,)
                cursor.execute(cls._ELIMINAR,valores)
                return f"Se han eliminado {cursor.rowcount} registros"
if __name__ == "__main__":
    # print(PersonaDAO.seleccionar())
    persona = Persona(id_persona=None,nombre='Antonio',apellido='Rivera',email='p@email.com',edad=22)
    print(PersonaDAO.insertar(persona))
import psycopg2 as bd
import sys
from psycopg2 import pool
from logger_base import log

class Conexion:
    _DATABASE = "test_db"
    _USERNAME = "postgres"
    _PASSWORD = "admin"
    _DBPORT = "5432"
    _HOST = "127.0.0.1"
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None
    
    _conexion = None
    _cursor = None
    
    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool= pool.SimpleConnectionPool(cls._MIN_CON,cls._MAX_CON,
                host = cls._HOST,
                user = cls._USERNAME,
                password = cls._PASSWORD,
                port = cls._DBPORT,
                database = cls._DATABASE)
                log.debug(f"Creación del pool exitosa: {cls._pool}")
                return cls._pool
            except Exception as e:
                log.error(f"Error al crear el pool: {e}")
                pass
        else:
            return cls._pool
        
    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        log.debug(f"Conexión obtenida del pool: {conexion}")
        return conexion
    @classmethod
    def liberarConexion(cls,conexion):
        cls.obtenerPool().putconn(conexion)
        log.debug(f"Conexion regresada: {conexion}")
        
if __name__ == '__main__':
    # pool = Conexion.obtenerPool()
    conexion1 = Conexion.obtenerConexion()
    conexion2 = Conexion.obtenerConexion()
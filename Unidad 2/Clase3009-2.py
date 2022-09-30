import psycopg2
from logger_base import log

conexion = psycopg2.connect(user="postgres",password="admin",
                            host="127.0.0.1",port="5432",database="Clase_DB")
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'DELETE FROM "Clientes" WHERE id_cliente = %s'
            id_Cliente = input("IDs a eliminar: ")
            valores = (tuple(id_Cliente.split(',')),)
            cursor.executemany(sentencia,valores)
            registrosEliminados = cursor.rowcount
            log.debug(f'Registros eliminados {registrosEliminados}')
except Exception as e:
    log.error(e)
    pass
finally:
    conexion.close()
    pass

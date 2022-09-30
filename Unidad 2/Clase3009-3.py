import psycopg2
from logger_base import log

conexion = psycopg2.connect(user="postgres",password="admin",
                            host="127.0.0.1",port="5432",database="Clase_DB")
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'UPDATE "Clientes" SET nombre_cliente = %s, apellido_cliente = %s, email_cliente =%s WHERE id_cliente = %s'
            valores = (
                ("Antonio","Rivera","adlacruz00@gmail.com",7),
                ("Patricio","Estrella","p@prueba.com",8),
            )
            cursor.executemany(sentencia,valores)
            registrosActualizados = cursor.rowcount
            log.debug(f'Registros actualizados {registrosActualizados}')
except Exception as e:
    log.error(e)
    pass
finally:
    conexion.close()
    pass

import psycopg2
from logger_base import log

conexion = psycopg2.connect(user="postgres",password="admin",
                            host="127.0.0.1",port="5432",database="Clase_DB")
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO "Clientes" (nombre_cliente,apellido_cliente,email_cliente) values(%s,%s,%s)'
            valores = (("Antonio","Rivera","antoniocruzrivera0216@gmail.com"),("Jose","Cabrera","prueba@example.com"),("Carlos","Santana","prueba@example.com"))
            cursor.executemany(sentencia,valores)
            #cursor.execute(sentencia,valores)
            registrosInsertados = cursor.rowcount
            log.debug(f'Registros insertados -> {registrosInsertados}')
            # sentencia = 'SELECT * FROM "Clientes" WHERE id_cliente = %s'
            # idCliente = input("Proporcione el id del cliente: ")
            # cursor.execute(sentencia,(idCliente,))
            # resultado = cursor.fetchone()
            # print(resultado)
        pass
    pass
except Exception as e:
    log.error(e)
    pass
finally:
    conexion.close()
    pass

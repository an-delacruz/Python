import psycopg2
from logger_base import log

conexion = psycopg2.connect(user="postgres",password="admin",
                            host="127.0.0.1",port="5432",database="Clase_DB")
try:
    conexion.autocommit = False
    cursor = conexion.cursor()
    nombreCliente = 'Antonio'
    apellidoCliente = 'Rivera'
    emailCliente = 'prueba2@example.com'
    cursor.execute('INSERT INTO "Clientes" (nombre_cliente,apellido_cliente,email_cliente) VALUES (%s,%s,%s);',
                   (nombreCliente,apellidoCliente,emailCliente))
    log.debug("Sentencia Insert")
    cursor.execute('SELECT * FROM "Clientes";')
    log.debug("Sentencia Select")
    print(cursor.fetchall())
    cursor.execute('UPDATE "Clientes" SET nombre_cliente=%s, apellido_cliente=%s,email_cliente=%s',("Antonio","De La Cruz","adlacruz00@gmail.com"))
    log.debug("Sentencia Update")
    cursor.execute('SELECT * FROM "Clientes";')
    log.debug("Sentencia Seelect")
    print(cursor.fetchall())
    conexion.commit()    
    pass
except Exception as e:
    conexion.rollback()
    print(e)
    pass
finally:
    cursor.close()
    conexion.close()
    pass
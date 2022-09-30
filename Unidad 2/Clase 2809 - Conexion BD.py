import psycopg2


conexion = psycopg2.connect(user="postgres",password="admin",
                            host="127.0.0.1",port="5432",database="Clase_DB")

cursor = conexion.cursor()
nombrePersona = 'Antonio'
apellidoPersona = 'De La Cruz'
emailPersona = 'prueba@example.com'
#cursor.execute('INSERT INTO "Personas" (nombre_persona,apellido_persona,email_persona) VALUES (%s,%s,%s);',(nombrePersona,apellidoPersona,emailPersona))
cursor.execute('SELECT * FROM "Personas";')
select = cursor.fetchall()
print(conexion)
print(select)
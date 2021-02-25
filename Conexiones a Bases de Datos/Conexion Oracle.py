import cx_Oracle

# class connect():

host = ''
port = 1521
user = 'blados'
passw = ''
tsname = 'XE'

try:
    dsn_tns = cx_Oracle.makedsn(host, port, tsname)
    connection = cx_Oracle.connect(user, passw, dsn_tns)
except Exception as error:
    print('Error al conectar la base de datos: ' + str(error))
else:
    print("Conexion Exitosa")
    
sql = 'select * from ciudades'



def consulta_sql(sentencia):
    cursor = connection.cursor()
    cursor.execute(sql)
    registros = cursor.fetchall()
    cursor.close()

    return registros



for index in consulta_sql(sql):
    print(index)

connection.close()


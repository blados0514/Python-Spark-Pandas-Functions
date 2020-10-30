import pyodbc

# establish a connection using the DSN you created earlier
try:
    # pyodbc.autocommit = False
    connection = pyodbc.connect("DSN=AzureDatabircks_DNS;UID=token;PWD=dapi4e918aff5d97c83fab469b2f6ac50b6c", autocommit=True)
    

    # run a SQL query using the connection you created
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM semih.filtros;")

# print the rows retrieved by the query.
    for row in cursor.fetchall():
        print(row)
except Exception as error:
    print("error al conectar con la base de datos " + str(error))


#importing all necessary libraries
import cx_Oracle

#Connecting to the database. The connect string is comprised of 'username/password@host/SID'
conn = cx_Oracle.connect('username/password@host/SID')

#Creating cursor to parse query result
cur = conn.cursor()

#Executing query (INSERT)
cur.execute("INSERT INTO y_paciente(cpf) VALUES ('12')")

#Commiting the query (Dependant on the connection variable, not the cursor)
conn.commit()

#Executing query (UPDATE)
cur.execute("UPDATE y_paciente SET cpf='12' WHERE cpf='12'")

#Commiting the query (Dependant on the connection variable, not the cursor)
conn.commit()

#Executing query (DELETE)
cur.execute("DELETE FROM y_paciente WHERE cpf='12'")

#Commiting the query (Dependant on the connection variable, not the cursor)
conn.commit()

#Executing query (SELECT)
cur.execute('SELECT * FROM W_AVALIAR')

#Retrieving data (Comes back in tuples)
for line in cur:
    print(line)

#Closing cursor
cur.close()

#Closing connection to database
conn.close()
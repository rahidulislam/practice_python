import psycopg2

connection = psycopg2.connect(
    host="localhost", user="postgres", password="raha7844", dbname="postgres"
)
if connection:
    print("Connection established")
else:
    print("Connection failed")

connection.close()

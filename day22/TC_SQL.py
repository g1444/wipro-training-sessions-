import mysql.connector

host = "localhost"     # ← THIS was wrong
user = "root"
password = "root"
database = "emp"

conn = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

cursor = conn.cursor()
print("connected to the database successfully")

query = "SELECT * FROM employees"

cursor.execute(query)
result = cursor.fetchall()

for row in result:
    print(row)

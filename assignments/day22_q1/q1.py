import mysql.connector

host="localhost"
user="root"
password="root"
database="emp"

conn=mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

cursor=conn.cursor()
print("connected to database successfully")
def fetch_high_salary(value):
    query1="SELECT *FROM employees WHERE salary > %s"


    cursor.execute(query1,(value,))
    result=cursor.fetchall()
    for row in result:
        print(row)

fetch_high_salary(50000)
def show_all():
     query="SELECT * FROM employees"
     cursor.execute(query)
     result=cursor.fetchall()
     for row in result:
         print(row)

def insert_query(values):
    query="INSERT INTO employees (id,name,department,salary) Values (%s ,%s,%s,%s)"
    
    cursor.execute(query,values)
    conn.commit()
    print("row added")



values=(105,"vishal","gaming",100000)
insert_query(values=values)
def update_salary(values):
    query="UPDATE employees SET salary= %s WHERE id=%s"

    cursor.execute(query,values)
    conn.commit()
    print("data updated")

update_salary((20000,104))
show_all()
from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017")
db=client["company_db"]
collection=db["employees"]

print("connected to mongodb")

def insert_employee(name,dept,salary):
    doc={
        "name": name,
        "department":dept,
        "salary":salary
    }

    collection.insert_one(doc)
    print("employee added")

# insert_employee("Jam","IT",75000)

def find_IT_employees():
    query={"department":"IT"}
    result=collection.find(query)
    for emp in result:
        print(emp)

find_IT_employees()

def update_salary(name,new_salary):

    collection.update_one(
        {"name":name},
        {"$set":{"salary":new_salary}}
    )
    print("salary updated")

update_salary("jam",40000)
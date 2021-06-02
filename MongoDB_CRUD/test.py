import sys
from pymongo import MongoClient
client = MongoClient('localhost:27017')
db = client.EmployeeData

# Create
def insert():
    try:
        employeeId = input('Enter Employee id :')
        employeeName = input('Enter Name :')
        employeeAge = input('Enter age :')
        employeeCountry = input('Enter Country :')
        
        db.Employees.insert_one(
            {
                "id": employeeId,
                "name":employeeName,
                "age":employeeAge,
                "country":employeeCountry
            }
        )
        print('\nInserted data successfully\n')
    
    except Exception as e:
        print(str(e))

# Read
def read():
    try:
        empCol = db.Employees.find()
        print('\n All data from EmployeeData Database \n')
        for emp in empCol:
            print(emp)

    except Exception as e:
        print(str(e))

# Update
def update():
    try:
        criteria = input('\nEnter id to update\n')
        name = input('\nEnter name to update\n')
        age = input('\nEnter age to update\n')
        country = input('\nEnter country to update\n')

        db.Employees.update_one(
            {"id": criteria},
                {
                "$set": {
                    "name":name,
                    "age":age,
                    "country":country
                        }
                }
            )
        print("\nRecords updated successfully\n")    
    
    except Exception as e:
        print(str(e))

# Delete
def delete():
    try:
        criteria = input('\nEnter employee id to delete\n')
        db.Employees.delete_many({"id":criteria})
        print('\nDeletion successful\n') 
    except Exception as e:
        print(str(e))


def main():

    while(1):
        selection = input('\nSelect 1 to insert, 2 to read, 3 to update, 4 to delete, 5 to exit\n')
    
        if (selection == '1'):
            insert()
        elif (selection == '2'):
            read()
        elif (selection == '3'):
            update()
        elif (selection == '4'):
            delete()
        elif (selection == '5'):
            sys.exit()
        else:
            print('\n INVALID SELECTION \n')

if __name__ == '__main__':
    main()
from pymongo import MongoClient

# Creating connections for communicating with Mongo DB
client = MongoClient('localhost:27017')
db = client.EmployeeData


# Function to insert data into mongo db
def insert():
    try:
        employeeid = input('Enter Employee id: ')
        employeename = input('Enter Name: ')
        employeeage = input('Enter Age: ')
        employeecountry = input('Enter Country: ')
        db.Employees.insert_one(
        {
            "id": employeeid,
            "name": employeename,
            "age": employeeage,
            "country": employeecountry 
        })

    except ImportError:
        platform_specific_module = None
        # Print Str(e)    
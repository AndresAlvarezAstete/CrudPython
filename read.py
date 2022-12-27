from pymongo import MongoClient

# Creating connections for communicating with Mongo DB
client = MongoClient('localhost:27017')
db = client.EmployeeData


# Function to read records from mongo db
def read():
    try:
        empcol = db.Employees.find()
        print('\nAll data from EmployeeData Database\n')
        for emp in empcol:
            print(emp)

    except ImportError:
        platform_specific_module = None
        # Print Str(e)    
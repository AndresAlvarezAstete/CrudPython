from pymongo import MongoClient

# Creating connections for communicating with Mongo DB
client = MongoClient('localhost:27017')
db = client.EmployeeData


# Function to delete records from mongo db
def delete():
    try:
        criteria = input('\nEnter employee id to delete:\n')
        db.Employees.delete_many({"id": criteria})
        print('\nDeletion Successfull\n')
        
    except ImportError:
        platform_specific_module = None
        # Print Str(e)    
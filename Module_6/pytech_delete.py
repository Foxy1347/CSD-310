"""Title: pytech_update.py
    Author: Shane Fox
    Date: 6/26/2021
    Description: Test program for deleting documents to the students collection."""

""" Import modules """
import pymongo
from pymongo import MongoClient

# Connection string
url = "mongodb+srv://admin:admin@cluster0.mdwlq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

# Connect to the cluster
client = MongoClient(url)

# Connect pytech database
db = client.pytech

# Find documents
docs = db.students.find({})

# Display message.
print(f"\n -- Found Documents --")
for doc in docs:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# Insert new student


# show an exit message
input("\n  End of program, press any key to exit... ")
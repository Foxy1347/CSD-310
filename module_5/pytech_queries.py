"""Title: mongodb_queries.py
    Author: Shane Fox
    Date: 6/19/2021
    Description: Test program for finding documents in a MongoDB Atlas cluster"""

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

# Find one document within the collection and display it
doc = db.students.find_one({"student_id": "1007"})
print("\n  -- DISPLAYING STUDENT TEST DOC -- ")
print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"])

# show an exit message
input("\n  End of program, press any key to exit... ")

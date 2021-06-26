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
feanor =  {
    "student_id": "1010",
    "first_name": "Feanor",
    "last_name": "Curufinwe",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "4.0",
            "start_date": "July 10, 2020",
            "end_date": "September 14, 2020",
            "courses": [
                {
                    "course_id": "CSD310",
                    "description": "Database Development and Use",
                    "instructor": "Professor Krasso",
                    "grade": "A+"
                },
                {
                    "course_id": "CSD320",
                    "description": "Programming with Java",
                    "instructor": "Professor Krasso",
                    "grade": "A+"
                }
            ]
        }
    ]
}

# insert statements with output 
print("\n  --INSERT STATEMENTS --")

feanor_student_id = db.students.insert_one(feanor).inserted_id
print(f"  Inserted student record Feanor Curufinwe into the students collection with student_id " + str(feanor['student_id']) + ".")

# Display new studnet
doc = db.students.find_one({"student_id": "1010"})
print("\n  -- DISPLAYING STUDENT TEST DOC -- ")
print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"])

# Delete new studnet
delete = db.students.delete_one({"student_id": "1010"})

# Display message.
docs = db.students.find({})
print(f"\n -- Found Documents --")
for stu in docs:
    print("  Student ID: " + stu["student_id"] + "\n  First Name: " + stu["first_name"] + "\n  Last Name: " + stu["last_name"] + "\n")

# show an exit message
input("\n  End of program, press any key to exit... ")
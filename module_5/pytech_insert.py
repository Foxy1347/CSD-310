"""Title: pytech_insert.py
    Author: Shane Fox
    Date: 6/19/2021
    Description: Test program for inserting new documents to the students collection."""

""" Import modules """
import pymongo
from pymongo import MongoClient

# Connection string
url = "mongodb+srv://admin:admin@cluster0.mdwlq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

# Connect to the cluster
client = MongoClient(url)

# Connect pytech database
db = client.pytech

""" three student documents"""
# Thorin Oakenshield's data document 
thorin = {
    "student_id": "1007",
    "first_name": "Thorin",
    "last_name": "Oakenshield",
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
# Bilbo Baggins data document 
bilbo = {
    "student_id": "1008",
    "first_name": "Bilbo",
    "last_name": "Baggins",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "3.52",
            "start_date": "July 10, 2020",
            "end_date": "September 14, 2020",
            "courses": [
                {
                    "course_id": "CSD310",
                    "description": "Database Development and Use",
                    "instructor": "Professor Krasso",
                    "grade": "B+"
                },
                {
                    "course_id": "CSD320",
                    "description": "Programming with Java",
                    "instructor": "Professor Krasso",
                    "grade": "A-"
                }
            ]
        }
    ]
}
# Frodo Baggins data document
frodo = {
    "student_id": "1009",
    "first_name": "Frodo",
    "last_name": "Baggins",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "1.5",
            "start_date": "July 10, 2020",
            "end_date": "September 14, 2020",
            "courses": [
                {
                    "course_id": "CSD310",
                    "description": "Database Development and Use",
                    "instructor": "Professor Krasso",
                    "grade": "C"
                },
                {
                    "course_id": "CSD 320",
                    "description": "Programming with Java",
                    "instructor": "Professor Krasso",
                    "grade": "B"
                }
            ]
        }
    ]
}

# get the students collection 
students = db.students


# insert statements with output 
print("\n  --INSERT STATEMENTS --")

thorin_student_id = students.insert_one(thorin).inserted_id
print(f"  Inserted student record Thorin Oakenshield into the students collection with student_id " + str(thorin['student_id']) + ".")

bilbo_student_id = students.insert_one(bilbo).inserted_id
print(f"  Inserted student record Bilbo Baggins into the students collection with student_id " + str(bilbo['student_id']) + ".")

frodo_student_id = students.insert_one(frodo).inserted_id
print(f"  Inserted student record Frodo Baggins into the students collection with student_id " + str(frodo['student_id']) + ".")

input("\n\n  End of program, press any key to exit... ")

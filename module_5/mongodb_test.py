"""Title: mongodb_test.py
    Author: Shane Fox
    Date: 6/19/2021
    Description: Test program for connecting to a
        MongoDB Atlas cluster"""

""" Import modules """
import pymongo
from pymongo import MongoClient

# Connection string
url = "mongodb+srv://admin:admin@cluster0.mdwlq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

# Connect to the cluster
client = MongoClient(url)

# Connect pytech database
db = client.pytech

# show collections
print("\n -- Pytech COllection List --")
print(db.list_collection_names())

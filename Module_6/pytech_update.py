"""Title: pytech_update.py
    Author: Shane Fox
    Date: 6/26/2021
    Description: Test program for updating documents to the students collection."""

""" Import modules """
import pymongo
from pymongo import MongoClient

# Connection string
url = "mongodb+srv://admin:admin@cluster0.mdwlq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

# Connect to the cluster
client = MongoClient(url)

# Connect pytech database
db = client.pytech

# testing push change to repository.
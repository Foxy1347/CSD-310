"""Title: pysports_update_and_delete.py
    Author: Shane Fox
    Date: 7/6/2021
    Description: Test program for joining the player and team tables"""

""" import statements """
import mysql.connector
from mysql.connector import errorcode

""" database config object """
config = {
    "user": "pysports_user",
    "password": "WanderLust#0588#",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}
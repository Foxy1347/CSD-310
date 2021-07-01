""" 
    Title: pysports_queries.py
    Author: Shane Fox
    Date: 6/30/2021
    Description: Test mysql queries through python
"""

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

""" Test connection to mysql"""
try:
    db = mysql.connector.connect(**config) # connect to the pysports database 

    cursor = db.cursor()

    # Query from team
    cursor.execute("SELECT team_id, team_name, mascot FROM team")

    # Get the results
    teams = cursor.fetchall()

    print("\n  -- DISPLAYING TEAM RECORDS --")

    # Loop through teams
    for team in teams: 
        print("Team ID: {}\n  Team Name: {}\n  Mascot: {}\n".format(team[0], team[1], team[2]))

    # Query from player
    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")

    # Get the results
    players = cursor.fetchall()

    print ("\n  -- DISPLAYING PLAYER RECORDS --")

    # Loop through players
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team ID: {}\n".format(player[0], player[1], player[2], player[3]))

    input("\n\n  Press any key to continue... ")


except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    db.close()
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

def show_players(cursor, title):
    """ method to execute an inner join on the player and team table, 
        iterate over the dataset and output the results to the terminal window.
    """

    # inner join query 
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    # get the results from the cursor object 
    players = cursor.fetchall()

    print("\n  -- {} --".format(title))
    
    # iterate over the player data set and display the results 
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

try:
    """ try/catch block for handling potential MySQL database errors """ 

    db = mysql.connector.connect(**config) # connect to the pysports database 

    #Get the cursor object
    cursor = db.cursor()

    # Insert a new player record
    cursor.execute("INSERT INTO player(first_name, last_name, team_id) VALUES('Smeagol', 'Shire Folk', 1)")

    # Commit the insert to the database 
    db.commit()

    # Show all records in the player table 
    show_players(cursor, "DISPLAYING PLAYERS AFTER INSERT")

    # Execute the update query
    cursor.execute("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol';")

    # Commit the update to the database 
    db.commit()

    # Show all records in the player table 
    show_players(cursor, "DISPLAYING PLAYERS AFTER UPDATE")

    cursor.execute("DELETE FROM player WHERE first_name = 'Gollum';")

    # Commit the delete to the database 
    db.commit()

    # Show all records in the player table 
    show_players(cursor, "DISPLAYING PLAYERS AFTER DELETE")

    input("\n\n  Press any key to continue... ")

except mysql.connector.Error as err:
    """ handle errors """ 

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    """ close the connection to MySQL """

    db.close()
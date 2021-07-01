/*
    Title: db_init.sql
    Author: Shane Fox
    Date: 6/30/2021
    Description: pysports database initialization script.
*/

-- drop test user if exists 
DROP USER IF EXISTS 'pysports_user'@'localhost';


-- create pysports_user and grant them all privileges to the pysports database 
CREATE USER 'pysports_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'WanderLust#0588#';

-- grant all privileges to the pysports database to user pysports_user on localhost 
GRANT ALL PRIVILEGES ON pysports.* TO'pysports_user'@'localhost';


-- drop tables if they are present
DROP TABLE IF EXISTS player;
DROP TABLE IF EXISTS team;


-- create the team table 
CREATE TABLE team (
    team_id     INT             NOT NULL        AUTO_INCREMENT,
    team_name   VARCHAR(75)     NOT NULL,
    mascot      VARCHAR(75)     NOT NULL,
    PRIMARY KEY(team_id)
); 

-- create the player table and set the foreign key
CREATE TABLE player (
    player_id   INT             NOT NULL        AUTO_INCREMENT,
    first_name  VARCHAR(75)     NOT NULL,
    last_name   VARCHAR(75)     NOT NULL,
    team_id     INT             NOT NULL,
    PRIMARY KEY(player_id),
    CONSTRAINT fk_team 
    FOREIGN KEY(team_id)
        REFERENCES team(team_id)
);


-- insert team records
INSERT INTO team(team_name, mascot)
    VALUES('Team Rohan', 'White Horse');

INSERT INTO team(team_name, mascot)
    VALUES('Team Gondor', 'White Tree');


-- insert player records 
INSERT INTO player(first_name, last_name, team_id) 
    VALUES('Eowyn', 'Eorl', (SELECT team_id FROM team WHERE team_name = 'Team Rohan'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Theoden', 'Eorl', (SELECT team_id FROM team WHERE team_name = 'Team Rohan'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Theodred', 'Eorl', (SELECT team_id FROM team WHERE team_name = 'Team Rohan'));

INSERT INTO player(first_name, last_name, team_id) 
    VALUES('Aragorn', 'Telcontar', (SELECT team_id FROM team WHERE team_name = 'Team Gondor'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Faramir', 'Son of Denethor.', (SELECT team_id FROM team WHERE team_name = 'Team Gondor'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Boromir', 'Son of Denethor', (SELECT team_id FROM team WHERE team_name = 'Team Gondor')); 
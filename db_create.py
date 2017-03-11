#!flask/bin/python
from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO
from app import db
import os.path
# this python file creates all the database tables that will be used by the application
# DO NOT RUN THIS FILE MORE THAN ONCE --- you only need to create the tables once!

db.drop_all()

#create the SONG table
if not db.engine.dialect.has_table(db.engine, "Song"):
	sql_str = "CREATE TABLE Song(" + \
		"Title VARCHAR NOT NULL," + \
		"Created_at INT NOT NULL," + \
		"Soundcloud_Views INT NOT NULL," + \
		"Song_Url VARCHAR NOT NULL," + \
		"Genre VARCHAR NOT NULL," + \
		"Track_type VARCHAR NOT NULL," + \
		"Duration INT NOT NULL," + \
		"Soundcloud_Favorites INT NOT NULL," + \
		"PRIMARY KEY (Song_Url));"
	db.engine.execute(sql_str)

#create the ARTIST table
if not db.engine.dialect.has_table(db.engine, "Artist"):
	sql_str = "CREATE TABLE Artist(" + \
		"Name VARCHAR NOT NULL," + \
		"Artist_Url VARCHAR NOT NULL," + \
		"Number_Followers INT NOT NULL," + \
		"PRIMARY KEY (Artist_Url));"
	db.engine.execute(sql_str)

#create the USER table
if not db.engine.dialect.has_table(db.engine, "UserTable"):
	sql_str = "CREATE TABLE UserTable(" + \
		"Username VARCHAR NOT NULL," + \
		"Password VARCHAR NOT NULL," + \
		"Email VARCHAR NOT NULL," + \
		"Artist_Url VARCHAR NOT NULL," + \
		"PRIMARY KEY (Email));"
	db.engine.execute(sql_str)

#create the BY table
if not db.engine.dialect.has_table(db.engine, "By"):
	sql_str = "CREATE TABLE By(" + \
		"Album_Name VARCHAR NOT NULL," + \
		"Artist_Url VARCHAR NOT NULL," + \
		"Song_Url VARCHAR NOT NULL);"
	db.engine.execute(sql_str)

#create the UPVOTE table
if not db.engine.dialect.has_table(db.engine, "Upvote"):
	sql_str = "CREATE TABLE Upvote(" + \
		"Email VARCHAR NOT NULL," + \
		"Song_Url VARCHAR NOT NULL);"
	db.engine.execute(sql_str)

#create the PLAYLIST table
if not db.engine.dialect.has_table(db.engine, "Playlist"):
	sql_str = "CREATE TABLE Playlist(" + \
		"Name VARCHAR NOT NULL," + \
		"Email VARCHAR NOT NULL," + \
		"Song_Url VARCHAR NOT NULL," + \
		"PRIMARY KEY (Name, Email, Song_Url));"
	db.engine.execute(sql_str)

# commit the results to keep them
# db.session.commit()
# if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
    # api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
    # api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
# else:
    # api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, api.version(SQLALCHEMY_MIGRATE_REPO))
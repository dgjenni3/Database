#!flask/bin/python
from migrate.versioning import api
#from config import SQLALCHEMY_DATABASE_URI
#from config import SQLALCHEMY_MIGRATE_REPO
from app import app, conn, m_data
import os.path
# this python file creates all the database tables that will be used by the application
# DO NOT RUN THIS FILE MORE THAN ONCE --- you only need to create the tables once!

# try to delete all the tables
m_data.drop_all()

#create the SONG table
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
conn.execute(sql_str)

#create the ARTIST table
	sql_str = "CREATE TABLE Artist(" + \
		"Name VARCHAR NOT NULL," + \
		"Artist_Url VARCHAR NOT NULL," + \
		"Number_Followers INT NOT NULL," + \
		"PRIMARY KEY (Artist_Url));"
	conn.execute(sql_str)

#create the USER table
	sql_str = "CREATE TABLE UserTable(" + \
		"Username VARCHAR NOT NULL," + \
		"Password VARCHAR NOT NULL," + \
		"Email VARCHAR NOT NULL," + \
		"Artist_Url VARCHAR NOT NULL," + \
		"PRIMARY KEY (Email));"
	conn.execute(sql_str)

#create the BY table
	sql_str = "CREATE TABLE By(" + \
		"Album_Name VARCHAR NOT NULL," + \
		"Artist_Url VARCHAR NOT NULL," + \
		"Song_Url VARCHAR NOT NULL);"
	conn.execute(sql_str)

#create the UPVOTE table
	sql_str = "CREATE TABLE Upvote(" + \
		"Email VARCHAR NOT NULL," + \
		"Song_Url VARCHAR NOT NULL);"
	conn.execute(sql_str)

#create the PLAYLIST table
	sql_str = "CREATE TABLE Playlist(" + \
		"Name VARCHAR NOT NULL," + \
		"Email VARCHAR NOT NULL," + \
		"Song_Url VARCHAR NOT NULL," + \
		"PRIMARY KEY (Name, Email, Song_Url));"
	conn.execute(sql_str)

 commit the results to keep them
 conn.commit()
# if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
    # api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
    # api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
# else:
    # api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, api.version(SQLALCHEMY_MIGRATE_REPO))
#!flask/bin/python
from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO
from app import db
import os.path
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
db.engine.execute(sql_str)

#create the ARTIST table
sql_str = "CREATE TABLE Artist(" + \
"Name VARCHAR NOT NULL," + \
"Artist_Url VARCHAR NOT NULL," + \
"Number_Followers INT NOT NULL," + \
"PRIMARY KEY (Artist_Url));"
db.engine.execute(sql_str)

#create the USER table
sql_str = "CREATE TABLE User(" + \
"Username VARCHAR NOT NULL," + \
"Password VARCHAR NOT NULL," + \
"E-mail VARCHAR NOT NULL," + \
"Artist_Url VARCHAR NOT NULL," + \
"PRIMARY KEY (E-mail));"
db.engine.execute(sql_str)

#create the BY table
db.engine.execute(sql_str)

#create the UPVOTE table
db.engine.execute(sql_str)

#create the PLAYLIST table
db.engine.execute(sql_str)

# commit the results to keep them
db.session.commit()
if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
    api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
else:
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, api.version(SQLALCHEMY_MIGRATE_REPO))
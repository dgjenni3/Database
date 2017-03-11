#!flask/bin/python
from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO
from app import db
import os.path
# this python file deletes all the database tables that will be used by the application
# DO NOT RUN THIS FILE MORE THAN ONCE --- you only need to delete the tables once!

db.delete_all()

# delete the SONG table
if db.engine.dialect.has_table(db.engine, "Song"):
	db.engine.execute("DROP TABLE Song;")

# delete the ARTIST table
if db.engine.dialect.has_table(db.engine, "Artist"):
	db.engine.execute("DROP TABLE Artist;")

# delete the USER table
if db.engine.dialect.has_table(db.engine, "UserTable"):
	db.engine.execute("DROP TABLE UserTable;")

# delete the BY table
if db.engine.dialect.has_table(db.engine, "By"):
	db.engine.execute("DROP TABLE By;")

# delete the UPVOTE table
if db.engine.dialect.has_table(db.engine, "Upvote"):
	db.engine.execute("DROP TABLE Upvote;")

# delete the PLAYLIST table
if db.engine.dialect.has_table(db.engine, "Playlist"):
	db.engine.execute("DROP TABLE Playlist;")

# commit the results to keep them
# db.session.commit()
# if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
    # api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
    # api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
# else:
    # api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, api.version(SQLALCHEMY_MIGRATE_REPO))
from flask import render_template, request, redirect, url_for
from app import app, db
import os

@app.route('/')
@app.route('/index')
def index():
	return render_template("index.html", logged_in=os.environ.get('LOGGED_IN'), username=os.environ.get('CURR_USER'))
	
@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		sql_str = "SELECT Username FROM UserTable WHERE Username='" + request.form['username'] + "';"
		req_user = db.engine.execute(sql_str).fetchall()
		sql_str = "SELECT Password FROM UserTable WHERE Password='" + request.form['password'] + "';"
		req_pass = db.engine.execute(sql_str).fetchall()
		valid = False
		if len(req_user) == 1 and len(req_pass) == 1:
			if str(req_user[0][0]) == request.form['username']:
				if str(req_pass[0][0]) == request.form['password']:
					valid = True
					
		if valid == True:
			os.environ['CURR_USER'] = request.form['username']
			os.environ['LOGGED_IN'] = 'YES'
			return redirect(url_for('/success'))
		else:
			return render_template("login.html", error=True, logged_in=os.environ.get('LOGGED_IN'))
				
	# return the user login page on a GET request
	return render_template("login.html", error=False, logged_in=os.environ.get('LOGGED_IN'))
	
@app.route('/signup', methods=['GET', 'POST'])
def signup():
	error = False
	if request.method == 'POST':
		sql_str = "INSERT INTO UserTable(Username, Password, Email, Artist_Url) VALUES ('" + request.form['username'] + "', '" + request.form['password'] + \
		"', '" + request.form['email'] + "', '" + request.form['username'] + "');"
		create_user = db.engine.execute(sql_str)
		sql_str = "SELECT * FROM UserTable;"
		all_users = db.engine.execute(sql_str).fetchall()
		os.environ['CURR_USER'] = request.form['username']
		os.environ['LOGGED_IN'] = 'YES'
		return redirect(url_for('/success'))
	return render_template("signup.html", error=error, logged_in=os.environ.get('LOGGED_IN'), username=os.environ.get('CURR_USER'))
	
@app.route('/success')
def success():
	return render_template("success.html", logged_in=os.environ.get('LOGGED_IN'), username=os.environ.get('CURR_USER'))
	
@app.route('/logout')
def logout():
	os.environ['CURR_USER'] = ''
	os.environ['LOGGED_IN'] = 'NO'
	return redirect(url_for('/'))
	
@app.route('/upload', methods=['GET', 'POST'])
def upload():
	if request.method == 'POST':
		sql_str = "INSERT INTO Song(Title, Created_at, Soundcloud_Views, Song_Url, Genre, Track_type, Duration, " + \
		"Soundcloud_Favorites) VALUES('" + request.form['title'] + "', 1234, 0, '" + request.form['song_url'] + \
		"', '" + request.form['genre'] + "', '" + request.form['track_type'] + "', 8, 0);"
		new_song = db.engine.execute(sql_str)
		return redirect(url_for('/songs'))
	return render_template("upload.html", username=os.environ.get('CURR_USER'), logged_in=os.environ['LOGGED_IN'])
	
@app.route('/songs')
def songs():
	sql_str = "SELECT * FROM Song;"
	all_songs = db.engine.execute(sql_str).fetchall()
	return render_template("songs.html", username=os.environ.get('CURR_USER'), logged_in=os.environ['LOGGED_IN'], song_list=all_songs)
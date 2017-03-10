from flask import render_template, request
from app import app, db



@app.route('/')
@app.route('/index')
def index():
    username = 'TEST_USERNAME'
    return render_template("index.html", logged_in=None, username=username)
	
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
			return render_template("success.html", username=request.form['username'], logged_in=True)
		else:
			return render_template("login.html", error=True, logged_in=None)
				
	# return the user login page on a GET request
	return render_template("login.html", error=False, logged_in=None)
	
@app.route('/signup', methods=['GET', 'POST'])
def signup():
	error = False
	if request.method == 'POST':
		sql_str = "INSERT INTO UserTable(Username, Password, Email, Artist_Url) VALUES ('" + request.form['username'] + "', '" + request.form['password'] + \
		"', '" + request.form['email'] + "', '" + request.form['username'] + "');"
		create_user = db.engine.execute(sql_str).fetchall()
		return render_template("success.html", username=request.form['username'], logged_in=True)
	return render_template("signup.html", error=error, logged_in=None)
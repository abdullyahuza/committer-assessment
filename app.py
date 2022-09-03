#----------------------------------------------------------------------------#
# Imports.
#----------------------------------------------------------------------------#
from flask import Flask, request, render_template, redirect, url_for, flash, session, send_file, jsonify, abort
from flask_session import Session
from tempfile import mkdtemp
from database.models import db, setup_db,db_drop_and_create_all, User
from auth import login_required
from werkzeug.security import check_password_hash 
from datetime import timedelta

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# use session
@app.before_first_request  # runs before FIRST request (only once)
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=10)


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
setup_db(app)

# db_drop_and_create_all()

#----------------------------------------------------------------------------#
# App Routes.
#----------------------------------------------------------------------------#

# Home route
@app.route('/')
def index():
	return render_template('index.html')

# Dashboard route
@app.route('/lead', methods=['GET','POST'])
def login():
	
	# Forget any user_id
	session.clear()

	if request.method == "POST":
		uname = request.form["username"]
		passw = request.form["password"]

		login = User.query.filter_by(username=uname).first()
		if login is not None:
			# check pass
			if check_password_hash(login.password, passw):
				# Remember which user has logged in
				session["user_id"] = login.username
				return redirect(url_for("dashboard"))
	return render_template("admin/login.html")


# Dashboard route
@app.route('/dashboard')
@login_required
def dashboard():
	return render_template('admin/index.html', current_page="Dashboard")


# File_prediction route
@app.route('/from_file')
@login_required
def from_file():
	return render_template('admin/upload.html', current_page="Prediction from file")

# Prediction result route
@app.route('/status')
@login_required
def status():
	return render_template('admin/prediction_result.html', current_page="Prediction Status")

# Prediction result route
@app.route('/status-file')
@login_required
def status_file():
	return render_template('admin/prediction_result_file.html', current_page="File Prediction Status")

# logout route
@app.route('/logout')
def logout():
	session.clear()
	return redirect('/lead')

# logout route
@app.route('/error')
def error():
	return render_template('error.html')

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html', error_code=404, error_msg="The page you are looking for doesn't exist.")
    return({
        "success": False,
        "message": "resource not found",
        "error": 404
    }), 404

if __name__ == '__main__':
	app.run(debug=True)
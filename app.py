#----------------------------------------------------------------------------#
# Imports.
#----------------------------------------------------------------------------#
from flask import Flask, request, render_template, redirect, url_for, flash, session, send_file, jsonify, abort
from flask_session import Session
from tempfile import mkdtemp
from database.models import db, setup_db, db_drop_and_create_all, User, Enquiry
from auth import login_required
from werkzeug.security import check_password_hash
from datetime import timedelta, date
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

db_drop_and_create_all()

#----------------------------------------------------------------------------#
# App Routes.
#----------------------------------------------------------------------------#

# Home route


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":

        new_enquiry = Enquiry(
            name=request.form["name"],
            age=request.form["age"],
            education=request.form["education"],
            email=request.form["email"],
            region=request.form["region"],
            fin_gain=request.form["fin_gain"],
            int_learn=request.form["int_learn"],
            dev_inv=request.form["dev_inv"],
            proj_desertion=request.form["proj_desertion"],
            dev_status=request.form["dev_status"],
            dev_experience=request.form["dev_experience"],
            sys_int=request.form["sys_int"],
            tech_norm=request.form["tech_norm"],
            code_test=request.form["code_test"],
            cont_code_dec=request.form["cont_code_dec"],
            dec_right_del=request.form["dec_right_del"],
            proj_age=request.form["proj_age"],
            date_submitted=date.today()
        )
        db.session.add(new_enquiry)
        db.session.commit()
        flash({'type': 'success', 'msg': 'You\'ve Successfully submitted your data.'})
        return redirect('/#form')
    return render_template('index.html')

# Dashboard route


@app.route('/lead', methods=['GET', 'POST'])
def login():
    if session.get("user_id"):
        return redirect(url_for("dashboard"))
    # Forget any user_id
    # session.clear()

    if request.method == "POST":
        uname = request.form["username"]
        passw = request.form["password"]

        login = User.query.filter_by(username=uname).first()
        if login is not None:
            # check pass
            if check_password_hash(login.password, passw):
                # Remember which user has logged in
                session["user_id"] = login.username
                flash({'type': 'success', 'msg': f'Welcome back, {login.name}'})
                return redirect(url_for("dashboard"))
        flash({'type': 'error', 'msg': 'Invalid login credentials'})
    return render_template("admin/login.html")


# Dashboard route
@app.route('/dashboard')
@login_required
def dashboard():
    user = User.query.filter_by(username=session['user_id']).first()
    user_data = user.details()

    enquiries = Enquiry.query.all()

    return render_template(
        'admin/index.html',
        current_page="Dashboard",
        user=user_data,
        enquiries=enquiries)


# Confirm route
@app.route('/confirm/<int:e_id>')
@login_required
def confirm(e_id):
    user = User.query.filter_by(username=session['user_id']).first()
    user_data = user.details()

    e_query = Enquiry.query.get(e_id)

    return render_template(
        'admin/confirm.html',
        current_page="Confirm Data",
        user=user_data, enquiry=e_query.details())

# File_prediction route
@app.route('/from_file')
@login_required
def from_file():
    user = User.query.filter_by(username=session['user_id']).first()
    user_data = user.details()
    return render_template(
        'admin/upload.html',
        current_page="Prediction from file",
        user=user_data)

# Prediction result route
@app.route('/status')
@login_required
def status():
    user = User.query.filter_by(username=session['user_id']).first()
    user_data = user.details()

    return render_template(
        'admin/prediction_result.html',
        current_page="Prediction Status",
        user=user_data)

# Prediction result route
@app.route('/status-file')
@login_required
def status_file():
    user = User.query.filter_by(username=session['user_id']).first()
    user_data = user.details()

    return render_template(
        'admin/prediction_result_file.html',
        current_page="File Prediction Status",
        user=user_data)

# logout route


@app.route('/logout')
@login_required
def logout():
    session.clear()
    return redirect('/lead')

# logout route


@app.route('/error')
def error():
    return render_template('error.html')


@app.errorhandler(404)
def not_found(error):
    return render_template(
        'error.html',
        error_code=404,
        error_msg="The page you are looking for doesn't exist.")
    return ({
        "success": False,
        "message": "resource not found",
        "error": 404
    }), 404


if __name__ == '__main__':
    app.run(debug=True)

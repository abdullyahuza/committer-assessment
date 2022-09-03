from flask import Flask, request, render_template, redirect, url_for, flash, session, send_file, jsonify, abort

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#
app = Flask(__name__)

# Home route
@app.route('/')
def index():
	return render_template('index.html')

# Dashboard route
@app.route('/lead')
def login():
	return render_template('admin/login.html')


# Dashboard route
@app.route('/dashboard')
def dashboard():
	return render_template('admin/index.html', current_page="Dashboard")


# File_prediction route
@app.route('/from_file')
def from_file():
	return render_template('admin/upload.html', current_page="Prediction from file")

# Prediction result route
@app.route('/status')
def status():
	return render_template('admin/prediction_result.html', current_page="Prediction Status")

# Prediction result route
@app.route('/status-file')
def status_file():
	return render_template('admin/prediction_result_file.html', current_page="File Prediction Status")

if __name__ == '__main__':
	app.run(debug=True)
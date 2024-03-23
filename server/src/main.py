# Library Imports
from flask import Flask, render_template, session, request, flash, redirect, make_response, url_for, send_from_directory, send_file, redirect
import flask_monitoringdashboard as dashboard
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from markupsafe import escape
from logger import log
import logging

# File Imports
from constants import SECRET_KEY

# Initialize Flask
app = Flask(__name__)
dashboard.bind(app)
app.secret_key = SECRET_KEY
test_request = app.test_request_context()




# Configure Login Manager
login_manager = LoginManager()
login_manager.init(app)


# Error Handler
@app.errorhandler(404)
def page_not_found(error):
  return '404 Not Found'
# STATIC ROUTES 
@app.route("/")
def index():
  return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'GET':
    return render_template('/pages/auth/login.html')
## AUTH ROUTES (STATIC)
@app.route('/register', methods=['GET', 'POST'])
def signup():
  if request.method == 'GET':
    return render_template('@/frontend/pages/auth/register.html')

## DYNAMIC ROUTES
  
@app.route('/profile/<username>')
def profile(username):
  response = make_response(render_template('profile.html', username))
  if 'username' in session:
    return response 
  else: 
    return render_template('frontend/pages/login_required.html') 
@app.post('/profile/<username>/upload')
def upload_avatar(username):
  file = request.files['avatar']
  file.save(f"/storage/avatars/{username}.jpg")  
  log.info(f'User {username} uploaded their avatar.')
@app.route('/post/<int:post_id>')

def post(post_id): 
  return f'Post {post_id}'

## API ROUTES ##
@app.route('/users')
def users_api():
  users = ['test1', 'test2', 'test3']
  # users = get_all_users()  
  return [user.to_json() for user in users]
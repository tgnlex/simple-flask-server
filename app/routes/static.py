from app import app 
from flask import Flask, request, render_template, make_response, session
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
# STATIC ROUTES 

@app.get("/")
def get_index():
  return render_template('pages/index.html', title="Home")
   # STATIC AUTH ROUTES

@app.get('/about')
def get_about():
  return render_template('pages/about.html')   

@app.get('/login')
def get_login_form():
  return render_template('pages/auth/login.html')

@app.get('/register')
def get_register_form():
  return render_template('pages/auth/register.html')

@app.route('/terms')
def get_terms():
  return render_template('pages/auth/terms.html')

@app.get('/required')
def get_login_required():
  return render_template('errors/required.html')
    ## END STATIC AUTH ROUTES## 
    ## AUTH HANDLING ROUTES ##


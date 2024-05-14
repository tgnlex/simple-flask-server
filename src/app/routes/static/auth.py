from src import app 
from flask import Flask, request, render_template, make_response, session

@app.get('/login')
def get_login_form():
  return render_template('src/staticpages/auth/login.html')

@app.get('/register')
def get_register_form():
  return render_template('src/static/pages/auth/register.html')

@app.route('/terms')
def get_terms():
  return render_template('src/static/pages/auth/terms.html')

@app.get('/required')
def get_login_required():
  return render_template('errors/required.html')
    ## END STATIC AUTH ROUTES## 
    ## AUTH HANDLING ROUTES ##

from src import app 
from flask import Flask, request, render_template, make_response, session, request 
# STATIC ROUTES 

@app.get("/")
def get_index():
  return render_template('app/static/pages/index.html', title="Home")
   # STATIC AUTH ROUTES

@app.get('/about')
def get_about():
  return render_template('src/static/views/about.html')   


@app.errorhandler(404)
def page_not_found(error):
    return render_template('src/static/views/page_not_found.html'), 404
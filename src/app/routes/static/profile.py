from flask import Flask, request, render_template, make_response, session, request 
from src.app import app 

@app.get('/profile/avatar')
def get_upload():
  render_template('src/static/pages/profile/avatar')

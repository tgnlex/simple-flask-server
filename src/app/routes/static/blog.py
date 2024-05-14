from src import app 
from flask import Flask, request, render_template, make_response, session

@app.get('/blog/index')
def get_blog():
  return render_template('app/static/pages/view/blog.html')
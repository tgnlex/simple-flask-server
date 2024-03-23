from flask import Flask, make_response
from app import app
@app.post('/auth/login')
def post_register():
  return make_response('Post @ login success')
@app.post('/auth/login')  
def post_login():
  return make_response('Post @ register success')
@app.post('/auth/logout')
def post_logout():
  return make_response('Post @ Logout Success')
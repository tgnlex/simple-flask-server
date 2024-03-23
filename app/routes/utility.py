from flask import Flask, make_response
from app import app
@app.route("/test")
def test():
  return make_response('[FLASK]: Server is Running')

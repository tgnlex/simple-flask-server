from flask import Flask, make_response
from src import app
@app.route("/test", methods=['POST'])
def test():
  return make_response('[FLASK]: Server is Running')

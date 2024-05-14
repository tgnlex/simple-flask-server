from flask import Flask, json
from werkzeug.exceptions import HTTPException

from config import AppConfig
def create_app(test_config=None):
  global app 
  app = Flask(__name__, instance_relative_config=True)
  app.config = AppConfig
   

@app.errorhandler(HTTPException)
def handle_exception(e):
  if isinstance(e, HTTPException): 
    response = e.get_response()
    response.data = json.dumps({
      "code": e.code,
      "name": e.name,
      "message": e.description
    })
    response.content_type = "application/json"
    return response
  #handle non-http exceptions 
  return render_template("")
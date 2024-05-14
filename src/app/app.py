from flask import Flask
from config import AppConfig
def create_app(test_config=None):
  global app 
  app = Flask(__name__, instance_relative_conig=True)
  app.config = AppConfig
  
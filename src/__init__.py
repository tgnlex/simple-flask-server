from flask import Flask

from src.app.routes.auth import index
from src.app.routes.static import index, blog, auth 

app = Flask(__name__)




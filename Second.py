from flask import request
from markupsafe import escape
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Index Page"


@app.route("/hello")
def index():
    return "Hello world"
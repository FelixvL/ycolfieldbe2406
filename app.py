from flask import Flask
import bootmodel

from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)

@app.route("/")
def hello_world():
    bootmodel.opslaan("eersteboot", 25)
    return "<p>Hello, World!</p>"

@app.route("/anders")
def anders():
    return bootmodel.allebotenopvragen()

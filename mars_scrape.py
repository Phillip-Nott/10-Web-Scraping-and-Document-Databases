from flask import Flask, render_template
from flask_pymongo import PyMongo
import mission_to_mars

app = Flask(__name__)

# using flask_pymongo, set up mongoDB connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mission_to_mars
mongo = PyMongo(app)

@app.route("/")
def index():
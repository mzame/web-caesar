from flask import Flask, request
from caesar import rotate_string
from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return "Hello World"

def encrypt("/")

app.run()

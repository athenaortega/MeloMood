from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return "<p>Hello, World!</p>"

@app.route("/about")
def about():
    return "<p>This is my first app!</p>"
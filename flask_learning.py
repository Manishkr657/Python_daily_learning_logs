#Flask is a micro web framework written in python.
#Unlike Django, which comes with built-in features like authentication and an admin panel, Flask keeps things minimal and lets us add only what we need
#Microframework: Flask is considered a "micro" web framework because it is lightweight and simple to use, with minimal dependencies.
#Werkzeug and Jinja2: Flask is built on top of two powerful libraries:
# Werkzeug: A comprehensive WSGI web server library that helps manage the application's request and response cycles.
# Jinja2: A templating engine that allows you to use dynamic HTML in your application, making it easy to build web pages with variables and loops.

from flask import Flask 
from flask import jsonify
app = Flask(__name__)
@app.route('/')
def first():
    return "Hello, Flask!"

@app.route("/about")
def about():
    return "This is the About page."

@app.route("/greet/<name>")
def greet(name):
    return f"Hello, {name}!"

@app.route("/api/data")
def api_data():
    return jsonify({"name": "SkillBarter", "status": "active"})

from flask import request

@app.route("/submit", methods=["POST"])
def submit():
    data = request.json
    return jsonify({"you_sent": data})

if __name__ == '__main__':
    app.run(debug=True)
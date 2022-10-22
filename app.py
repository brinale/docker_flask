from flask import Flask
import os
import socket

counter = 0
app = Flask(__name__)

@app.route("/")
def show():
    return counter
    hi
@app.route("/stat")
def show():
    html = "{counter}"
    counter=counter+1
    return html.format(name=os.getenv("NAME", "world"))

@app.route("/about")
def hello():
    
    html = "<h3>Hello, Arina Belousova!</h3>" 
    return html.format(name=os.getenv("NAME", "world"))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
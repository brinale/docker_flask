from flask import Flask, g
import os
import socket

app = Flask(__name__)
counter = 0

@app.route("/")
def show():
    global counter
    html = f"<p>{counter}</p>"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname())

@app.route("/about")
def hello():
    html = "<h3>Hello, Arina Belousova!</h3>" 
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname())

@app.route("/stat")
def incr():
    global counter
    html = f"<p>{counter}</p>"
    counter = counter + 1
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
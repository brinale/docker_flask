from flask import Flask
import os
import socket

counter = 0
app = Flask(__name__)

@app.route("/")
def hello():
    html = "<h3>Hello, Arina Belousova!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname())

@app.route("/about")
def show():
    html = "<p>{counter}</p>"
    return html.format(name=os.getenv("NAME", "world"))

@app.route("/stat")
def incr():
    html = "<p>{counter}</p>"
    counter=counter+1
    return html.format(name=os.getenv("NAME", "world"))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
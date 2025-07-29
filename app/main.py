from flask import Flask, render_template
import socket
import datetime
import random

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def index():
    ip_address = socket.gethostbyname(socket.gethostname())
    version = "v1.3"
    return render_template("index.html", ip=ip_address, version=version)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def get_host_ip():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return f"<strong>Host IP: </strong>{ip}\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
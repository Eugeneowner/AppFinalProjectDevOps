from flask import Flask, render_template_string
import socket
import datetime
import random

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Pod Info</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f5f6fa;
            text-align: center;
            padding-top: 50px;
        }
        .card {
            display: inline-block;
            background: #fff;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 0 20px rgba(0,0,0,0.1);
        }
        h1 {
            color: #333;
        }
        p {
            font-size: 18px;
        }
        canvas {
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>🧠 Flask App Status</h1>
        <p><strong>IP:</strong> {{ pod_ip }}</p>
        <p><strong>Version:</strong> v1.3</p>
        <canvas id="loadChart" width="400" height="180"></canvas>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script>
        const ctx = document.getElementById('loadChart').getContext('2d');
        const chart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: {{ labels | safe }},
                datasets: [{
                    label: 'CPU Load (%)',
                    data: {{ values | safe }},
                    borderColor: 'rgba(75, 192, 192, 1)',
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    tension: 0.4
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true,
                        max: 100
                    }
                }
            }
        });
    </script>
</body>
</html>
"""


@app.route("/")
def index():
    pod_ip = socket.gethostbyname(socket.gethostname())
    labels = [(datetime.datetime.now() - datetime.timedelta(minutes=i)).strftime("%H:%M") for i in range(9, -1, -1)]
    values = [random.randint(10, 90) for _ in range(10)]
    return render_template_string(HTML_TEMPLATE, pod_ip=pod_ip, labels=labels, values=values)

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)



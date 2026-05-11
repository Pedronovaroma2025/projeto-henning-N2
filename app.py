from flask import Flask, render_template_string
import random
import os

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Container Dashboard</title>

    <style>
        body{
            background:#0f172a;
            color:white;
            font-family:Arial;
            padding:40px;
        }

        h1{
            text-align:center;
            color:#38bdf8;
        }

        .container{
            background:#1e293b;
            padding:20px;
            margin:20px;
            border-radius:15px;
            box-shadow:0 0 10px rgba(0,0,0,0.3);
        }

        .online{
            color:#22c55e;
            font-weight:bold;
        }
    </style>

    <script>
        setTimeout(() => {
            location.reload();
        }, 3000);
    </script>

</head>

<body>

<h1>🚀 Dashboard de Containers</h1>

{% for c in containers %}

<div class="container">
    <h2>{{c.nome}}</h2>

    <p>Status:
    <span class="online">ONLINE</span>
    </p>

    <p>CPU: {{c.cpu}}%</p>

    <p>RAM: {{c.ram}}%</p>
</div>

{% endfor %}

</body>
</html>
"""

@app.route('/')
def home():

    containers = [
        {
            "nome":"Container API",
            "cpu":random.randint(10,90),
            "ram":random.randint(10,90)
        },

        {
            "nome":"Container Redis",
            "cpu":random.randint(10,90),
            "ram":random.randint(10,90)
        },

        {
            "nome":"Container Frontend",
            "cpu":random.randint(10,90),
            "ram":random.randint(10,90)
        }
    ]

    return render_template_string(HTML, containers=containers)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
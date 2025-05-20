from flask import Flask, render_template_string
import csv

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>NetScan Pro Web UI</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f4f4f4; padding: 20px; }
        table { border-collapse: collapse; width: 100%; background: white; }
        th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }
        th { background: #005b96; color: white; }
    </style>
</head>
<body>
    <h1>NetScan Pro - Scan Results</h1>
    <table>
        <thead>
            <tr>
                <th>IP Address</th>
                <th>Open Ports</th>
            </tr>
        </thead>
        <tbody>
            {% for row in rows %}
            <tr>
                <td>{{ row[0] }}</td>
                <td>{{ row[1] }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>
"""

@app.route("/")
def index():
    with open("results.csv", newline="") as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        rows = list(reader)
    return render_template_string(HTML_TEMPLATE, rows=rows)

if __name__ == "__main__":
    app.run(debug=True)
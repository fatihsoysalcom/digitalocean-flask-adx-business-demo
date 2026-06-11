import os
from datetime import datetime
import random
from flask import Flask, render_template_string

app = Flask(__name__)

# Basic HTML template for the web page
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ADX Business Demo on DigitalOcean</title>
    <style>
        body { font-family: sans-serif; margin: 40px; background-color: #f4f7f6; color: #333; }
        .container { max-width: 800px; margin: auto; background: #fff; padding: 30px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        h1 { color: #007bff; }
        p { line-height: 1.6; }
        .metric { background-color: #e9f5ff; border-left: 5px solid #007bff; padding: 15px; margin-top: 20px; border-radius: 4px; }
        .metric strong { color: #0056b3; }
        footer { text-align: center; margin-top: 30px; font-size: 0.9em; color: #666; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome to ADX Business Demo on DigitalOcean!</h1>
        <p>This is a simple Python Flask application simulating a basic service endpoint, similar to what an ADX Business component might offer when deployed on a DigitalOcean droplet.</p>
        <p>It demonstrates a minimal web service running on a cloud environment, ready to serve data or application interfaces.</p>

        <div class="metric">
            <h3>Current Business Metric Simulation:</h3>
            <p><strong>Timestamp:</strong> {{ current_time }}</p>
            <p><strong>Sales Performance Index:</strong> {{ sales_index }}</p>
            <p><strong>Customer Satisfaction Score:</strong> {{ csat_score }}%</p>
            <p>This data is dynamically generated to illustrate a basic data point served by a web application.</p>
        </div>

        <p>In a real ADX Business setup, this would be a more complex application interacting with databases, processing analytics, and providing detailed reports.</p>
    </div>
    <footer>
        <p>Example deployed on a DigitalOcean-like environment.</p>
    </footer>
</body>
</html>
"""

@app.route('/')
def home():
    """
    This endpoint simulates a basic dashboard or data display
    that an ADX Business component might provide.
    It shows dynamically generated data.
    """
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sales_index = round(random.uniform(100.0, 500.0), 2)
    csat_score = random.randint(70, 99)
    return render_template_string(
        HTML_TEMPLATE,
        current_time=current_time,
        sales_index=sales_index,
        csat_score=csat_score
    )

if __name__ == '__main__':
    # When deploying on DigitalOcean (or any server), you'd typically use a production-ready WSGI server
    # like Gunicorn or uWSGI, and proxy requests through Nginx.
    # For this simple example, Flask's built-in server is sufficient.
    # The host '0.0.0.0' makes the app accessible from outside the container/localhost.
    # The port can be configured via an environment variable, common in cloud deployments.
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

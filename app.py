from flask import Flask, jsonify, render_template_string
import os

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Flask Azure App</title>
        </head>
        <body>
            <h1>Welcome to Python Flask on Azure App Service!</h1>
            <p>Application deployed successfully.</p>
        </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "message": "Flask application is running"
    })

@app.route("/api")
def api():
    return jsonify({
        "application": "Flask on Azure App Service",
        "status": "success"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
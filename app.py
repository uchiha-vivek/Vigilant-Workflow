from flask import Flask, request, jsonify
from src.logger import setup_logger
from src.metrics import setup_metrics, log_metric, shutdown_metrics
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
logger = setup_logger()
setup_metrics()

@app.route('/')
def home():
    logger.info("Home page accessed")
    log_metric("page_view", 1, {"page": "home"})
    return "Welcome to the Chiro Assistant Health Care App "

@app.route('/login', methods=['POST'])
def login():
    user_id = request.json.get("user_id", "unknown")
    logger.info(f"User {user_id} logged in")
    log_metric("user_login", 1, {"user_id": user_id})
    return jsonify({"message": "Login successful"})

@app.route('/shutdown')
def shutdown():
    shutdown_metrics()
    logger.shutdown()
    return "Shutting down logger and metrics handler"

if __name__ == '__main__':
    app.run(debug=True)

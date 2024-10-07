from flask import Flask, jsonify

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return jsonify(message="Welcome to the Flask App")

    @app.route('/add/<int:a>/<int:b>')
    def add(a, b):
        result = a + b
        return jsonify(result=result)

    @app.route('/subtract/<int:a>/<int:b>')
    def subtract(a, b):
        result = a - b
        return jsonify(result=result)

    @app.route('/multiply/<int:a>/<int:b>')
    def multiply(a, b):
        result = a * b
        return jsonify(result=result)

    @app.route('/divide/<int:a>/<int:b>')
    def divide(a, b):
        if b == 0:
            return jsonify(error="Cannot divide by zero"), 400
        result = a / b
        return jsonify(result=result)

    return app

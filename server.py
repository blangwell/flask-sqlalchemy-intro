from models import app, db, User
from flask import jsonify, request, redirect, url_for

@app.route('/')
def home():
    return jsonify(message="Welcome to my api")

if __name__ == '__main__':
    app.run('localhost', 5000, debug=True)
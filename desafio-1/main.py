#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager
from src.database import db

app = Flask(__name__)
jwt = JWTManager(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['JWT_SECRET_KEY'] = 'thunderbolt-and-lightning'
app.config['SECRET_KEY'] = 'very-very-frightening-me'

with app.app_context():
    import src.models
    import src.resources
    db.init_app(app)


@app.before_first_request
def create_tables():
    print('Creating all application tables')
    db.create_all()


@app.route('/status')
def status():
    status = {'status': 'up'}
    return jsonify(status), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

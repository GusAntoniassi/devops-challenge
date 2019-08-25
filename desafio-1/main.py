#!/usr/bin/python
# -*- coding: utf-8 -*-

from src.database import db
from src.models.user import UserModel
from src.models.character import CharacterModel

import os
from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager

app = Flask(__name__)
jwt = JWTManager(app)

database_filename = 'app.db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + database_filename
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['JWT_SECRET_KEY'] = 'thunderbolt-and-lightning'
app.config['SECRET_KEY'] = 'very-very-frightening-me'

seed_database = True

# Verifica se o arquivo do banco de dados já existe
if (not os.path.isfile(
    os.path.join(os.path.dirname(__file__), database_filename)
)):
    seed_database = True

with app.app_context():
    import src.models
    import src.resources
    db.init_app(app)


@app.before_first_request
def create_tables():
    print('Creating all application tables')
    db.create_all()
    if (seed_database):
        print('Seeding database')

        characters = [
            CharacterModel(name='Aragorn Segundo Elessar',
                           race='men', age='210'),
            CharacterModel(name='Gandalf', race='Maia', age=''),
            CharacterModel(name='Sauron', race='Maia', age=''),
            CharacterModel(name='Bilbo Baggins', race='	Hobbit', age=''),
        ]

        for character in characters:
            character.save_to_db()

        users = [
            UserModel(
                username='gus',
                password='$argon2i$v=19$m=102400,t=2,p=8$jRHiHANAKGUspZQSwjhHiA$4KuUrqN2VCeCwKZY7hBOeA'
            ),
        ]

        for user in users:
            user.save_to_db()


@app.route('/status')
def status():
    status = {'status': 'up'}
    return jsonify(status), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

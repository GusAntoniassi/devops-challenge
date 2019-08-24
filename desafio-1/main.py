#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request

app = Flask(__name__)

characters = [
  { 'name': 'Aragorn Segundo Elessar', 'Race': 'men', 'age': '210' },
  { 'name': 'Gandalf', 'Race': 'Maia', 'age': '' },
  { 'name': 'Sauron', 'Race': 'Maia', 'age': '' },
  { 'name': 'Bilbo Baggins', 'Race': 'Hobbit', 'age': '' },
]


@app.route('/characters')
def get_characters():
  return jsonify(characters), 200


@app.route('/characters', methods=['POST'])
def add_characters():
  print(request.get_json())
  characters.append(request.get_json())
  return '', 204


@app.route('/status')
def status():
  status = {'status' : 'up'}
  return jsonify(status), 200

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')

#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request

app = Flask(__name__)

characters = [
  { 'id': 1, 'name': 'Aragorn Segundo Elessar', 'Race': 'men', 'age': '210' },
  { 'id': 2, 'name': 'Gandalf', 'Race': 'Maia', 'age': '' },
  { 'id': 3, 'name': 'Sauron', 'Race': 'Maia', 'age': '' },
  { 'id': 4, 'name': 'Bilbo Baggins', 'Race': 'Hobbit', 'age': '' },
]

@app.route('/characters')
def get_characters():
  return jsonify(characters), 200

@app.route('/characters/<int:id>')
def get_character(id):
  character = filter(lambda character: character['id'] == int(id), characters)

  if len(character) == 0:
    return 'Character not found', 404

  return jsonify(character), 200

@app.route('/characters', methods=['POST'])
def add_characters():
  character = request.get_json()
  character['id'] = len(characters)+1
  
  characters.append(character)
  return '', 204

@app.route('/characters/<int:id>', methods=['PUT'])
def edit_character(id):
  try:
    characterIndex = next(i for i, character in enumerate(characters) if character['id'] == int(id))
  except StopIteration:
    return 'Character not found', 404
  
  characters[characterIndex] = request.get_json()

  return '', 204

@app.route('/characters/<int:id>', methods=['DELETE'])
def delete_character(id):
  try:
    characterIndex = next(i for i, character in enumerate(characters) if character['id'] == int(id))
  except StopIteration:
    return 'Character not found', 404
  
  del characters[characterIndex]

  return '', 204

@app.route('/status')
def status():
  status = {'status' : 'up'}
  return jsonify(status), 200

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')

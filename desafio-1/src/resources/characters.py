from flask import jsonify, request, current_app as app
from flask_jwt_extended import jwt_required

characters = [
  { 'id': 1, 'name': 'Aragorn Segundo Elessar', 'Race': 'men', 'age': '210' },
  { 'id': 2, 'name': 'Gandalf', 'Race': 'Maia', 'age': '' },
  { 'id': 3, 'name': 'Sauron', 'Race': 'Maia', 'age': '' },
  { 'id': 4, 'name': 'Bilbo Baggins', 'Race': 'Hobbit', 'age': '' },
]

@app.route('/characters')
@jwt_required
def get_characters():
  return jsonify(characters), 200

@app.route('/characters/<int:id>')
@jwt_required
def get_character(id):
  character = filter(lambda character: character['id'] == int(id), characters)

  if len(character) == 0:
    return 'Character not found', 404

  return jsonify(character), 200

@app.route('/characters', methods=['POST'])
@jwt_required
def add_characters():
  character = request.get_json()
  character['id'] = len(characters)+1
  
  characters.append(character)
  return '', 204

@app.route('/characters/<int:id>', methods=['PUT'])
@jwt_required
def edit_character(id):
  try:
    characterIndex = next(i for i, character in enumerate(characters) if character['id'] == int(id))
  except StopIteration:
    return 'Character not found', 404
  
  character = request.get_json()
  character['id'] = id
  characters[characterIndex] = character

  return '', 204

@app.route('/characters/<int:id>', methods=['DELETE'])
@jwt_required
def delete_character(id):
  try:
    characterIndex = next(i for i, character in enumerate(characters) if character['id'] == int(id))
  except StopIteration:
    return 'Character not found', 404
  
  del characters[characterIndex]

  return '', 204

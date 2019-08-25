from src.models.character import CharacterModel

from flask import jsonify, request, current_app as app
from sqlalchemy import exc as SQLException
from flask_jwt_extended import jwt_required

@app.route('/characters')
@jwt_required
def get_characters():
  return jsonify(CharacterModel.returnAll()), 200

@app.route('/characters/<int:id>')
@jwt_required
def get_character(id):
  character = CharacterModel.findById(id)

  if not character:
    return jsonify({'message': 'Character with ID {} doesn\'t exist'.format(id)}), 404

  return jsonify(character), 200

@app.route('/characters/<name>')
@jwt_required
def get_character_by_name(name):
  character = CharacterModel.findByName(name)

  if not character:
    return jsonify({'message': 'Character with name {} doesn\'t exist'.format(name)}), 404

  return jsonify(character), 200

@app.route('/characters', methods=['POST'])
@jwt_required
def add_characters():
  data = request.get_json()
  newCharacter = CharacterModel(
    name = data['name'],
    race = data['race'],
    age = data['age'],
  )
  
  try:
    newCharacter.saveToDb()
    return '', 204
  except Exception as e:
    print('Exception: ', e)
    return jsonify({ 'message': 'Something went wrong' }), 500

@app.route('/characters/<int:id>', methods=['PUT'])
@jwt_required
def edit_character(id):
  data = request.get_json()

  try:
      CharacterModel.update(id, data)
  except LookupError:
      return jsonify({'message': 'Character with ID {} doesn\'t exist'.format(id)}), 404

  return '', 204

@app.route('/characters/<int:id>', methods=['DELETE'])
@jwt_required
def delete_character(id):
  try: 
    CharacterModel.delete(id)
  except LookupError:
    return jsonify({'message': 'Character with ID {} doesn\'t exist'.format(id)}), 404


  return '', 204

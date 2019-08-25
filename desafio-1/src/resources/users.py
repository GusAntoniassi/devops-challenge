from src.models.user import UserModel

from flask import jsonify, request, current_app as app
from sqlalchemy import exc as SQLException
from flask_jwt_extended import create_access_token

@app.route('/login', methods=['POST'])
def login():  
  data = request.get_json()

  currentUser = UserModel.findByUsername(data['username'])

  if not currentUser:
    return jsonify({'message': 'User {} doesn\'t exist'.format(data['username'])}), 404
    
  if not UserModel.verifyHash(data['password'], currentUser.password):
    return jsonify({'message': 'Wrong credentials'})

  accessToken = create_access_token(identity = data['username'])

  return jsonify(
    {
      'message': 'Logged in as {}'.format(currentUser.username),
      'token': accessToken,
    }
  )

@app.route('/users')
def get_users():  
  return jsonify(UserModel.returnAll())

@app.route('/users', methods=['POST'])
def add_users():
  data = request.get_json()
  newUser = UserModel(
    username = data['username'],
    password = UserModel.generateHash(data['password'])
  )

  try:
    newUser.saveToDb()
    return jsonify(
      { 'message': 'User {} was created'.format(data['username']) }
    )
  except SQLException.IntegrityError:
    return jsonify({ 'message': 'This username is already in use' }), 409
  except Exception as e:
    print('Exception: ', e)
    return jsonify({ 'message': 'Something went wrong' }), 500

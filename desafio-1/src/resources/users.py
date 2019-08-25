from flask import jsonify, request, current_app as app
from src.models import UserModel
from sqlalchemy import exc as SQLException

@app.route('/login', methods=['POST'])
def login():  
  data = request.get_json()

  currentUser = UserModel.findByUsername(data['username']);

  if not currentUser:
    return jsonify({'message': 'User {} doesn\'t exist'.format(data['username'])})
    
  if UserModel.verifyHash(data['password'], currentUser.password):
    return jsonify({'message': 'Logged in as {}'.format(currentUser.username)})
  else:
    return jsonify({'message': 'Wrong credentials'})

@app.route('/logout', methods=['POST'])
def logout():  
  return jsonify({'message': 'User logout'})

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
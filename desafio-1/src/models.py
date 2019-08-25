from src.database import db
from passlib.hash import argon2 as hasher

# https://codeburst.io/jwt-authorization-in-flask-c63c1acf4eeb
class UserModel(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True} 

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(120), nullable = False)
    
    def saveToDb(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def findByUsername(cls, username):
        return cls.query.filter_by(username = username).first()
    
    @classmethod
    def returnAll(cls):
        def to_json(x):
            return {
                'username': x.username,
                'password': x.password
            }
        return (map(lambda x: to_json(x), UserModel.query.all()))

    @staticmethod
    def generateHash(password):
        return hasher.hash(password)

    @staticmethod
    def verifyHash(password, hash):
        return hasher.verify(password, hash)
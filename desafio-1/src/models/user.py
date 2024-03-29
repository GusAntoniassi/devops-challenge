from src.database import db
from passlib.hash import argon2 as hasher


class UserModel(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def return_all(cls):
        def to_json(x):
            return {
                'username': x.username
            }

        return map(to_json, UserModel.query.all())

    @staticmethod
    def generate_hash(password):
        return hasher.hash(password)

    @staticmethod
    def verifyHash(password, hash):
        return hasher.verify(password, hash)

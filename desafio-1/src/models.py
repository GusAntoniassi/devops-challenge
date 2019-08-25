from src.database import db
from passlib.hash import argon2 as hasher


class UserModel(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def saveToDb(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def findByUsername(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def returnAll(cls):
        def to_json(x):
            return {
                'username': x.username
            }

        return map(to_json, UserModel.query.all())

    @staticmethod
    def generateHash(password):
        return hasher.hash(password)

    @staticmethod
    def verifyHash(password, hash):
        return hasher.verify(password, hash)


class CharacterModel(db.Model):
    __tablename__ = 'characters'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    race = db.Column(db.String(120), nullable=False)
    age = db.Column(db.String(120), nullable=False)

    def saveToDb(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def to_json(cls, x):
        if not x:
            return
        
        return {
            'name': x.name,
            'race': x.race,
            'age': x.age
        }

    @classmethod
    def findById(cls, id):
        return cls.to_json(
            cls.query.filter_by(id=id).first()
        )

    @classmethod
    def findByName(cls, name):
        search = "{}%".format(name)
        return map(
            cls.to_json, 
            cls.query.filter(cls.name.ilike(search)).all()
        )

    @classmethod
    def returnAll(cls):
        return map(cls.to_json, cls.query.all())

    @classmethod
    def update(cls, id, data):
        character_query = cls.query.filter_by(id=id)

        if not character_query.first():
            raise LookupError

        character_query.update(data)

        db.session.commit()

    @classmethod
    def delete(cls, id):
        character_query = cls.query.filter_by(id=id)
        character_query.delete()

        if not character_query.first():
            raise LookupError
        
        db.session.commit()

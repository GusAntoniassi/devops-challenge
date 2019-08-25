from src.database import db


class CharacterModel(db.Model):
    __tablename__ = 'characters'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    race = db.Column(db.String(120), nullable=False)
    age = db.Column(db.String(120), nullable=False)

    def save_to_db(self):
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
    def find_by_id(cls, id):
        return cls.to_json(
            cls.query.filter_by(id=id).first()
        )

    @classmethod
    def find_by_name(cls, name):
        search = "{}%".format(name)
        return map(
            cls.to_json,
            cls.query.filter(cls.name.ilike(search)).all()
        )

    @classmethod
    def return_all(cls):
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

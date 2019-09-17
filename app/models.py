from . import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    # email = db.Column(db.string(100), unique = True)
    username = db.Column(db.String(200))
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))
    def __repr__(self):
        return f'User {self.username}'
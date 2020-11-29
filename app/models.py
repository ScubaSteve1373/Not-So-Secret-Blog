from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userName = db.Column(db.VARCHAR, unique=True)
    password = db.Column(db.String(128))
    email = db.Column(db.String(128))
    schoolYear = db.Column(db.String(128))
    schoolName = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, unique=True)
    description = db.Column(db.String(360))
    datetime = db.Column(db.DateTime, index=True)

    def __repr__(self):
        return '{}: {}'.format(self.name, self.description)


class UserToEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userID = db.Column(db.Integer, db.ForeignKey('user.id'))
    eventID = db.Column(db.Integer, db.ForeignKey('event.id'))

    def __repr__(self):
        return '{}'.format(self.name)

class Blog(db.model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    body = db.Column(db.String(360), index=True)
    datetime = db.Column(db.DateTime, index=True)
    userID = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '{}'.format(self.name)

class DiningHall(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))

    def __repr__(self):
        return '{}'.format(self.name)


class SnackingSlacking(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    datetime = db.Column(db.DateTime)
    description = db.Column(db.String(128))
    food = db.Column(db.String(128))
    userID = db.Column(db.Integer, db.ForeignKey('user.id'))
    diningID = db.Column(db.Integer, db.ForeignKey("dininghall.id"))

    def __repr__(self):
        return '{}'.format(self.name)

class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))

    def __repr__(self):
        return '{}'.format(self.name)

class Professor(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), index=True)
    rate = db.Column(db.Integer)
    comment = db.Column(db.String(128))
    departmentID = db.Column(db.Integer, db.ForeignKey('department.id'))

    def __repr__(self):
        return '{}: {}'.format(self.name, self.rate)
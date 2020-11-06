from . import db
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash
from . import login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Student(UserMixin,db.Model):
    __tablename__ ="students"
    student_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    phone = db.Column(db.Integer,unique = True)
    questions = db.Column(db.ARRAY(db.String))

    def get_id(self):
        return student_id


class Admin(db.Model):
    __tablename__ = "admins"
    admin_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    email = db.Column(db.String())
    approved = db.Column(db.Boolean)
    pass_word= db.Column(db.String(255))
    

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_word = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_word,password)


    def __repr__(self):
        return f'User {self.username}'

class Question(db.Model):
    __tablename__ ="questions"
    question_id = db.Column(db.Integer, primary_key = True)
    question = db.Column(db.String())
    subject = db.Column(db.String(255))
    grade = db.Column(db.Integer)
    seen = db.Column(db.Boolean)
    answer = db.relationship('Answer',backref = 'question',lazy="dynamic")

class Answer(db.Model):
    __tablename__ = "answers"
    answer_id = db.Column(db.Integer, primary_key = True)
    answer = db.Column(db.String(255))
    question_id = db.Column(db.Integer,db.ForeignKey('questions.question_id'))

class CurrentQuestion(db.Model):
    __tablename__ = "currentquestions"
    question_id = db.Column(db.Integer, primary_key = True)
    question = db.Column(db.String())
    subject = db.Column(db.String(255))
    grade = db.Column(db.Integer)
    seen = db.Column(db.Boolean)


from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
        
#add necessary imports
class Student(db.Model):
    __tablename__ ="students"
    student_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    phone = db.Column(db.String(11))
    questions = db.relationship('Question',backref = 'students',lazy="dynamic")

    def get_id(self):
        return student_id
        
class Question(db.Model):
    question_id = db.Column(db.Integer, primary_key = True) 
    question = db.Column(db.String())
    subject = db.Column(db.String(255))
    grade = db.Column(db.Integer)
    # seen = db.Column(db.Boolean)
    answer = db.Column(db.String())
    student_id = db.Column(db.Integer,db.ForeignKey('students.student_id'))

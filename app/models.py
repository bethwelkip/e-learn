from . import db

class Student(db.Model):
    __tablename__ ="students"
    student_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    phone = db.Column(db.Integer)
    questions = db.Column(db.ARRAY(db.String))

    def get_id(self):
        return student_id


class Admin(db.Model):
    __tablename__ ="admins"
    admin_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    email = db.Column(db.String())
    approved = db.Column(db.Boolean)


class Question(db.Model):
    __tablename__ ="questions"
    question_id = db.Column(db.Integer, primary_key = True)
    question = db.Column(db.String())
    subject = db.Column(db.String(255))
    grade = db.Column(db.Integer)
    seen = db.Column(db.Boolean)
    answer = db.relationship('Answer',backref = 'question',lazy="dynamic")

class Answer(db.Model):
    __tablename__ ="answers"
    answer_id = db.Column(db.Integer, primary_key = True)
    answer = db.Column(db.String(255))
    question_id = db.Column(db.Integer,db.ForeignKey('questions.question_id'))

class CurrentQuestion(db.Model):
    __tablename__ ="currentquestions"
    question_id = db.Column(db.Integer, primary_key = True)
    question = db.Column(db.String())
    subject = db.Column(db.String(255))
    grade = db.Column(db.Integer)
    seen = db.Column(db.Boolean)
    answer = db.Column(db.Integer,db.ForeignKey('students.student_id'))

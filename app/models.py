
#add necessary imports
class Student(db.Model):
    __tablename__ ="students"
    student_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    phone = db.Column(db.Integer, varchar(11))
    questions = db.relationship('Question',backref = 'students',lazy="dynamic")

    def get_id(self):
        return student_id
        
class Question(db.Model):
    question_id = db.Column(db.Integer, primary_key = True) "1"
    question = db.Column(db.String()) "what is 55 *76"
    subject = db.Column(db.String(255)) "Math"
    grade = db.Column(db.Integer) "5"
    # seen = db.Column(db.Boolean)
    answer = db.Column(db.String())
    student_id = db.Column(db.Integer,db.ForeignKey('students.student_id'))

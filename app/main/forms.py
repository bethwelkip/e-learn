from flask_wtf import FlaskForm
from wtforms import RadioField, TextAreaField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Required, Email, EqualTo
from wtforms import ValidationError

class quizForm(FlaskForm):
    Subject=RadioField('Label', choices=[('English', 'English'),('Science', 'Science'),('Kiswahili','Kiswahili'),('Math','Math')],validators=[Required()])
    A= TextAreaField('A', validators=[Required()])
    B= TextAreaField('B', validators=[Required()])
    C= TextAreaField('C', validators=[Required()])
    D= TextAreaField('D', validators=[Required()])
    Answer= TextAreaField('Answer', validators=[Required()])
    Submit =SubmitField('Submit')
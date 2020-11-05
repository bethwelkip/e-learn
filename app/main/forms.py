from flask_wtf import FlaskForm
from wtforms import RadioField, TextAreaField,StringField, PasswordField, SubmitField, BooleanField,FormField
from wtforms.validators import Required, Email, EqualTo
from wtforms import ValidationError
from ..models import Student

class quizForm(FlaskForm):
    Grade = StringField('Grade', validators=[Required()])
    Subject=RadioField('Label', choices=[('English', 'English'),('Science', 'Science'),('Kiswahili','Kiswahili'),('Math','Math')],validators=[Required()])
    question=TextAreaField('Question', validators=[Required()])
    A= TextAreaField('A', validators=[Required()])
    B= TextAreaField('B', validators=[Required()])
    C= TextAreaField('C', validators=[Required()])
    D= TextAreaField('D', validators=[Required()])
    Answer= TextAreaField('Answer', validators=[Required()])
    Submit =SubmitField('Submit')

class loginForm(FlaskForm):
    email = StringField('Your email address', validators=[Required(), Email()])
    password = PasswordField('Enter your password', validators=[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    name = StringField('Enter your username',validators = [Required()])
    mobile_phone = StringField('Enter your phone.no')
    submit = SubmitField('Sign Up')

    def validate_phone(self,data_field):
        if Student.query.filter_by(phone =data_field.data).first():
            raise ValidationError('Phone number already taken. Send join egg-unusual to +1415 523 8886 to start learning!')
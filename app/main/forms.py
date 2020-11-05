from flask_wtf import FlaskForm
from wtforms import RadioField, TextAreaField,StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Required, Email, EqualTo
from wtforms import ValidationError

class quizForm(FlaskForm):
    Grade = StringField('Grade', validators=[Required()])
    Subject=RadioField('Label', choices=[('English', 'English'),('Science', 'Science'),('Kiswahili','Kiswahili'),('Math','Math')],validators=[Required()])
    Question=TextAreaField('Question', validators=[Required()])
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
    mobile_phone = FormField('Enter your phone.no',validators = [Required()])
    submit = SubmitField('Sign Up')
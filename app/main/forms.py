from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import Required,Email,EqualTo
from ..models import User
from wtforms import ValidationError


class RegistrationForm(FlaskForm):
    name = StringField('Enter your username',validators = [Required()])
    mobile_phone = FormField('Enter your phone.no',validators = [Required()])
    submit = SubmitField('Sign Up')
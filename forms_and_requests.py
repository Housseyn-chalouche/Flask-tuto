from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

        # this is a registration form (for users who aren't signed yet)
class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=3, max=20)])
    # StringField : the fields of forms, here the first input(field) is the user name, the second is an email
    # validators : verify the integrity of user's names, DataRequired : make sure the name is not empty
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired(), EqualTo('Password')])
    # EqualTo : Confirm password field  must be equal to the Password field
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    # you don't need a user name to sign in, nor a confirmation password
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('LogIn')
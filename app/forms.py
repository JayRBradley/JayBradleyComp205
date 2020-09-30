from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class CreateAccountForm(FlaskForm):
   username = StringField('Username', validators=[DataRequired()])
   age = IntegerField('Age')
   password = PasswordField('Password', validators=[DataRequired()])
   submit = SubmitField('Sign In')


class AddNewArtistForm(FlaskForm):
    new_artist = StringField('Artist Name', validators=[DataRequired()])
    town = StringField('Hometown')
    description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Sign In')

from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, PasswordField, SubmitField
from wtforms.validators import Length, Email, EqualTo, DataRequired


class RegisterForm(FlaskForm):
    username = StringField(label='username', validators=[Length(min=2, max=10), DataRequired()])
    email = StringField(label='email', validators=[Email()])
    password1 = PasswordField(label='password1', validators=[Length(min=6)])
    password2 = PasswordField(label='password2', validators=[EqualTo('password1')])
    submit = SubmitField(label='submit')


class LoginForm(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired()])
    password = StringField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label="Submit")

    

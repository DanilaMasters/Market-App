from flask_wtf import FlaskForm
from wtforms import IntegerField
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


class PurchaseForm(FlaskForm):
    purchase_button = SubmitField(label='Submit', validators=[])


class AddItemForm(FlaskForm):
    name = StringField(label='Item Name', validators=[DataRequired()])
    price = IntegerField(label='Price', validators=[DataRequired()])
    barcode = StringField(label='Item Barcode', validators=[DataRequired()])
    description = StringField(label='Description', validators=[DataRequired()])
    submit = SubmitField(label="Submit")
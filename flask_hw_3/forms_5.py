from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    password_confirmation = PasswordField(
        'Confirm Password', validators=[DataRequired(), EqualTo('password')]
    )
    birth_date = DateField('Birth Date', validators=[DataRequired()])
    data_access = BooleanField('Consent to processing of personal data')


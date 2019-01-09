from wtforms import StringField, PasswordField, BooleanField, Form, validators
from flask_wtf.recaptcha import RecaptchaField

class RegisterForm(Form):  
  name = StringField('name', [validators.DataRequired(), validators.Length(max=255)]) 
  password = PasswordField('new password', [validators.DataRequired(),validators.Length(min=8),
                                            validators.EqualTo('confirm', message='password must match')]) 
  confirm = PasswordField('Repeat Password')     
  email = StringField('emailaddress', [validators.DataRequired(), validators.Length(min=6, max=35)]) 
  recaptcha = RecaptchaField()

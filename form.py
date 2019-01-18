from flask_wtf import Form, RecaptchaField
from wtforms import TextField, PasswordField, TextAreaField, StringField, validators

class RegisterForm(Form):  
  name = StringField('name', [validators.DataRequired(), validators.Length(max=255)]) 
  password = PasswordField('new password', [validators.DataRequired(), validators.Length(min=8)])
  email = StringField('emailaddress', [validators.DataRequired(), validators.Length(min=6, max=35)]) 
  recaptcha = RecaptchaField()

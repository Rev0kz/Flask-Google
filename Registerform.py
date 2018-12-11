from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, EqualTo, Length, 

class RegisterForm(FlaskForm):  
  name = StringField('name', [validator.DataRequired(), Length(max=255)]) 
  password = PasswordField('new password', [validator.DataRequired(),validators.EqaulTo('confirm', message='password must match']) 
  confirm = PasswordField('Repeat Password')                                        
  
     
          
          

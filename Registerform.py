from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, EqualTo, Length, 

class RegisterForm(FlaskForm):  
  name = StringField('name', [validator.DataRequired(), validators.Length(max=255)]) 
  password = PasswordField('new password', [validator.DataRequired(),validator.Length(min=8),
                                            validators.EqaulTo('confirm', message='password must match']) 
  confirm = PasswordField('Repeat Password')                                        
  
     
          
          

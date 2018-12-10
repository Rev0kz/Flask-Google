from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, 
from wtforms.validators import DataRequired

class RegisterForm(FlaskForm):  
  name = StringField('name', [validator.DataRequired(), Length(max=255)]) 
  password = PasswordField('new password', [validator.DataRequired()])  
  
     
          
          

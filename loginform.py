from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, 
from wtforms.validators import DataRequired

class Login(FlaskForm):  
  name = StringField('name', validators=[DataRequired(), Length(max=255)]) 
  password = PasswordField('password', validators=[DataRequired()])  
  
     
          
          

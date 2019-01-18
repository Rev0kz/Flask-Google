from flask import Flask, render_template, request
from form import RegisterForm  


app = Flask(__name__)

app.config['RECAPTCHA_USE_SSL']= False
app.config['RECAPTCHA_PUBLIC_KEY']='enter_your _public_key'
app.config['RECAPTCHA_PRIVATE_KEY']='enter_your_private_key'
app.config['RECAPTCHA_OPTIONS']= {'theme':'white'}


@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegisterForm()
	
	if form.validate_on_submit()
		return 'the form has been submitted. Success!'
	
    	return render_template("register.html", form=form)        





if __name__ == '__main__':
	app.run(port=5000, debug=True)

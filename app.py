from flask import Flask, render_template, request, redirect, url_for
from form import RegisterForm  


app = Flask(__name__)

app.config['RECAPTCHA_USE_SSL']= False
app.config['RECAPTCHA_PUBLIC_KEY']='enter_your _public_key'
app.config['RECAPTCHA_PRIVATE_KEY']='enter_your_private_key'
app.config['RECAPTCHA_OPTIONS']= {'theme':'white'}


@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegisterForm(request.form)
	if request.method == 'POST' and form.validate():
    		user = User(form.user.data, form.password.data, form.email.data)
		return redirect('/success')
    	return render_template("form.html", form=form)        


@app.route('/success')
def success():
  return 'registered successfully'



if __name__ == '__main__':
	app.run(port=5000, debug=True)

from flask import Flask, render_template, request
from form import RegisterForm  


app = Flask(__name__)

app.config['RECAPTCHA_USE_SSL']= False
app.config['RECAPTCHA_PUBLIC_KEY']='6LelJIAUAAAAAKUaSluZ-TakFlNc8rHAH-Lq7UBS'
app.config['RECAPTCHA_PRIVATE_KEY']='6LelJIAUAAAAAD-h6TVx4wufNd5XMa-b_4V7Yxr0'
app.config['RECAPTCHA_OPTIONS']= {'theme':'white'}


@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegisterForm(request.form)
	if request.method == 'POST' and form.validate():
    		user = User(form.user.data, form.password.data, form.email.data)
    		flash("successful registration")
    		return redirect(url_for("googlemap"))
  	return render_template("form.html", form=form)



if __name__ == '__main__':
	app.run(port=5000, debug=True)
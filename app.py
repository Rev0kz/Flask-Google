from flask import Flask , render_template 
from Login import Registerform   

app =  Fask(app)   


@app.route('/register', methods=['GET', 'POST'])
  form = Registerform(request.method)
  if request.method == 'POST' and form.validate()
    user = User(form.user.data, form.password.data, form.email.data)
    flash("successful registration")
    return redirect(url_for("googlemap"))
  return render_template("register.html", form=form)
    


if __name__ = '__main__':
  app.run(port=5000, debug=True



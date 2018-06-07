@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username']!='admin' or request.form['password']!='admin':
			error = "Invalid Crediantial. Please try again"
		else:
			session['logged_in']=True
			flash("You were just logged in")
			return redirect(url_for("home"))
	return render_template("login.html", error= error)

@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash("You were just logged out")
	return redirect(url_for("welcome"))

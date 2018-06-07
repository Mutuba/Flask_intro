
from flask import flash, redirect, render_template, request,\
    url_for, Blueprint  # pragma: no cover
from flask_login import login_user,\
    login_required, logout_user  # pragma: no cover
from .forms import LoginForm, RegisterForm  # pragma: no cover
# from functools import wraps
from project.models import User, bcrypt, db # pragma: no cover


users_blueprint = Blueprint(
    'users', __name__,
    template_folder='templates'
)


@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = db.session.query(
                User).filter_by(name=form.username.data).first()
            if user is not None and bcrypt.check_password_hash(
                    user.password, form.password.data):
                # session['logged_in'] = True
                login_user(user)
                flash("You were just logged in")
                return redirect(url_for("home.home"))
            else:
                error = "Invalid Crediantial. Please try again"
    return render_template("login.html", form=form, error=error)


@users_blueprint.route('/logout')
@login_required
def logout():
    # session.pop('logged_in', None)
    logout_user()
    flash("You were just logged out")
    return redirect(url_for("home.welcome"))


@users_blueprint.route(
    '/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(
            name=form.username.data,
            email=form.email.data,
            password=form.password.data
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('home.home'))
    return render_template('register.html', form=form)

from project import db # pragma: no cover
from project.models import BlogPost # pragma: no cover
from flask import render_template, redirect, url_for, flash, Blueprint# pragma: no cover
# from functools import wraps
from flask_login import login_required, current_user # pragma: no cover
from .forms import MessageForm # pragma: no cover


home_blueprint = Blueprint(
    'home', __name__,
    template_folder='templates'
)


@home_blueprint.route('/', methods=['GET', 'POST'])
@login_required
def home():
    error = None
    form = MessageForm()
    if form.validate_on_submit():
        new_message = BlogPost(
            form.title.data,
            form.description.data,
            current_user.id
        )
        db.session.add(new_message)
        db.session.commit()
        flash("New entry was successfully posted. Thanks.")
        return redirect(url_for('home.home'))
    posts = db.session.query(BlogPost).all()
    return render_template(
        'index.html', posts=posts, form=form, error=error)


@home_blueprint.route('/welcome')
@login_required
def welcome():
    return render_template('welcome.html')

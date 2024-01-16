from flask import render_template, url_for, redirect

from forms import RegisterForm
from market import app, db
from market.models import Item, User


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.get('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)


@app.route('/about/<username>')
def about(username):
    return f"<h1>This is about page of {username}</h1>"


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(name=form.username.data, email=form.email.data, password_hash=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))
    return render_template('register.html', form=form)

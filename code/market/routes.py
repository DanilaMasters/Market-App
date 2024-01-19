from flask import render_template, url_for, redirect, flash

from market.forms import LoginForm, RegisterForm
from market import app, db
from market.models import Item, User

from flask_login import login_required, login_user, logout_user


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.get('/market')
@login_required
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
        user_to_create = User(name=form.username.data, email=form.email.data, password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))
    if form.errors != {}:
        for error in form.errors.values():
            flash(f'There was an error with creating a user: {error}', category='danger')
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        atempted_user = User.query.filter_by(name=form.username.data).first()
        if atempted_user and atempted_user.check_password_correction(atempted_password=form.password.data):
            login_user(atempted_user)
            flash('You are logged in!', category='success')
            return redirect(url_for('market_page'))
        else:
            flash('Username and pasword do not match! Please try again', category='danger')
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash('You are logged out!', category='info')
    return redirect(url_for('home_page'))
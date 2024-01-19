from flask import render_template, request, url_for, redirect, flash

from market.forms import AddItemForm, LoginForm, PurchaseForm, RegisterForm
from market import app, db
from market.models import Item, User

from flask_login import current_user, login_required, login_user, logout_user


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/market', methods=['POST', 'GET'])
@login_required
def market_page():
    purchase_form = PurchaseForm()
    if request.method == 'POST':
        purchased_item_name = request.form.get('purchase_item')
        item = Item.query.filter_by(name=purchased_item_name).first()
        if item and current_user.can_purchase(item.price):
            item.owner = current_user.id
            current_user.budget -= item.price
            db.session.commit()
            flash(f'You have bought an object', category='success')
        else:
            flash(f'You have got not enough money to buy an object', category='danger')
        return redirect(url_for('market_page'))
    elif request.method == 'GET':
        items = Item.query.filter_by(owner=None)
        owned_items = Item.query.filter_by(owner=current_user.id)
    return render_template('market.html', items=items, purchase_form=purchase_form, owned_items=owned_items)


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

@app.route('/add_items', methods=['POST', 'GET'])
def add_items_page():
    form = AddItemForm()
    if form.validate_on_submit():
        item = Item(name=form.name.data, price=form.price.data, barcode=form.barcode.data, description=form.description.data)
        if item:
            db.session.add(item)
            db.session.commit()
            flash('Item successfully added!', category='success')
            return redirect(url_for('market_page'))
    return render_template('add_item.html', form=form)
from flask import render_template
from market import app
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
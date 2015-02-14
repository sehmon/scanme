from flask import render_template, flash, redirect
from app import app, db
from models import Item 

@app.route("/")
@app.route("/index")
def hello():
    clothes = Item.query.all()
    return render_template('items.html', clothes = clothes)

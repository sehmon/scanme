from flask import render_template, flash, redirect
from app import app, db
from models import Item 
import requests
import bs4

@app.route("/")
@app.route("/index")
def hello():

    items = Item.query.all()
    for item in items:
        db.session.delete(item)
    db.session.commit()

    response = requests.get('http://www.urbanoutfitters.com/urban/catalog/search.jsp?q=red+shirt#/') 
    soup = bs4.BeautifulSoup(response.text)

    for link in soup.find_all('div', attrs={'class':'category-product'}):
        i = Item(store='This is some text') 
        db.session.add(i)

    db.session.commit() 
    
    clothes = Item.query.all()
    arrayLen = len(clothes)

    return render_template('items.html', clothes = clothes, arrayLen = arrayLen)

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

    response = requests.get('http://www.urbanoutfitters.com/urban/catalog/search.jsp?q=blue+shirt#/') 
    soup = bs4.BeautifulSoup(response.text)

    for link in soup.find_all('div', attrs={'class':'category-product'}):
        i = Item(desc = link.find("h2").get_text(),
                imgurl = link.find("img").get("src"),
                price = link.find("h3").get_text())
        db.session.add(i)

    db.session.commit() 
    
    clothes = Item.query.all()
    arrayLen = len(clothes)
    rows = arrayLen/4

    return render_template('items.html',
            clothes = clothes,
            arrayLen = arrayLen, rows = rows)

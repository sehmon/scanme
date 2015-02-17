from flask import render_template, flash, redirect
from app import app, db
from models import Item 
import requests
import bs4

# The home template, will later change to the search function

@app.route("/")
@app.route("/index")
def hello():

# Clear the Database before returning the new search to the User
    items = Item.query.all()
    for item in items:
        db.session.delete(item)
    db.session.commit()

# Load the website for Beautiful Soup
    response = requests.get('http://www.urbanoutfitters.com/urban/catalog/search.jsp?q=blue+shirt#/') 
    soup = bs4.BeautifulSoup(response.text)

# For each link in the soup that matches "category-product" create a new Item and store it in the database
    for link in soup.find_all('div', attrs={'class':'category-product'}):
        i = Item(desc = link.find("h2").get_text(),
                imgurl = link.find("img").get("src"),
                price = link.find("h3").get_text())
        db.session.add(i)

    db.session.commit() 
   
# Create array of clothing Items, as well as the length of the items, and the number of Rows to display
# Assuming you have 4 items per row
    clothes = Item.query.all()
    arrayLen = len(clothes)
    rows = arrayLen/4

    return render_template('items.html',
            clothes = clothes,
            arrayLen = arrayLen, rows = rows)

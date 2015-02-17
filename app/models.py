from app import db

# The class model for each clothing item you return to the user

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(240), index=True, unique=True) 
    imgurl = db.Column(db.String(240), index=True, unique=True) 
    store = db.Column(db.String(60), index=True) 
    price = db.Column(db.String(60), index=True)
    desc = db.Column(db.String(100))

    def __repr__(self):
        return '<%r>' % (self.desc)

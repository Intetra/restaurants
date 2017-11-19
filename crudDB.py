from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('postgresql:///restaurantmenu')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()
session.commit()

def getRestaurants():
    z = []
    y = session.query(Restaurant).all()
    for x in y:
            z.append(x.name)
    return z






"""
myFirstRestaurant = Restaurant(name = "Pizza Palace")
session.add(myFirstRestaurant)
session.commit()
session.query(Restaurant).all()
firstResult = session.query(Restaurant).first()
firstResult.name
cheesepizza = MenuItem(name = "Cheese Pizza", description = "Made with cheese",
course = "Entree", price = "$8.99", restaurant = myFirstRestaurant)
session.add(cheesepizza)
session.commit()
"""

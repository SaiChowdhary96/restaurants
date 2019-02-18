from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Restaurant, Base, MenuItem, User

engine = create_engine('sqlite:///restaurantmenu.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create a dummy user
User1 = User(name="Sai Rapz", email="sairapz15@gmail.com",
             picture='https://o.aolcdn.com/images/dims3/GLOB/legacy_thumbnail/1200x630/format/jpg/quality/85/http%3A%2F%2Fi.huffpost.com%2Fgen%2F5334782%2Fimages%2Fn-TWIN-BABY-628x314.jpg')
session.add(User1)
session.commit()

# Menu for UrbanBurger
restaurant1 = Restaurant(user_id=1, name="Urban Burger")

session.add(restaurant1)
session.commit()

menuItem1 = MenuItem(user_id=1,name="Veggie Burger", item_type="Veg",
                     price="$7.50", restaurant_id=1, restaurant=restaurant1)

session.add(menuItem1)
session.commit()


menuItem2 = MenuItem(user_id=1,name="French Fries", item_type="Veg",
                     price="$2.99", restaurant_id=1, restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1,name="Chicken Burger", item_type="Non-Veg",
                     price="$5.50", restaurant_id=1, restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1,name="Chocolate Cake", item_type="Veg",
                     price="$3.99", restaurant_id=1, restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1,name="Sirloin Burger", item_type="Veg",
                     price="$7.99", restaurant_id=1, restaurant=restaurant1)

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(user_id=1,name="Root Beer", item_type="Beverage",
                     price="$1.99", restaurant_id=1, restaurant=restaurant1)

session.add(menuItem6)
session.commit()

menuItem7 = MenuItem(user_id=1,name="Iced Tea", item_type="Beverage",
                     price="$.99", restaurant_id=1, restaurant=restaurant1)

session.add(menuItem7)
session.commit()

menuItem8 = MenuItem(user_id=1,name="Grilled Cheese Sandwich", item_type="Veg",
                     price="$3.49", restaurant_id=1, restaurant=restaurant1)

session.add(menuItem8)
session.commit()



# Menu for Super Stir Fry
restaurant2 = Restaurant(user_id=1,name="Super Stir Fry")

session.add(restaurant2)
session.commit()


menuItem1 = MenuItem(user_id=1,name="Chicken Stir Fry", item_type="Non-Veg",
                     price="$7.99", restaurant_id=2, restaurant=restaurant2)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1,name="Peking Duck", item_type="Non-Veg", price="$25", restaurant_id=2, restaurant=restaurant2)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1,name="Spicy Tuna Roll", item_type="Non-Veg",
                     price="15", restaurant_id=2, restaurant=restaurant2)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1,name="Nepali Momo ", item_type="Veg",
                     price="12", restaurant_id=2, restaurant=restaurant2)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1,name="Beef Noodle Soup", item_type="Non-Veg",
                     price="14", restaurant_id=2, restaurant=restaurant2)

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(user_id=1,name="Ramen", item_type="Veg",
                     price="12", restaurant_id=2, restaurant=restaurant2)

session.add(menuItem6)
session.commit()

# Menu for Panda Garden
restaurant3 = Restaurant(user_id=1,name="Panda Garden")

session.add(restaurant3)
session.commit()


menuItem1 = MenuItem(user_id=1,name="Pho", item_type="Veg",
                     price="$8.99", restaurant_id=3, restaurant=restaurant3)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1,name="Chinese Dumplings", item_type="Veg",
                     price="$6.99", restaurant_id=3, restaurant=restaurant3)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1,name="Gyoza", item_type="Veg",
                     price="$9.95", restaurant_id=3, restaurant=restaurant3)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1,name="Stinky Tofu", item_type="Veg",
                     price="$6.99", restaurant_id=3, restaurant=restaurant3)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1,name="Veggie Burger", item_type="Veg",
                     price="$9.50", restaurant_id=3, restaurant=restaurant3)

session.add(menuItem5)
session.commit()


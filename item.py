from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Categories, User, Base, Item

engine = create_engine('sqlite:///catalogsusers.db')
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

User1 = User(name="Sidharth Dugar", email="sidharthdugar1998@gmail.com",
             picture='https://pbs.twimg.com/profile_images/2671170543'
             '/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

category1 = Categories(user_id=1, name="Skating")
session.add(category1)
session.commit()

item1 = Item(name="Roller Skates", description="Roller skates are shoes,"
             " or bindings that fit onto shoes, that are"
             " worn to enable the wearer to roll along on wheels."
             " The first roller skate was effectively an "
             "ice skate with wheels replacing the blade.", category=category1,
             user_id=1)

session.add(item1)
session.commit()

item2 = Item(name="Helmet", description="A helmet is an object which protects"
             " a persons head while they are skating.", category=category1,
             user_id=1)

session.add(item2)
session.commit()

category2 = Categories(user_id=1, name="Basketball")
session.add(category2)
session.commit()

item1 = Item(name="Basketball", description="Basketball is a team sport."
             " Two teams of five players each try to score by shooting a"
             " ball through a hoop elevated 10 feet above the ground."
             " The game is played on a rectangular floor called the court,"
             " and there is a hoop at each end.", category=category2,
             user_id=1)

session.add(item1)
session.commit()

category3 = Categories(user_id=1, name="Snowboarding")
session.add(category3)
session.commit()

item1 = Item(name="Snowboard", description="Best for any terrain and"
             " conditions.All mountain snowboards perform any where on a"
             " mountain-groomed runs, backcountry even park and pipe. "
             "Most boarders ride all mountain boards.", category=category3,
             user_id=1)

session.add(item1)
session.commit()

item2 = Item(name="Goggles", description="Goggles or safety glasses are"
             " forms of protective eyewear that usually enclose or protect"
             "the area surrounding the eye in order to prevent particulates, "
             "water or chemicals from striking the eyes.", category=category3,
             user_id=1)

session.add(item2)
session.commit()

print("Items added!!")

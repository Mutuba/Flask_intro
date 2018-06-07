from project import db
from project.models import User

# insert user data
db.session.add(User("Dan", "danielmutubait@gmail.com", "baraka"))
#db.session.add(User(Diana, dianajerop@gmail.com, truesecret))
#db.session.add(User(Ken, kenmigoma@gmail.com, secret))

db.session.commit()

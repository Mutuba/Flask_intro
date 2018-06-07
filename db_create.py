from project import db
from project.models import BlogPost, User

# create the database and the db table
db.create_all()

# insert data
db.session.add(BlogPost("Good", "I\'m good."))
db.session.add(BlogPost("Well", "I\'m well."))
db.session.add(BlogPost("Excellent", "I\'m excellent."))
db.session.add(BlogPost("Okay", "Had a wonderful day today"))
db.session.add(BlogPost("postgres", "we setup a local postgres instance"))
db.session.add(User("admin", "admin@gmail.com", "admin"))
#db.session.update(BlogPost(author_id = 1))

# commit the changes
db.session.commit()

from app import db



# Your database models should go here.
# Check out the Flask-SQLAlchemy quickstart for some good docs!
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/


class userInClub(db.Model):
    userKey = db.Column(db.Integer, nullable= False)
    clubCode = db.Column(db.Integer, nullable= False)

class userInEvent(db.Model):
    userKey = db.Column(db.Integer, nullable= False)
    eventId = db.Column(db.Integer, nullable= False)

class Club(db.Model):
    code = db.Column(db.String, primary_key=True)
    clubname = db.Column(db.String, unique= True, nullable= False)
    description = db.Column(db.String)
    tags = db.Column(db.String)

class Events(db.Model):
    id = db.Column(db.String, primary_key=True)
    eventname = db.Column(db.String, nullable= False)
    description = db.Column(db.String)
    location = db.Column(db.String)

class User(db.Model):
    id = db.Column(db.String, primary_key=True)
    username = db.Column(db.String, unique= True, nullable= False)
    password = db.Column(db.String, unique= True, nullable= False)
    graduation = db.Column(db.Integer)
    school = db.Column(db.String)
    major = db.Column(db.String)





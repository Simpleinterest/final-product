import os, json

from app import app, db, DB_FILE

from models import *



def create_club(co, name, desc, tag):
    #Make a club "object" using the inputted parameters
    club = Club(code = co, clubname = name, description = desc, tags = tag)

    #Add the new club "object" to the databse 
    db.session.add(club)

    #Runs the SQL commands
    db.session.commit()
    return club

    #Same logic as create-club
def create_event(id, name, desc, lo):
    event = Events(id = id, eventname = name, description = desc, location = lo)
    db.session.add(event)
    db.session.commit()
    return event

#Same logic as create_club
def create_user(user, passw, grad, scho, maj):
    user = User(username = user, password = passw, graduation = grad, school = scho, major = maj)
    db.session.add(user)
    db.session.commit()
    return user





def load_data(json_file = "clubs.json"):

    with open(json_file) as file:
        club = json.load(file)
    
    
    for v in club:
        code = v["code"]
        name = v["name"]
        description = v["description"]
        tags = ",".join(v["tags"])

        create_club(code, name, description, tags)



# No need to modify the below code.
if __name__ == "__main__":
    # Delete any existing database before bootstrapping a new one.
    LOCAL_DB_FILE = "instance/" + DB_FILE
    if os.path.exists(LOCAL_DB_FILE):
        os.remove(LOCAL_DB_FILE)

    with app.app_context():
        db.create_all()
        create_user()
        load_data()

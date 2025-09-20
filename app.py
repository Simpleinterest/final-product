from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 

DB_FILE = "clubreview.db"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_FILE}"
db = SQLAlchemy(app)

from models import *
from bootstrap import *

@app.route("/")
def main():
    return "Welcome to Penn Club Review!"

@app.route("/api/clubs", methods=["GET"])
def get_AllClubs():
    clubs = Club.query.all()
    allClubs = [         
        {
                "code": v.code,
                "name": v.clubname,
                "description": v.description,
                "tags": v.tags.split(",")
        }
        for v in clubs
    ]
    return jsonify(allClubs)


@app.route("/api/clubs/<string:code>", methods=["GET"])
def get_club(code):
    club = Club.query.get(code)
    if club == None:
        return jsonify({"N/A": "Club not found"})
    
    foundClub = {
        "code": club.code,
        "name": club.clubname,
        "description": club.description,
        "tags": club.tags.split(",") if club.tags else []
    }

    return jsonify(foundClub)

@app.route("/api/clubs/<string:code>", methods=["GET"])
def get_username(username):
    user = User.query.get(username)
    if user == None:
        return jsonify({"N/A": "User not found"})
    
    foundUser = {
        "username": user.code,
        "password": user.clubname,
        "graduation": user.description,
        "school": user.school,
        "major": user.major
    }

    return jsonify(foundUser)

@app.route("/api/clubs", methods=["POST"])
def create_club_api():
    data = request.get_json()

    create_club(data["code"], data["clubname"], data["description"], ",".join(data["tags"]))

@app.route("/api/clubs", methods=["PUT"])
def modify_club(code):
    club = Club.query.get(code)
    data = request.get_json()

    if "clubname" in data:
        club.clubname = data["clubname"]
    if "description" in data:
        club.description = data["description"]
    if "tags" in data:
        club.tags = ",".join(data["tags"])

    db.session.commit()

@app.route("/api/tags", methods=["GET"])
def get_ClubTags():
    clubs = Club.query.all()
    tagCount = {}

    for v in clubs:
        for tag in v.tags.split(","):
            tagCount[tag] = tagCount.get(tag, 0) + 1

    return jsonify(tagCount)

#Could not fully figure out how to do the favorite function
#def favorite_club(code):
#   data = request.get_json()
#   username = data.get("username")

#Event API Routing

@app.route("/api/events", methods=["PUT"])
def modify_event(id):
    event= Events.query.get(id)
    data = request.get_json()

    if "eventname" in data:
        event.clubname = data["eventname"]
    if "description" in data:
        event.description = data["description"]
    if "location" in data:
        event.tags = data["location"]

    db.session.commit()

@app.route("/api/events", methods=["POST"])
def create_event_api():
    data = request.get_json()

    create_event(data["id"], data["eventname"], data["description"], data["location"])

@app.route("/api/events", methods=["GET"])
def get_AllEvents():
    events = Events.query.all()
    allEvents = [         
        {
                "code": v.code,
                "name": v.clubname,
                "description": v.description,
                "tags": v.tags.split(",")
        }
        for v in events
    ]
    return jsonify(allEvents)

@app.route("/api")
def api():
    return jsonify({"message": "Welcome to the Penn Club Review API!."})


if __name__ == "__main__":
    app.run()

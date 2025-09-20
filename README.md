# Penn Labs Backend Challenge

## Documentation

Model.py:
--Created userinClub model for relationaltable between user and clubs to show which users are in which club
--Created userinEvent model for relationaltable between user and event to show which users are going to which event

--Created Clubs model to represent the different clubs, using codes to make each club unique for relational tables
--Created Event model to represent the different events held by different clubs
--Created Users model to represent the different users, gave it primary_key property for relational tables

Bootstrap.py:
--Made "create_club" function to create new clubs 
--Made "create_event" function to create new events
--Made "create_user" function to create new users

App.py:
--Created get_allClubs route with a "GET" in order to return json of all clubs in Club table
--Created get_club route with a "GET" in order to return json specific club using its unique code
--Created get_user route with a "GET" in order to return json specific username using its unique id
--Made create_club_api using the create_club function in bootstrap.py with a "POST"
--Made modify_club with a "PUT" in order to update specific club in table specifying the club by its unique code
--Made get_tags with a "GET" to get all the tags in each club, looped through each club and incremented value in a dictionary if tag key was found.

--Created get_allEvent route with a "GET" in order to return json of all events in Events table
--Created get_event route with a "GET" in order to return json specific event using its unique id
--Made create_event_api using the create_event function in bootstrap.py with a "POST"

Fill out this section as you complete the challenge!

## Installation

1. Click the green "use this template" button to make your own copy of this repository, and clone it. Make sure to create a **private repository**.
2. Change directory into the cloned repository.
3. Install `pipx`
   - `brew install pipx` (macOS)
   - See instructions here https://github.com/pypa/pipx for other operating systems
4. Install `poetry`
   - `pipx install poetry`
5. Install packages using `poetry install`.

## File Structure

- `app.py`: Main file. Has configuration and setup at the top. Add your [URL routes](https://flask.palletsprojects.com/en/1.1.x/quickstart/#routing) to this file!
- `models.py`: Model definitions for SQLAlchemy database models. Check out documentation on [declaring models](https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/) as well as the [SQLAlchemy quickstart](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#quickstart) for guidance
- `bootstrap.py`: Code for creating and populating your local database. You will be adding code in this file to load the provided `clubs.json` file into a database.

## Developing

0. Determine how to model the data contained within `clubs.json` and then complete `bootstrap.py`
1. Activate the Poetry shell with `poetry shell`.
2. Run `python3 bootstrap.py` to create the database and populate it.
3. Use `flask run` to run the project.
4. Follow the instructions [here](https://www.notion.so/pennlabs/Backend-Challenge-862656cb8b7048db95aaa4e2935b77e5).
5. Document your work in this `README.md` file.

## Submitting

Follow the instructions on the Technical Challenge page for submission.

## Installing Additional Packages

Use any tools you think are relevant to the challenge! To install additional packages
run `poetry add <package_name>` within the directory. Make sure to document your additions.

# Open-Ended Questions

## 1. I would use an html form login setting the type of the password input as "password" so that your password is hidden when its typed in. These forms would be sent to routes such as /logout, /login, etc. I would also hash the password before its put in its user table with the werkzeug.security package. In order to add sessions for the users so that they dont have to login every other second I would use the sessions that are already apart of Flask.

## 2. I would create a comments table in the database. this comments table would contain the user table "id" property which is a primary key to specify which user made the comment. I would also add the club table "code" property which is a primary key to specify which club the comment was made under. I would also add a "time" property to display when the comment was posted. An "additional_comments" property could also be added for nested comments which can have a list of other comments as its value 

## 3. I beleive the routes modify_club, get_username getclub_tabs, get_club, get_allclubs should be cached as those actions would be used daily. Other routes such as create_club would not be used as often as clubs have to go through a process of approval. In order to cambat invaldiation I would delete certain cache when data changes.

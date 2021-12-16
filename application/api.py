from application.app import app, db
from flask import request

# Import your models here
from application.models import Users, Groups, Pairs

@app.route("/")
def home():
    return {"Status": "Success"}, 200 

# Write your API endpoints here

# | Action        |               |                |                |          |         |
# |_______________|_______________|________________|________________|__________|_________|
# | Signin        |  Groups       |    POST        |     /groups    |  200     |   400   |
# | Sign up       |  Groups       |    POST        |     /groups    |  200     |   400   |
# | Add Name      |  Users        |    POST        |     /users     |  200     |   400   |
# | Delete Name   |  Users        |    DELETE      |   /users/id    |  200     |   400   |
# | Get Names     |  Users        |    GET         |     /users     |  200     |   400   |
# | Create Pairs  |  Pairs        |    POST        |/pairs/group_id |  200     |   400   |
# | Get Pairs     |  Pairs        |    GET         |     /pairs     |  200     |   400   | 


@app.route("/users", methods=["POST"])
def add_name():
    #username, group_id
    params = request.json
    users = Users(username = params["username"])
    db.session.add(users)
    db.session.commit()
    return {"id": users.id, "username": users.username, "group_id": users.group_id}

@app.route("/users/<int:id>", methods=["DELETE"])
def delete_name(id):
    users = Users.query.get(id)
    db.session.delete(users)
    db.session.commit()
    return{"Status":"Success", "message":"Book deleted"}

@app.route("/users", methods=["GET"])
def get_names():
    users = Users.query.filter_by().all()
    
    results = []
    
    for user in users:
        results.append({"id": user.id, "username": user.username, "group_id": user.group_id})
    
    return {"data": results}


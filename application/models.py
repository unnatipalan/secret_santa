from application.app import app, db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # email = db.Column(db.String(80), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120))


# Table 1: Groups
# - Group_ID : Int (Primary Key)
# - Group_Name : String
# - Number_of_Users : Int
# - Created_date : Date
# - Is_SecretSanta_Assigned : Boolean

class Groups(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(150))
    number_of_users = db.Column(db.Integer)
    created_date = db.Column(db.Date)
    is_secretsanta_assigned = db.Column(db.Boolean)

# Table 2: Users
# - User_ID : Int (Primary Key)
# - Group_ID : Int (Foreign Key) 
# - User_Name : String

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'), nullable=True)
    username = db.Column(db.String(150))
    
# Table 3 - Pairs (Maybe)
# - User_ID : Int (Foreign Key)
# - Santee_User_ID : Relationship (Foreign Key)

class Pairs(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    santee_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False) 

# Sample for One-many and Many-Many relationship
# class WorkItem(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(80), nullable=False)
#     description = db.Column(db.String(120))

#     created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     shared_with = db.relationship('User', secondary=shared_with, lazy='subquery', backref=db.backref('user', lazy=True))

# shared_with = db.Table('shared_with',
#     db.Column('work_item_id', db.Integer, db.ForeignKey('work_item.id'), primary_key=True),
#     db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
# )

# Using the above sample write the DB models here



# create all tables and initialize app

db.create_all()
db.init_app(app)
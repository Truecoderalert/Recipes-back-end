from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re	# the regex module
# create a regular expression object that we'll use later   
r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

db = 'Recipes_schema'
class User:
    def __init__(self , data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        
        
        
        
    @classmethod
    def save(cls,data):
        query = 'INSERT INTO users (first_name, last_name,  email ,password) Values (%(first_name)s, %(last_name)s, %(email)s, %(password)s)'
        return connectToMySQL(db).query_db(query,data)
    



            
    @classmethod
    def get_by_email(cls,data):
            query = "SELECT * FROM users WHERE email = %(email)s;"
            result = connectToMySQL(db).query_db(query,data)
            # Didn't find a matching user
            if len(result) < 1:
                return False
            return cls(result[0])

    @staticmethod
    def validate_user(users):
        is_valid = True
        if len(users['first_name']) < 2 or len(users['first_name']) > 50 :
            flash("first_name must be between 1 and 21  characters.")
            is_valid = False
        if len(users['email']) < 2 or len(users['email']) > 50 :
            flash("Email must be in email format.")
            is_valid = False
        if len(users['password']) < 1:
            flash("Please enter a password")
            is_valid = False
            
        return is_valid

    
db = 'Recipes_schema'
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.models_user import User


class Recipe:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.created_at  = data ['created_at']
        self.updated_at = data ['updated_at']
        self.user_id = data['user_id']
    
    @classmethod
    def get_all(cls):
        query = """Select * from recipes 
        Join users ON users.id = recipes.user_id
        """
        results = connectToMySQL (db).query_db(query)
        users = []
        for user in results:
            recipe_user = cls(user)
            #line24 creating recipe user
            user_data = {
                'id':user['id'],
                'first_name' :user['first_name'],
                'last_name':user['last_name'],
                'email':user['email'],
                'password':user['password']
            }
            recipe_user.creator = User(user_data)
            users.append(recipe_user)
        return users
    
    
        
        
    @classmethod
    def create(cls , data):
        query = """Insert into recipes ( name   ,   description  ,   instructions , user_id ) 
        Values (%(name)s   ,   %(description)s  ,   %(instructions)s , %(user_id)s) 
        """
        return connectToMySQL (db).query_db(query , data)
    @classmethod
    def get_one( cls , data):
        query = 'select * from recipes where id = %(id)s'
        results = connectToMySQL(db).query_db(query,data)
        #results is all the information in the database plus the query and the data we passed in class creation
        recipes = []
        #created an empty list
        for recipe in results:
        #for every object in the list in this case recipe in results
            recipes.append(recipe)
        # add a recipe into the empty list
        return recipes
    #show me the list
    @classmethod
    def update(cls , data  ):
        query = 'update recipes set name = %(name)s , description = %(description)s  , instructions = %(instructions)s    where id = %(id)s;'
        return connectToMySQL(db).query_db(query , data)
    
    @classmethod
    def delete(cls,data):
        query = """delete  from recipes 
        Where id = %(id)s
        """
        
        return connectToMySQL(db).query_db(query , data)
    
    
    @staticmethod
    def validate_user(recipes):
        is_valid = True
        if len(recipes['name']) < 2 or len(users['name']) > 50 :
            flash("name must be between 1 and 21  characters.")
            is_valid = False
        if len(recipes['description']) < 2 or len(recipes['description']) > 50 :
            flash("description must be between 2 and 50 characters.")
            is_valid = False
        if len(recipes['instructions']) < 1:
            flash("please enter instructions")
            is_valid = False
            
        return is_valid
    

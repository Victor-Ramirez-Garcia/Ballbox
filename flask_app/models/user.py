from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ballbox
from flask import flash
import re

name_regex = re.compile(r"^[a-zA-Z ]{3,49}$")
email_regex = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,}$")


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_ballboxes = []
    
    @classmethod
    def create_user(cls, data):

        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"

        user_id = connectToMySQL('ballbox_schema').query_db(query, data)
        
        return user_id
    
    @classmethod
    def email_exist(cls, data):

        query = "SELECT email from users WHERE email = %(email)s;"

        result = connectToMySQL('ballbox_schema').query_db(query, data)
        
        return result

    @classmethod
    def specific_validation(cls, data, regex):
        is_valid = False
        
        for character in data['password']:
            if regex.match(character):
                is_valid = True        
                break
        
        if not is_valid:
            is_valid = False
            return is_valid
        
        return is_valid

    @classmethod
    def validate_registration(cls, data):

        is_valid = True

        if not name_regex.match(data['first_name']):
            is_valid = False
            flash("First name has to be all letters and is at least 3 characters.", "registration_error")
        
        if not name_regex.match(data['last_name']):
            is_valid = False
            flash("Last name has to be all letters and is at least 3 characters.", "registration_error")
        
        if not email_regex.match(data['email']) or len(data['email']) > 50:
            is_valid = False
            flash('Email address must have a valid email format.', "registration_error")
        elif User.email_exist(data):
            is_valid = False
            flash("This email address already exists in our database", "registration_error") 

        if data['confirm_password'] != data['password']:
            is_valid = False
            flash("Confirm Password does not match with Password", "registration_error")

        return is_valid
    
    @classmethod
    def get_user_by_email(cls, data):

        query = "SELECT * FROM users WHERE email = %(email)s;"

        result = connectToMySQL('ballbox_schema').query_db(query, data)

        if not result:
            return result

        return User(result[0])

    @classmethod
    def validate_login(cls, data, bcrypt):
        
        is_valid = True

        user = User.get_user_by_email(data)
        
        if not user:
            is_valid = False
            flash("Invalid Email Address/Password", "login_error")
        elif not bcrypt.check_password_hash(user.password, data['password']):
            is_valid = False
            flash("Incorrect Password", "login_error")

        return is_valid
    
    @classmethod
    def get_user_by_id(cls, data):

        query = "SELECT * FROM users LEFT JOIN boxes ON users.id = boxes.user_id WHERE users.id = %(user_id)s;"

        results = connectToMySQL('ballbox_schema').query_db(query, data)

        user = User(results[0])

        for row in results:
            if row['boxes.id'] == None:
                break
            
            data = {
                'id': row['boxes.id'],
                'title': row['title'],
                'box_height': row['box_height'],
                'box_width': row['box_width'],
                'box_background_color': row['box_background_color'],
                'box_gradient': row['box_gradient'],
                'box_border_width': row['box_border_width'],
                'box_radius': row['box_radius'],
                'box_border_color': row['box_border_color'],
                'ball_amount': row['ball_amount'],
                'ball_size': row['ball_size'],
                'ball_background_color': row['ball_background_color'],
                'ball_gradient': row['ball_gradient'],
                'ball_border_width': row['ball_border_width'],
                'ball_border_color': row['ball_border_color'],
                'created_at': row['boxes.created_at'],
                'updated_at': row['boxes.updated_at']
            }

            user.user_ballboxes.append(ballbox.Ballbox(data))
        
        return user
    
    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users;"

        results = connectToMySQL('ballbox_schema').query_db(query)

        users = []

        for row in results:
            users.append(User(row))
        
        return results
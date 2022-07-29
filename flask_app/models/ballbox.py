from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask import flash
import re

class Ballbox:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.box_height = data['box_height']
        self.box_width = data['box_width']
        self.box_background_color = data['box_background_color']
        self.box_gradient = data['box_gradient']
        self.box_border_width = data['box_border_width']
        self.box_radius = data['box_radius']
        self.box_border_color = data['box_border_color']
        self.ball_amount = data['ball_amount']
        self.ball_size = data['ball_size']
        self.ball_background_color = data['ball_background_color']
        self.ball_gradient = data['ball_gradient']
        self.ball_border_width = data['ball_border_width']
        self.ball_border_color = data['ball_border_color']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ballbox_creator = []
    
    @classmethod
    def create_ballbox(cls, data):

        query = "INSERT INTO boxes (title, box_height, box_width, box_background_color, box_gradient, box_border_width, box_radius, box_border_color, ball_amount, ball_size, ball_background_color, ball_gradient, ball_border_width, ball_border_color, user_id) VALUES (%(title)s, %(box_height)s, %(box_width)s, %(box_background_color)s, %(box_gradient)s, %(box_border_width)s, %(box_radius)s, %(box_border_color)s, %(ball_amount)s, %(ball_size)s, %(ball_background_color)s, %(ball_gradient)s, %(ball_border_width)s, %(ball_border_color)s, %(user_id)s);"

        connectToMySQL('ballbox_schema').query_db(query, data)
    
    @classmethod
    def get_ballbox_by_id(cls, data):

        query = "SELECT * FROM boxes LEFT JOIN users ON boxes.user_id = users.id WHERE boxes.id = %(box_id)s;"

        results = connectToMySQL('ballbox_schema').query_db(query, data)

        ballbox = Ballbox(results[0])

        for row in results:
            if row['users.id'] == None:
                break

            data = {
                "id": row['users.id'],
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "email": row['email'],
                "password": row['password'],
                "created_at": row['users.created_at'],
                "updated_at": row['users.updated_at']
            }
        
            ballbox.ballbox_creator.append(user.User(data))
        
        return ballbox
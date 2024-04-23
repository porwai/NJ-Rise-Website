import os
from dotenv import load_dotenv
import sqlalchemy
from typing import List
from sqlalchemy import update

# Add Flask-Login attributes to user db class
from flask_login import UserMixin

from sqlalchemy.ext.declarative import declarative_base

load_dotenv()

_DATABASE_URL = os.getenv("DATABASE_URL")
_DATABASE_URL = _DATABASE_URL.replace("postgres://", "postgresql://")

_engine = sqlalchemy.create_engine(_DATABASE_URL)
Base = declarative_base()


class user_client(UserMixin, Base):
    __tablename__ = "users"
    username = sqlalchemy.Column(sqlalchemy.String, primary_key= True)
    password = sqlalchemy.Column(sqlalchemy.String)
    user_role = sqlalchemy.Column(sqlalchemy.String)
    
def check_user (username: str, password: str):
    # SQL QUERY SCHEMA
    '''
    SELECT * 
    From user_client
    WHERE user_client.username = {username}
    AND user_client.password = {password}
    '''
    print("check inputs:", username, password)
    
    with sqlalchemy.orm.Session(_engine) as session:
        if username != "":
            # query = session.query(user_client).filter(user_client.username == username, user_client.password == password).first()
            query = session.query(user_client).filter(user_client.username.like(username), user_client.password.like(password)).first()

            # Check if the query was found
            if query:
                print("CHECK DICT:", query.username)
                return query.user_role
            
            return "not_authorized"
        
def add_new_user(username: str, password: str, user_role: str):


    # Do not allow entry of new user that is empty or non-string value
    if type(username) != str or type(password) != str or type(user_role) != str:
        return False
    if username is "" or password is "" or user_role is "":
        return False
    
    # Create a new user instance
    new_user = user_client(username=username, password=password, user_role=user_role)
    # Create a session
    with sqlalchemy.orm.Session(_engine) as session:
        try:
            # Add the new user to the session
            session.add(new_user)
            # Commit the transaction
            session.commit()
            print("User added successfully.")
            return True
        except Exception as e:
            # Rollback the transaction if an error occurs
            session.rollback()
            print(f"Error occurred while adding user: {e}")
            return False
        
def read_all_users():
    # Create a session
    with sqlalchemy.orm.Session(_engine) as session:
        # query = session.query(user_client)
        users = session.query(user_client).all()
        user_list = []

        if users == []:
            return False, []
        
        for user in users:
            user_dict = {
                "username": user.username,
                "password": user.password,
                "user_role": user.user_role
            }
            user_list.append(user_dict)
        return True, user_list

    
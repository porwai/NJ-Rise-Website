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
            
            return "no_role"
 
#  callback for flask login get_user function
def get_user(username: str):

    with sqlalchemy.orm.Session(_engine) as session:
        if username != "":

            query = session.query(user_client).filter(user_client.username.like(username)).first()

            # Check if the query was found
            if query:
                print("CHECK DICT:", query.username)
                return query
            
            return None
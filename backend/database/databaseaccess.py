import os
from dotenv import load_dotenv
import sqlalchemy
from typing import List
from sqlalchemy import update
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()

_DATABASE_URL = os.getenv("DATABASE_URL")
_DATABASE_URL = _DATABASE_URL.replace("postgres://", "postgresql://")

_engine = sqlalchemy.create_engine(_DATABASE_URL)
Base = declarative_base()

class t_client(Base):
    __tablename__ = "transactional_db"
    first_name = sqlalchemy.Column(sqlalchemy.String)
    last_name = sqlalchemy.Column(sqlalchemy.String)
    phone = sqlalchemy.Column(sqlalchemy.String)
    dob = sqlalchemy.Column(sqlalchemy.String)
    client_type = sqlalchemy.Column(sqlalchemy.String)
    client_id = sqlalchemy.Column(sqlalchemy.String)

    # PRIMARY KEY to identify instances in transactional_db table
    transactional_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key= True, autoincrement=True)

class t_history(Base):
    __tablename__ = "transactional_history"
    t_id = sqlalchemy.Column(sqlalchemy.Integer)

    visit_date = sqlalchemy.Column(sqlalchemy.Date)
    food_bags = sqlalchemy.Column(sqlalchemy.Integer)
    baby_supplies = sqlalchemy.Column(sqlalchemy.Integer)
    pet_food = sqlalchemy.Column(sqlalchemy.Integer)
    gift_items = sqlalchemy.Column(sqlalchemy.Integer)
    cleaning = sqlalchemy.Column(sqlalchemy.Integer)
    personal_care = sqlalchemy.Column(sqlalchemy.Integer)
    summer_feeding = sqlalchemy.Column(sqlalchemy.Integer)
    pj = sqlalchemy.Column(sqlalchemy.Integer)
    winter = sqlalchemy.Column(sqlalchemy.Integer)
    clothing = sqlalchemy.Column(sqlalchemy.Integer)
    other = sqlalchemy.Column(sqlalchemy.Integer)
    
    # PRIMARY KEY to identify instances in transactional_history table
    visit_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key= True, autoincrement=True)
    
def get_client (client_id: str, first_name: str, last_name: str, phone: str, dob: str):
    # SQL QUERY SCHEMA
    '''
    SELECT * 
    From t_client
    WHERE t_client.client_id = {client_id}
    AND
    t_client.first_name = {first_name}
    AND
    t_client.last_name = {last_name}
    AND
    t_client.phone = {phone}
    AND 
    t_client.dob = {dob}
    '''
    
    with sqlalchemy.orm.Session(_engine) as session:
        if client_id != "":
            client_id = "%" + client_id + "%"
            query = session.query(t_client).filter(t_client.client_id.like(client_id))
        else:
            
            first_name = "%" + first_name + "%"
            last_name = "%" + last_name + "%"
            phone = "%" + phone + "%"
            dob = "%" + dob + "%"
            query = session.query(t_client).filter(t_client.first_name.ilike(first_name), t_client.last_name.ilike(last_name), t_client.dob.like(dob), t_client.phone.like(phone))        
    res = []
    for u in query.all():
        u = u.__dict__
        del u["_sa_instance_state"]
        res.append(u)
    return res

# Update Special items or visit_date_list
def update_client (transactional_id: int, new_visit_date: str, f_bags=0, b_supplies=0, p_food=0, g_items=0, c=0, 
                   p_care=0, sf = 0, p=0, cloth=0, w=0, o=0):
    # SQL Query SCHEMA
    '''
    UPDATE transactional_db
    SET visit_date_list = {new appended list}
    SET special_item_list = {special_item_list}
    WHERE transactional_id = {transactional_id}
    '''

    with sqlalchemy.orm.Session(_engine) as session:

        # Select current visit_date_list
        date_format = '%Y-%m-%d'
        date_obj = datetime.strptime(new_visit_date, date_format)
        new_visit = t_history(t_id=transactional_id, visit_date=date_obj, food_bags=f_bags, baby_supplies=b_supplies,pet_food=p_food,
                              gift_items=g_items, cleaning=c, personal_care=p_care, summer_feeding = sf, pj=p, clothing = cloth, winter=w, other = o)
        session.add(new_visit)
        session.commit()
        

        # # Add new visit date
        # visit_date_list = query.all()[0]["visit_date_list"]
        # visit_date_list = visit_date_list.insert(0, new_visit_date)

        # # Update database value for visit_date_list
        # u = update(t_client)
        # u = u.values({
        #     "visit_date_list": visit_date_list,
        #     "special_item_list": special_item_list,
        # })
        # u = u.where(t_client.c.transactional_id == transactional_id)

        # # Execute changes
        # _engine.execute(u)


# Delete client from database
def delete_client (transactional_id: int):

    with sqlalchemy.orm.Session(_engine) as session:

        # Select relevant row
        x = session.query(t_client).filter(t_client.transactional_id == transactional_id)

        # Delete and commit
        session.delete(x)
        session.commit()    

def add_client (f_name: str, l_name:str, p: str, dob_date: str, date:str, foodbags: int):
    id = 0
    with sqlalchemy.orm.Session(_engine) as session:
        if f_name is None:
            f_name = ''
        if l_name is None:
            l_name = ''
        if p is None:
            p = ''
        if dob_date is None:
            dob_date = ''
        # Select relevant row
        new_client = t_client(first_name=f_name, last_name=l_name, phone=p, dob=dob_date)
        session.add(new_client)
        session.commit()

        
 
        



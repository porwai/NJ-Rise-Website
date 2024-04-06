import os
from dotenv import load_dotenv
import sqlalchemy
from typing import List
from sqlalchemy import update

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
    visit_date_list = sqlalchemy.Column(sqlalchemy.ARRAY(sqlalchemy.String))
    special_item_list = sqlalchemy.Column(sqlalchemy.ARRAY(sqlalchemy.String))

    # PRIMARY KEY to identify instances in transactional_db table
    transactional_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key= True, autoincrement=True)
    
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
            query = session.query(t_client).filter(t_client.first_name.like(first_name), t_client.last_name.like(last_name), t_client.dob.like(dob), t_client.phone.like(phone))
             
    res = []
    for u in query.all():
        u = u.__dict__
        del u["_sa_instance_state"]
        res.append(u)
        
    return res

# Update Special items or visit_date_list
def update_client (transactional_id: int, new_visit_date: str, special_item_list: List[str]):
    # SQL Query SCHEMA
    '''
    UPDATE transactional_db
    SET visit_date_list = {new appended list}
    SET special_item_list = {special_item_list}
    WHERE transactional_id = {transactional_id}
    '''

    with sqlalchemy.orm.Session(_engine) as session:

        # Select current visit_date_list
        query = session.query(t_client).filter(t_client.transactional_id == transactional_id)
        query = query.one()
        visit_date_copy = list(query.visit_date_list)
        visit_date_copy.append(new_visit_date)
        query.visit_date_list = visit_date_copy
        query = session.query(t_client).filter(t_client.transactional_id == transactional_id)
        query = query.one()
        query.special_item_list = special_item_list
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
def add_client (c_type: str, f_name: str, l_name:str, p: str, dob: str, v_d_l: str):
    with sqlalchemy.orm.Session(_engine) as session:
        if c_type is None:
            c_type = ''
        if f_name is None:
            f_name = ''
        if l_name is None:
            l_name = ''
        if p is None:
            p = ''
        if dob is None:
            dob = ''
        if v_d_l is None:
            v_d_l = ''
        visit_history = [v_d_l]
        # Select relevant row
        new_client = t_client(client_type=c_type, first_name=f_name, last_name=l_name, phone=p, DOB=dob, visit_date_list = visit_history)
        session.add(new_client)
        session.commit()

        
 
        



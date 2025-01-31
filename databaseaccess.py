import os
from dotenv import load_dotenv
import sqlalchemy
from collections import OrderedDict
from typing import List
import codecs
import csv
from sqlalchemy import update, MetaData, func
from sqlalchemy.sql import extract
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
import calendar

load_dotenv()

_DATABASE_URL = os.getenv("DATABASE_URL")
_DATABASE_URL = _DATABASE_URL.replace("postgres://", "postgresql://")

_engine = sqlalchemy.create_engine(_DATABASE_URL)
Base = declarative_base()

class t_master_db(Base):
    __tablename__ = "master_db"

    client_id = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    last_name = sqlalchemy.Column(sqlalchemy.String)
    first_name = sqlalchemy.Column(sqlalchemy.String)
    middle_initial = sqlalchemy.Column(sqlalchemy.String)
    total_family_members = sqlalchemy.Column(sqlalchemy.Integer)
    case_manager_initials = sqlalchemy.Column(sqlalchemy.String)
    client_type = sqlalchemy.Column(sqlalchemy.String)
    renewal_date = sqlalchemy.Column(sqlalchemy.String)
    gender_head_of_household = sqlalchemy.Column(sqlalchemy.String)
    head_of_household_date_of_birth = sqlalchemy.Column(sqlalchemy.Date)
    household_number_of_adults = sqlalchemy.Column(sqlalchemy.Integer)
    household_number_of_children = sqlalchemy.Column(sqlalchemy.Integer)
    household_number_of_children_under_18 = sqlalchemy.Column(sqlalchemy.Integer)
    additional_family_members_first_name = sqlalchemy.Column(sqlalchemy.String)
    additional_family_members_last_name = sqlalchemy.Column(sqlalchemy.String)
    additional_family_member_middle_initial = sqlalchemy.Column(sqlalchemy.String)
    additional_family_members_date_of_birth = sqlalchemy.Column(sqlalchemy.String)
    city = sqlalchemy.Column(sqlalchemy.String)
    state = sqlalchemy.Column(sqlalchemy.String)
    zip_code = sqlalchemy.Column(sqlalchemy.String)
    country_of_origin = sqlalchemy.Column(sqlalchemy.String)
    residence_hightstown = sqlalchemy.Column(sqlalchemy.Integer)
    residence_east_windsor = sqlalchemy.Column(sqlalchemy.Integer)
    residence_cranbury = sqlalchemy.Column(sqlalchemy.Integer)
    residence_other = sqlalchemy.Column(sqlalchemy.Integer)
    housing_own = sqlalchemy.Column(sqlalchemy.Integer)
    housing_rent = sqlalchemy.Column(sqlalchemy.Integer)
    housing_other_permanent = sqlalchemy.Column(sqlalchemy.Integer)
    homeless = sqlalchemy.Column(sqlalchemy.Integer)
    date_file_opened = sqlalchemy.Column(sqlalchemy.String)
    renewal_return_date = sqlalchemy.Column(sqlalchemy.String)
    return_client = sqlalchemy.Column(sqlalchemy.Integer)
    new_client = sqlalchemy.Column(sqlalchemy.Integer)
    new_client_intake_date = sqlalchemy.Column(sqlalchemy.String)
    phone_number = sqlalchemy.Column(sqlalchemy.String)
    affected_by_covid = sqlalchemy.Column(sqlalchemy.Integer)
    household_single = sqlalchemy.Column(sqlalchemy.Integer)
    household_two_adults_no_children = sqlalchemy.Column(sqlalchemy.Integer)
    household_single_parent_female = sqlalchemy.Column(sqlalchemy.Integer)
    household_single_parent_male = sqlalchemy.Column(sqlalchemy.Integer)
    household_two_parent = sqlalchemy.Column(sqlalchemy.Integer)
    household_non_related_adults_no_children = sqlalchemy.Column(sqlalchemy.Integer)
    household_multi_generational = sqlalchemy.Column(sqlalchemy.Integer)
    household_other = sqlalchemy.Column(sqlalchemy.Integer)
    household_not_reported = sqlalchemy.Column(sqlalchemy.Integer)
    ethnicity_hispanic_latino = sqlalchemy.Column(sqlalchemy.Integer)
    ethnicity_non_hispanic_latino = sqlalchemy.Column(sqlalchemy.Integer)
    ethnicity_unknown = sqlalchemy.Column(sqlalchemy.Integer)
    ethnicity_american_indian = sqlalchemy.Column(sqlalchemy.Integer)
    ethnicity_alaska_native = sqlalchemy.Column(sqlalchemy.Integer)
    ethnicity_asian = sqlalchemy.Column(sqlalchemy.Integer)
    ethnicity_black_african = sqlalchemy.Column(sqlalchemy.Integer)
    ethnicity_white = sqlalchemy.Column(sqlalchemy.Integer)
    ethnicity_other =  sqlalchemy.Column(sqlalchemy.Integer)
    ethnicity_multi_race = sqlalchemy.Column(sqlalchemy.Integer)
    ethnicity_unknown_not_reported = sqlalchemy.Column(sqlalchemy.Integer)
    adults_in_household_female = sqlalchemy.Column(sqlalchemy.Integer)
    adults_in_household_pregnant_female = sqlalchemy.Column(sqlalchemy.Integer)
    adults_in_household_pregnant_due_date = sqlalchemy.Column(sqlalchemy.String)
    adults_in_household_male = sqlalchemy.Column(sqlalchemy.Integer)
    adults_in_household_other = sqlalchemy.Column(sqlalchemy.Integer)
    adults_in_household_unknown_not_reported = sqlalchemy.Column(sqlalchemy.Integer)
    adults_in_household_disabled = sqlalchemy.Column(sqlalchemy.Integer)
    adults_in_household_aged = sqlalchemy.Column(sqlalchemy.Integer)
    adults_in_household_veteran = sqlalchemy.Column(sqlalchemy.Integer)
    adults_in_household_veteran_active = sqlalchemy.Column(sqlalchemy.Integer)
    household_total_number_of_children = sqlalchemy.Column(sqlalchemy.Integer)
    household_total_number_of_female_children = sqlalchemy.Column(sqlalchemy.Integer)
    household_total_number_of_male_children = sqlalchemy.Column(sqlalchemy.Integer)
    household_total_number_of_disabled_children = sqlalchemy.Column(sqlalchemy.Integer)
    household_children_0_5_years_old = sqlalchemy.Column(sqlalchemy.Integer)
    household_children_6_13_years_old = sqlalchemy.Column(sqlalchemy.Integer)
    household_children_14_17_years_old = sqlalchemy.Column(sqlalchemy.Integer)
    education_9_12_grade_non_graduate = sqlalchemy.Column(sqlalchemy.Integer)
    education_graduate_or_equivalent_diploma = sqlalchemy.Column(sqlalchemy.Integer)
    education_12th_grade_and_some_post_secondary_school = sqlalchemy.Column(sqlalchemy.Integer)
    education_2_4_year_college_graduate = sqlalchemy.Column(sqlalchemy.Integer)
    education_graduate_and_post_secondary_school = sqlalchemy.Column(sqlalchemy.Integer)
    education_graduate_and_post_secondary_school_over_25_years_old = sqlalchemy.Column(sqlalchemy.Integer)
    annual_income = sqlalchemy.Column(sqlalchemy.String)
    full_time_employment = sqlalchemy.Column(sqlalchemy.Integer)
    part_time_employment = sqlalchemy.Column(sqlalchemy.Integer)
    migrant_or_seasonal_worker = sqlalchemy.Column(sqlalchemy.Integer)
    unemployed_short_term_6_months_or_less = sqlalchemy.Column(sqlalchemy.Integer)
    unemployed_long_term_over_6_months = sqlalchemy.Column(sqlalchemy.Integer)
    not_in_labor_force = sqlalchemy.Column(sqlalchemy.Integer)
    retired = sqlalchemy.Column(sqlalchemy.Integer)
    unknown_or_not_reported_employment = sqlalchemy.Column(sqlalchemy.Integer)
    obtained_job_through_rise = sqlalchemy.Column(sqlalchemy.Integer)
    poverty_guidelines_125 = sqlalchemy.Column(sqlalchemy.Integer)
    poverty_guidelines_185 = sqlalchemy.Column(sqlalchemy.Integer)
    poverty_guidelines_200 = sqlalchemy.Column(sqlalchemy.Integer)
    poverty_guidelines_over_200 = sqlalchemy.Column(sqlalchemy.Integer)
    total_family_receiving_fs_snap = sqlalchemy.Column(sqlalchemy.Integer)
    total_family_receiving_tanf = sqlalchemy.Column(sqlalchemy.Integer)
    total_family_receiving_alimony = sqlalchemy.Column(sqlalchemy.Integer)
    total_family_receiving_lheap = sqlalchemy.Column(sqlalchemy.Integer)
    total_family_receiving_ga = sqlalchemy.Column(sqlalchemy.Integer)
    total_family_receiving_medicaid_njfc = sqlalchemy.Column(sqlalchemy.Integer)
    total_family_receiving_child_support = sqlalchemy.Column(sqlalchemy.Integer)
    total_family_receiving_pension = sqlalchemy.Column(sqlalchemy.Integer)
    total_family_receiving_ssa = sqlalchemy.Column(sqlalchemy.Integer)
    total_family_receiving_ssi = sqlalchemy.Column(sqlalchemy.Integer)
    total_family_receiving_ssdi = sqlalchemy.Column(sqlalchemy.Integer)
    total_family_receiving_wic = sqlalchemy.Column(sqlalchemy.Integer)
    total_family_receiving_workers_comp = sqlalchemy.Column(sqlalchemy.Integer)
    total_family_receiving_temporary_disability = sqlalchemy.Column(sqlalchemy.Integer)
    total_family_receiving_unemployment = sqlalchemy.Column(sqlalchemy.Integer)

    transactional_id = sqlalchemy.Column(sqlalchemy.Integer)

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
    client_type = sqlalchemy.Column(sqlalchemy.String)

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

import_list = [
    ("client_id","string"),
    ("last_name","string"),
    ("first_name","string"),
    ("middle_initial","string"),
    ("total_family_members","int"),
    ("case_manager_initials","string"),
    ("client_type","string"),
    ("renewal_date","string"),
    ("gender_head_of_household","string"),
    ("head_of_household_date_of_birth","string"),
    ("household_number_of_adults","int"),
    ("household_number_of_children","int"),
    ("household_number_of_children_under_18","int"),
    ("additional_family_members_first_name","string"),
    ("additional_family_members_last_name","string"),
    ("additional_family_member_middle_initial","string"),
    ("additional_family_members_date_of_birth","string"),
    ("city","string"),
    ("state","string"),
    ("zip_code","string"),
    ("country_of_origin","string"),
    ("residence_hightstown","int"),
    ("residence_east_windsor","int"),
    ("residence_cranbury","int"),
    ("residence_other","int"),
    ("housing_own","int"),
    ("housing_rent","int"),
    ("housing_other_permanent","int"),
    ("homeless","int"),
    ("date_file_opened","string"),
    ("renewal_return_date","string"),
    ("return_client","int"),
    ("new_client","int"),
    ("new_client_intake_date","string"),
    ("phone_number","string"),
    ("affected_by_covid","int"),
    ("household_single","int"),
    ("household_two_adults_no_children","int"),
    ("household_single_parent_female","int"),
    ("household_single_parent_male","int"),
    ("household_two_parent","int"),
    ("household_non_related_adults_no_children","int"),
    ("household_multi_generational","int"),
    ("household_other","int"),
    ("household_not_reported","int"),
    ("ethnicity_hispanic_latino","int"),
    ("ethnicity_non_hispanic_latino","int"),
    ("ethnicity_unknown","int"),
    ("ethnicity_american_indian","int"),
    ("ethnicity_alaska_native","int"),
    ("ethnicity_asian","int"),
    ("ethnicity_black_african","int"),
    ("ethnicity_white","int"),
    ("ethnicity_other","int"),
    ("ethnicity_multi_race","int"),
    ("ethnicity_unknown_not_reported","int"),
    ("adults_in_household_female","int"),
    ("adults_in_household_pregnant_female","int"),
    ("adults_in_household_pregnant_due_date","string"),
    ("adults_in_household_male","int"),
    ("adults_in_household_other","int"),
    ("adults_in_household_unknown_not_reported","int"),
    ("adults_in_household_disabled","int"),
    ("adults_in_household_aged","int"),
    ("adults_in_household_veteran","int"),
    ("adults_in_household_veteran_active","int"),
    ("household_total_number_of_children","int"),
    ("household_total_number_of_female_children","int"),
    ("household_total_number_of_male_children","int"),
    ("household_total_number_of_disabled_children","int"),
    ("household_children_0_5_years_old","int"),
    ("household_children_6_13_years_old","int"),
    ("household_children_14_17_years_old","int"),
    ("education_9_12_grade_non_graduate","int"),
    ("education_graduate_or_equivalent_diploma","int"),
    ("education_12th_grade_and_some_post_secondary_school","int"),
    ("education_2_4_year_college_graduate","int"),
    ("education_graduate_and_post_secondary_school","int"),
    ("education_graduate_and_post_secondary_school_over_25_years_old","int"),
    ("annual_income","string"),
    ("full_time_employment","int"),
    ("part_time_employment","int"),
    ("migrant_or_seasonal_worker","int"),
    ("unemployed_short_term_6_months_or_less","int"),
    ("unemployed_long_term_over_6_months","int"),
    ("not_in_labor_force","int"),
    ("retired","int"),
    ("unknown_or_not_reported_employment","int"),
    ("obtained_job_through_rise","int"),
    ("poverty_guidelines_125","int"),
    ("poverty_guidelines_185","int"),
    ("poverty_guidelines_200","int"),
    ("poverty_guidelines_over_200","int"),
    ("total_family_receiving_fs_snap","int"),
    ("total_family_receiving_tanf","int"),
    ("total_family_receiving_alimony","int"),
    ("total_family_receiving_lheap","int"),
    ("total_family_receiving_ga","int"),
    ("total_family_receiving_medicaid_njfc","int"),
    ("total_family_receiving_child_support","int"),
    ("total_family_receiving_pension","int"),
    ("total_family_receiving_ssa","int"),
    ("total_family_receiving_ssi","int"),
    ("total_family_receiving_ssdi","int"),
    ("total_family_receiving_wic","int"),
    ("total_family_receiving_workers_comp","int"),
    ("total_family_receiving_temporary_disability","int"),
    (" total_family_receiving_unemployment","int")
]
def get_client (client_id: str, first_name: str, last_name: str, phone: str, month: str, day: str,year: str):
    
    with sqlalchemy.orm.Session(_engine) as session:
        query_id = "%" + client_id + "%"
        query_fname = "%" + first_name + "%"
        query_lname = "%" + last_name + "%"
        query_phone = "%" + phone + "%"
        if client_id != "":
            query  = session.query(t_client).filter(t_client.client_id.ilike(query_id),t_client.first_name.ilike(query_fname), t_client.last_name.ilike(query_lname), 
                                                    t_client.phone.like(query_phone))  
        else:
            query  = session.query(t_client).filter(t_client.first_name.ilike(query_fname), t_client.last_name.ilike(query_lname)
                                                   , t_client.phone.like(query_phone))  
        if month != "":
            if not month.isnumeric():
                return []
            query = query.filter(extract('month', t_client.dob) == month)
        if day != "":
            if not day.isnumeric():
                return []
            query = query.filter(extract('day', t_client.dob) == day)
        if year != "":
            if not year.isnumeric():
                return []
            query = query.filter(extract('year', t_client.dob) == year)

        query = query.order_by(t_client.client_id, t_client.first_name, t_client.last_name)      
        res = []
        for u in query.all():
            u = u.__dict__
            del u["_sa_instance_state"]
            u['dob'] = u['dob'].strftime("%Y-%m-%d")
            res.append(u)
        return res

def query_masterdb_client (client_id: str, first_name: str, last_name: str, phone: str, month: str, day: str,year: str):
    with sqlalchemy.orm.Session(_engine) as session:
        query_id = "%" + client_id + "%"
        query_fname = "%" + first_name + "%"
        query_lname = "%" + last_name + "%"
        query_phone = "%" + phone + "%"
        query = session.query(t_master_db).filter(
            t_master_db.client_id.ilike(query_id),
            t_master_db.first_name.ilike(query_fname),
            t_master_db.last_name.ilike(query_lname),
            t_master_db.phone_number.like(query_phone))
        if month != "":
            if not month.isnumeric():
                return []
            query = query.filter(extract('month', t_master_db.head_of_household_date_of_birth) == month)
        if day != "":
            if not day.isnumeric():
                return []
            query = query.filter(extract('day', t_master_db.head_of_household_date_of_birth) == day)
        if year != "":
            if not year.isnumeric():
                return []
            query = query.filter(extract('year', t_master_db.head_of_household_date_of_birth) == year)
        query = query.order_by(t_master_db.client_id, t_master_db.first_name, t_master_db.last_name)

        # Process results: convert SQLAlchemy objects to dictionaries
        res = []
        for item in query.all():
            # Using OrderedDict to maintain order of columns as defined in the class
            item_data = OrderedDict((col.name, getattr(item, col.name)) for col in item.__table__.columns)
            item_data['head_of_household_date_of_birth'] = item_data['head_of_household_date_of_birth'].strftime("%Y-%m-%d")
            res.append(item_data)
        return res

def edit_masterdb_client (client_id: str, updates: dict):
    with sqlalchemy.orm.Session(_engine) as session:
        try:
            t_client_updates = {
                "first_name": updates.get("first_name"),
                "last_name": updates.get("last_name"),
                "phone": updates.get("phone_number"),
                "dob": updates.get("head_of_household_date_of_birth"),
                "client_type": updates.get("client_type")
            }
        except Exception as e:
            raise RuntimeError(f"Missing fields")

        # Retrieve the client record by client_id
        client = session.query(t_master_db).filter_by(client_id=client_id).first()
        if client is None:
            raise ValueError(f"No client found in master_db with client_id {client_id}")

        # Fields that should not be edited
        immutable_fields = ['client_id']

        # Update the fields with the data provided in the updates dictionary
        for key, value in updates.items():
            if key in immutable_fields:
                raise ValueError(f"The field '{key}' is not editable.")
            if hasattr(client, key):
                setattr(client, key, value)
            else:
                raise ValueError(f"{key} is not a valid field of t_master_db")

        transactional_client = session.query(t_client).filter_by(client_id=client_id).first()

        # Update the fields with the data provided in the updates dictionary
        for key, value in t_client_updates.items():
            if key in immutable_fields:
                raise ValueError(f"The field '{key}' is not editable.")
            if hasattr(transactional_client, key):
                setattr(transactional_client, key, value)
            else:
                raise ValueError(f"{key} is not a valid field of t_master_db")

        # Attempt to commit changes to the database
        try:
            session.commit()
            print(f"Client {client_id} updated successfully.")
        except sqlalchemy.exc.SQLAlchemyError as e:
            session.rollback()  # Roll back the transaction if any database errors occurred
            raise RuntimeError(f"Failed to update client due to: {str(e)}")
def importCsv(file: str):
    stream = codecs.iterdecode(file.stream, 'utf-8')
    format = "%m/%d/%Y"
    count = 0
    with sqlalchemy.orm.Session(_engine) as session:
        for fields in csv.reader(stream, dialect=csv.excel):
            if count == 0:
                count = count + 1
                continue
            data = {}
            if len(fields) != 108:
                raise Exception("number of columns does not match up")
            for i in range(len(fields)):
                key = import_list[i][0].strip()
                data_value = import_list[i][1]
                value = fields[i]
                if (data_value == "int" and value == ""):
                    value = 0        
                elif (data_value == "int" and not value.strip().isnumeric()):
                    raise Exception("Column " + key + " is not an integer.")

                if (key == "head_of_household_date_of_birth"):
                    try:
                        value = datetime.strptime(value, format)
                    except ValueError:
                        raise Exception("Date column " + key + " is not in MM/DD/YYYY format")
                if (key == "client_type" and (value != "Empower" and value != "not eligible" and value != "TEFAP" and value != "Neighbor")):
                    raise Exception ("Client type is not valid")
                data[key] = value
            required_fields = {
                "first_name": "First Name is required",
                "last_name": "Last Name is required",
                "phone_number": "Phone Number is required",
                "head_of_household_date_of_birth": "Date of Birth for Head of Household is required",
                "client_id": "Client ID is missing",
                "client_type": "Client type is missing"
            }

            # Check for missing required fields
            for field, error_message in required_fields.items():
                if not data.get(field):
                    raise ValueError(error_message)
            try:
                # Create a new client object
                new_client = t_client(
                    first_name=data["first_name"],
                    last_name=data["last_name"],
                    phone=data["phone_number"],
                    dob=data["head_of_household_date_of_birth"],
                    client_id=data["client_id"],
                    client_type=data["client_type"]
                )

                # Add the new client to the session and flush to generate the transactional_id
                session.add(new_client)
                session.flush()  # This flushes the session to the database and populates new_client.transactional_id

                # Check if client_id already exists in the database
                existing_client = session.query(t_client).filter(t_client.client_id == data["client_id"]).first()
                if existing_client and existing_client != new_client:
                    raise ValueError("Client with this ID already exists")

                # Prepare and add master_db client object using the transactional_id from new_client
                data['transactional_id'] = new_client.transactional_id  # Set the transactional_id in the data dictionary
                new_masterdb_client = t_master_db(**data)
                session.add(new_masterdb_client)

            except Exception as e:
                session.rollback()  
                raise  
        try:
            session.commit()
        except Exception as e:
            session.rollback()
            raise

    


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
        if not isinstance(f_bags, int) or not isinstance(b_supplies, int) or not isinstance(p_food, int) or not isinstance(g_items, int):
            raise Exception("Please enter integer values")
        if not isinstance(c, int) or not isinstance(p_care, int) or not isinstance(sf, int) or not isinstance(p, int):
            raise Exception("Please enter integer values")
        if not isinstance(cloth, int) or not isinstance(w, int) or not isinstance(o, int):
            raise Exception("Please enter integer values")
        date_format = '%Y-%m-%d'
        c_type = session.query(t_client).filter(t_client.transactional_id==transactional_id).one().client_type
        date_obj = datetime.strptime(new_visit_date, date_format)
        new_visit = t_history(t_id=transactional_id, visit_date=date_obj, food_bags=f_bags, baby_supplies=b_supplies,pet_food=p_food,
                              gift_items=g_items, cleaning=c, personal_care=p_care, summer_feeding = sf, pj=p, clothing = cloth, winter=w, other = o, client_type=c_type)
        session.add(new_visit)
        try:
            session.commit()
        except sqlalchemy.exc.SQLAlchemyError as e:
            session.rollback()  # Roll back the transaction if any database errors occurred
            raise RuntimeError("A server error occured")
        return get_history(transactional_id)

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

def add_master_db_client(data: dict):
    required_fields = {
        "first_name": "First Name is required",
        "last_name": "Last Name is required",
        "phone_number": "Phone Number is required",
        "head_of_household_date_of_birth": "Date of Birth for Head of Household is required",
        "client_id": "Client ID is missing",
        "client_type": "Client type is missing"
    }

    # Check for missing required fields
    for field, error_message in required_fields.items():
        if not data.get(field):
            raise ValueError(error_message)

    with sqlalchemy.orm.Session(_engine) as session:
        try:
            # Create a new client object
            new_client = t_client(
                first_name=data["first_name"],
                last_name=data["last_name"],
                phone=data["phone_number"],
                dob=data["head_of_household_date_of_birth"],
                client_id=data["client_id"],
                client_type=data["client_type"]
            )

            # Add the new client to the session and flush to generate the transactional_id
            session.add(new_client)
            session.flush()  # This flushes the session to the database and populates new_client.transactional_id

            # Check if client_id already exists in the database
            existing_client = session.query(t_client).filter(t_client.client_id == data["client_id"]).first()
            if existing_client and existing_client != new_client:
                raise ValueError("Client with this ID already exists")

            # Prepare and add master_db client object using the transactional_id from new_client
            data['transactional_id'] = new_client.transactional_id  # Set the transactional_id in the data dictionary
            new_masterdb_client = t_master_db(**data)
            session.add(new_masterdb_client)

            # Commit all transactions if everything is valid
            session.commit()
            return new_client.transactional_id

        except Exception as e:
            session.rollback()  # Roll back the transaction if any errors occurred
            raise  # Re-raise the exception after rollbackx
        
def update_master_db_client(client_id: str, updates: dict, _engine):
    """
    Update an existing client record in the t_master_db table.

    Args:
    client_id (str): The primary key of the client to update.
    updates (dict): A dictionary of fields to update.
    _engine: The SQLAlchemy engine instance connected to the database.

    Raises:
    ValueError: If no client is found with the given client_id.
    """
    # Create a new session
    with sqlalchemy.orm.Session(_engine) as session:
        # Retrieve the client record by client_id
        client = session.query(t_master_db).filter_by(client_id=client_id).first()
        if client is None:
            raise ValueError(f"No client found in master_db with client_id {client_id}")

        # Retrieve the transactional_db client record
        transactional_client = session.query(t_client).filter_by(client_id=client_id).first()
        if transactional_client is None:
            raise ValueError(f"No client found in transactional_db with client_id {client_id}")

        # Fields that should not be edited
        immutable_fields = ['client_id', 'new_client_intake_date']

        # Fields that require sync with transactional_db
        sync_fields = ['phone_number']

        # Update the fields with the data provided in the updates dictionary
        for key, value in updates.items():
            if key in immutable_fields:
                raise ValueError(f"The field '{key}' is not editable.")
            if hasattr(client, key):
                setattr(client, key, value)
                if key in sync_fields:
                    setattr(transactional_client, key, value)
            else:
                raise ValueError(f"{key} is not a valid field of t_master_db")

        # Attempt to commit changes to the database
        try:
            session.commit()
            print(f"Client {client_id} updated successfully.")
        except sqlalchemy.exc.SQLAlchemyError as e:
            session.rollback()  # Roll back the transaction if any database errors occurred
            raise RuntimeError(f"Failed to update client due to: {str(e)}")
        
def delete_transactional_id_records(transactional_id: int):
    """
    Delete client records from both master_db and transactional_db tables based on the client_id.

    Args:
    client_id (str): The primary key of the client to delete.
    _engine: The SQLAlchemy engine instance connected to the database.
    """
    with sqlalchemy.orm.Session(_engine) as session:
        # Attempt to retrieve the client records from both databases
        master_client = session.query(t_master_db).filter_by(transactional_id=transactional_id).first()
        transactional_client = session.query(t_client).filter_by(transactional_id=transactional_id).first()

        if transactional_client is None:
            raise ValueError(f"No client found with transactional_id {transactional_id} in transactional DB.")

        # Delete the client records
        try:
            if master_client:
                session.delete(master_client)
            if transactional_client:
                session.delete(transactional_client)
            session.commit()
            print(f"Client records with transactional_id {transactional_id} have been deleted successfully from both databases.")
        except sqlalchemy.exc.SQLAlchemyError as e:
            session.rollback()
            raise Exception(f"Database operation failed: {e}") from e

def delete_client_id_records(client_id: str, _engine):
    """
    Delete client records from both master_db and transactional_db tables based on the client_id.

    Args:
    client_id (str): The primary key of the client to delete.
    _engine: The SQLAlchemy engine instance connected to the database.
    """
    with sqlalchemy.orm.Session(_engine) as session:
        # Attempt to retrieve the client records from both databases
        master_client = session.query(t_master_db).filter_by(client_id=client_id).first()
        transactional_client = session.query(t_client).filter_by(client_id=client_id).first()

        if master_client is None or transactional_client is None:
            raise ValueError(f"No client found with client_id {client_id} in one or both databases.")

        # Delete the client records
        try:
            if master_client:
                session.delete(master_client)
            if transactional_client:
                session.delete(transactional_client)
            session.commit()
            print(f"Client records with client_id {client_id} have been deleted successfully from both databases.")
        except sqlalchemy.exc.SQLAlchemyError as e:
            session.rollback()  # Roll back the transaction if any database errors occurred
            raise RuntimeError(f"Failed to delete client records due to: {str(e)}")

def delete_client_visithistory(transactional_id: int, visit_id: int):
    """
    Delete a specific visit history record for a client in the transactional_history table.

    Args:
    transactional_id (int): The transactional_id of the client.
    visit_id (int): The visit_id of the history record to delete.
    """
    with sqlalchemy.orm.Session(_engine) as session:
        # Attempt to retrieve the visit history record
        visit_record = session.query(t_history).filter_by(t_id=transactional_id, visit_id=visit_id).first()

        if visit_record is None:
            raise ValueError(f"No visit history record found with transactional_id {transactional_id} and visit_id {visit_id}.")

        # Delete the visit history record
        try:
            session.delete(visit_record)
            session.commit()
            print(f"Visit history record with visit_id {visit_id} for client {transactional_id} has been deleted successfully.")
        except sqlalchemy.exc.SQLAlchemyError as e:
            session.rollback()  # Roll back the transaction if any database errors occurred
            raise RuntimeError(f"Failed to delete visit history record due to: {str(e)}")

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
        try:
            if f_name is None:
                f_name = ''
            if l_name is None:
                l_name = ''
            if p is None:
                p = ''
            if dob_date is None:
                dob_date = ''
            # Select relevant row
            new_client = t_client(first_name=f_name, last_name=l_name, phone=p, dob=dob_date, client_type="walk in")
            session.add(new_client)
            session.flush()
            id = new_client.transactional_id
            if date != "" and foodbags != "":
                date_format = '%Y-%m-%d'
                date_obj = datetime.strptime(date, date_format)
                new_visit = t_history(t_id=id, visit_date=date_obj, food_bags=foodbags, baby_supplies=0,pet_food=0,
                                    gift_items=0, cleaning=0, personal_care=0, summer_feeding = 0, pj=0, clothing = 0, winter=0, other = 0, client_type="walk in")
                session.add(new_visit)
            session.commit()
        except sqlalchemy.exc.SQLAlchemyError as e:
            session.rollback()
            raise RuntimeError(f"Failed to add new client due to: {str(e)}")

def get_history (id: int):
    with sqlalchemy.orm.Session(_engine) as session:
        history = session.query(t_history).filter(t_history.t_id == id).order_by(t_history.visit_date.desc()).all()
    h = []
    for visit in history:
        visit = visit.__dict__
        del visit["_sa_instance_state"]
        del visit["client_type"]
        visit['visit_date'] = visit['visit_date'].strftime("%A \n %B %d, %Y")
        h.append(visit)
    return h

def monthEmpower(month: int, year: int):
    with sqlalchemy.orm.Session(_engine) as session:
        res = "Client,Distribution Day,Food Bags,Baby Supplies,Pet Food,Gift Items, Cleaning Supplies,"
        res += "Personal Care,Summer Feeding,Kids Pajamas,Clothing,Winter Coats,Other Items,Date\n"
        visits=session.query(t_history).filter(extract('month', t_history.visit_date) == month).filter(extract('year', t_history.visit_date) == year).filter(t_history.client_type=="Empower").all()
        for visit in visits:
            name = session.query(t_client).filter(t_client.transactional_id==visit.t_id).one()
            fullname = name.first_name + " " + name.last_name
            date = visit.visit_date.strftime("%m/%d/%Y")
            res += fullname + ','
            
            res += f"{calendar.day_name[visit.visit_date.weekday()]},{visit.food_bags},{visit.baby_supplies},"
            res += f"{visit.pet_food},{visit.gift_items},{visit.cleaning},{visit.personal_care},{visit.summer_feeding},"
            res += f"{visit.pj},{visit.clothing},{visit.winter},{visit.other},{date}\n"
        return res

def monthSummary(year: int):
    with sqlalchemy.orm.Session(_engine) as session:
        res = "Items,January,February,March,April,May,June,July,August,September,October,November,December,Year To Date\n"
        res += "Total Food Bags Distributed - Monday,"
        tot = 0
        for i in range(12):
            val = session.query(func.sum(t_history.food_bags)).filter(extract('month', t_history.visit_date) == (i + 1)).filter(extract('dow', t_history.visit_date) == 1)\
                .filter(extract('year', t_history.visit_date) == (year)).scalar()
            if val is None:
                val = 0
            tot += val
            res += str(val) + ","
        res += str(tot) + '\n'
        res += "Total Food Bags Distributed - Tuesday,"
        tot = 0
        for i in range(12):
            val = session.query(func.sum(t_history.food_bags)).filter(extract('month', t_history.visit_date) == (i + 1)).filter(extract('dow', t_history.visit_date) == 2)\
                .filter(extract('year', t_history.visit_date) == (year)).scalar()
            if val is None:
                val = 0
            tot += val
            res += str(val) + ","
        res += str(tot) + '\n'
        res += "Total Food Bags Distributed - Wednesday,"
        tot = 0
        for i in range(12):
            val = session.query(func.sum(t_history.food_bags)).filter(extract('month', t_history.visit_date) == (i + 1)).filter(extract('dow', t_history.visit_date) == 3)\
                .filter(extract('year', t_history.visit_date) == (year)).scalar()
            if val is None:
                val = 0
            tot += val
            res += str(val) + ","
        res += str(tot) + '\n'
        res += "Total Bags Distributed - Pet Food,"
        tot = 0
        for i in range(12):
            val = session.query(func.sum(t_history.pet_food)).filter(extract('month', t_history.visit_date) == (i + 1))\
                .filter(extract('year', t_history.visit_date) == (year)).scalar()
            if val is None:
                val = 0
            tot += val
            res += str(val) + ","
        res += str(tot) + '\n'
        res += "Total Bags Distributed - Personal Care,"
        tot = 0
        for i in range(12):
            val = session.query(func.sum(t_history.personal_care)).filter(extract('month', t_history.visit_date) == (i + 1))\
                .filter(extract('year', t_history.visit_date) == (year)).scalar()
            if val is None:
                val = 0
            tot += val
            res += str(val) + ","
        res += str(tot) + '\n'
        res += "Total Bags Distributed - Baby Supplies,"
        tot = 0
        for i in range(12):
            val = session.query(func.sum(t_history.baby_supplies)).filter(extract('month', t_history.visit_date) == (i + 1))\
                .filter(extract('year', t_history.visit_date) == (year)).scalar()
            if val is None:
                val = 0
            tot += val
            res += str(val) + ","
        res += str(tot) + '\n'
        res += "Total Bags Distributed -  Gift Items,"
        tot = 0
        for i in range(12):
            val = session.query(func.sum(t_history.gift_items)).filter(extract('month', t_history.visit_date) == (i + 1))\
                .filter(extract('year', t_history.visit_date) == (year)).scalar()
            if val is None:
                val = 0
            tot += val
            res += str(val) + ","
        res += str(tot) + '\n'
        res += "Total Bags Distributed - Summer Feeding,"
        tot = 0
        for i in range(12):
            val = session.query(func.sum(t_history.summer_feeding)).filter(extract('month', t_history.visit_date) == (i + 1))\
                .filter(extract('year', t_history.visit_date) == (year)).scalar()
            if val is None:
                val = 0
            tot += val
            res += str(val) + ","
        res += str(tot) + '\n'
        res += "Total Bags Distributed - Cleaning Supplies,"
        tot = 0
        for i in range(12):
            val = session.query(func.sum(t_history.cleaning)).filter(extract('month', t_history.visit_date) == (i + 1))\
                .filter(extract('year', t_history.visit_date) == (year)).scalar()
            if val is None:
                val = 0
            tot += val
            res += str(val) + ","
        res += str(tot) + '\n'
        res += "Total Bags Distributed - Kids Pajamas,"
        tot = 0
        for i in range(12):
            val = session.query(func.sum(t_history.pj)).filter(extract('month', t_history.visit_date) == (i + 1))\
                .filter(extract('year', t_history.visit_date) == (year)).scalar()
            if val is None:
                val = 0
            tot += val
            res += str(val) + ","
        res += str(tot) + '\n'
        res += "Total Bags Distributed - Clothing (General),"
        tot = 0
        for i in range(12):
            val = session.query(func.sum(t_history.clothing)).filter(extract('month', t_history.visit_date) == (i + 1))\
                .filter(extract('year', t_history.visit_date) == (year)).scalar()
            if val is None:
                val = 0
            tot += val
            res += str(val) + ","
        res += str(tot) + '\n'
        res += "Total Bags Distributed - Winter Coats,"
        tot = 0
        for i in range(12):
            val = session.query(func.sum(t_history.winter)).filter(extract('month', t_history.visit_date) == (i + 1))\
                .filter(extract('year', t_history.visit_date) == (year)).scalar()
            if val is None:
                val = 0
            tot += val
            res += str(val) + ","
        res += str(tot) + '\n'
        res += "Total Bags Distributed - Other Items,"
        tot = 0
        for i in range(12):
            val = session.query(func.sum(t_history.other)).filter(extract('month', t_history.visit_date) == (i + 1))\
                .filter(extract('year', t_history.visit_date) == (year)).scalar()
            if val is None:
                val = 0
            tot += val
            res += str(val) + ","
        res += str(tot) + '\n'
        res += "Total Walk in/Unregistered Visits,"
        tot = 0
        for i in range(12):
            val = session.query(t_history).filter(extract('month', t_history.visit_date) == (i + 1))\
                .filter(extract('year', t_history.visit_date) == (year)).filter(t_history.client_type=="walk in").count()
            if val is None:
                val = 0
            tot += val
            res += str(val) + ","
        res += str(tot) + '\n'
        res += "Total Food Pantry Visits,"
        tot = 0
        for i in range(12):
            val = session.query(t_history).filter(extract('month', t_history.visit_date) == (i + 1))\
                .filter(extract('year', t_history.visit_date) == (year)).count()
            if val is None:
                val = 0
            tot += val
            res += str(val) + ","
        res += str(tot) + '\n'
        res += "Total Food Bags Distributed,"
        tot = 0
        for i in range(12):
            val = session.query(func.sum(t_history.food_bags)).filter(extract('month', t_history.visit_date) == (i + 1))\
                .filter(extract('year', t_history.visit_date) == (year)).scalar()
            if val is None:
                val = 0
            tot += val
            res += str(val) + ","
        res += str(tot) + '\n'
        return res
    
def walkInReport(year: int):
    with sqlalchemy.orm.Session(_engine) as session:
        res = "Full Name,Phone Number,Date,Distribution Day\n"
        visits=session.query(t_history).filter(t_history.client_type == "walk in").filter(extract('year', t_history.visit_date) == (year)).all()
        for visit in visits:
            client = session.query(t_client).filter(t_client.transactional_id==visit.t_id).one()
            fullname = client.first_name + " " + client.last_name
            phone = client.phone
            date = visit.visit_date.strftime("%m/%d/%Y")
            weekday = calendar.day_name[visit.visit_date.weekday()]
            res += f"{fullname},{phone},{date},{weekday}\n"
        return res


# Function to retrieve visit history between start and end date
def get_visit_history(start, end):

    start_date = datetime.strptime(start, '%Y-%m-%d').date()
    end_date = datetime.strptime(end, '%Y-%m-%d').date()
    
    with sqlalchemy.orm.Session(_engine) as session:

        # Total number of days in range
        num_days = (end_date - start_date).days + 1

        # Initialize a list to store the visit counts for each day
        visit_counts = [0] * num_days

        # Query the database to retrieve transactional history records between start and end date
        history_records = session.query(t_history).filter(
            t_history.visit_date >= start_date,
            t_history.visit_date <= end_date
        ).all()

        # Update visit counts for each day based on the retrieved history records
        for record in history_records:
            # Calculate the index for the current record's visit date in the visit_counts list
            index = (record.visit_date - start_date).days
            # Increment the visit count for the corresponding day
            visit_counts[index] += 1


        # check visit_count array before returning
        print("check visit count list:", visit_counts)
        return visit_counts

import flask
from flask import Flask, Response
import requests
import json
from flask_cors import CORS
import databaseaccess as db
import user_login as user_db
import csv

app = Flask(__name__, static_folder="./dist/static", template_folder="./dist", static_url_path="/static")
app.config.from_object(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})

# Set up Flask login manager
# from flask_login import LoginManager
# from flask_login import login_required
# from flask_login import User
# import flask_login
# login_manager = LoginManager()
# login_manager.init_app(app)

# Login reroute
@app.route('/api/login', methods = ["POST"])
def login():

    print("REACHED LOGIN API")

    # JSON schema
    # {
    #     "username": <username>,
    #     "password": <password>
    # }
    get_data = flask.request.get_json()
    print('check inputs in app', get_data)

    # A matching login will return true in response object
    try:
        response_object = user_db.check_user(get_data["username"], get_data["password"])

    except Exception as ex:
        print("debug: login failed:", ex)
        response_object = {
            "status": False,
            "role" : "not_authorized"
        }
        # flask.redirect("/login")
        return flask.jsonify(response_object)
    
    # Save user session
    # if the above check passes, then we know the user has the right credentials
    # print('redirect now')
    # flask_login.login_user(response_object, remember= False)
    # flask.redirect("/")
    response_object = {
        "status": True,
        "role" : response_object
    }
    return flask.jsonify(response_object)

@app.route('/api/register_new_client', methods = ["POST"])
def register_new_client():
    requests = flask.request.get_json()
    
    try:
        status = db.add_master_db_client(requests)
        return flask.jsonify({"status": status}), 200
    except Exception as e:
        # Log the error here if you have logging setup
        return flask.jsonify({"error": str(e)}), 500
    
@app.route('/api/edit_masterdb_client', methods = ['POST'])
def edit_masterdb_client():
    requests = flask.request.get_json()
    if flask.request.method == 'POST':
        client_id = requests.get('client_id')
        update = requests.get('update')
    try:
        status = db.edit_masterdb_client(client_id, update)
        return flask.jsonify({"status": status}), 200
    except Exception as ex:
        return flask.jsonify({"error": str(ex)}), 500
     
# Query Master Database for users
@app.route('/api/query_masterdatabase', methods = ["POST"])
def query_masterdatabase():
    requests = flask.request.get_json()
    if flask.request.method == 'POST':
        client_id = requests.get('client_id')
        first_name = requests.get('first_name')
        last_name = requests.get('last_name')
        phone = requests.get('phone')
        month = requests.get('month')
        day = requests.get('day')
        year = requests.get('year')
    try:
        response = db.query_masterdb_client(
            client_id, first_name, last_name, phone, month, day, year)
        json_response = json.dumps(response, ensure_ascii=False)
        return Response(json_response, mimetype='application/json')
    except Exception as e:
        # Log the error here if you have logging setup
        return flask.jsonify({"error": str(e)}), 500

# Add new volunteers or admins - only accessible for ADMINS
@app.route('/api/add_new_user', methods = ["POST"])
def add_new_user():

    # input schema
    # {
    #     "sender_role": "role",
    #     "username": "...",
    #     "password": "..."
    #     "user_role": "..."
    # }

    request = flask.request.get_json()

    # Sender must be admin in order to add new user
    if request["sender_role"] != "admin":
        response = {
            "status": False
        }
        return flask.jsonify(response)
    
    username = request["username"]
    password = request["password"]
    user_role = request["user_role"]

    status = user_db.add_new_user(username= username, password= password, user_role= user_role)
    response = {
        "status": status
    }
    return flask.jsonify(response)


# Add new volunteers or admins - only accessible for ADMINS
@app.route('/api/read_all_users', methods = ["POST"])
def read_all_users():

    # input schema
    # {
    #     "sender_role": "role",
    # }

    request = flask.request.get_json()

    # Sender must be admin in order to add new user
    if request["sender_role"] != "admin":
        response = {
            "status": False,
            "user_list": []
        }
        return flask.jsonify(response)
    
    status, user_list = user_db.read_all_users()
    response = {
        "status": status,
        "user_list": user_list
    }
    return flask.jsonify(response)

# Add new volunteers or admins - only accessible for ADMINS
@app.route('/api/remove_user', methods = ["POST"])
def remove_user():

    # input schema
    # {
    #     "sender_role": "role",
    #     "username": "...",
    #     "password": "..."
    # }

    request = flask.request.get_json()

    # Sender must be admin in order to add new user
    if request["sender_role"] != "admin":
        response = {
            "status": False
        }
        return flask.jsonify(response)
    
    username = request["username"]
    password = request["password"]

    status = user_db.remove_user(username= username, password= password)
    response = {
        "status": status
    }
    return flask.jsonify(response)


# search for the user 
@app.route('/api/search', methods=['GET', 'POST'])
def search():
    get_data = flask.request.get_json()
    if flask.request.method == 'POST':
        client_id = get_data.get('client_id')
        first_name = get_data.get('first_name')
        last_name = get_data.get('last_name')
        phone = get_data.get('phone')
        month = get_data.get('month')
        day = get_data.get('day')
        year = get_data.get('year')
        try:
            response_object = db.get_client(client_id, first_name, last_name, phone, month, day, year)
        except Exception as ex:
            return flask.jsonify(False, "A server error occured")
    return flask.jsonify([True, response_object])

# add row for the user
@app.route('/api/newdate', methods = ['POST'])
def add_date():
    get_data = flask.request.get_json()
    if flask.request.method == 'POST':
        transactional_id = get_data.get('transactional_id')
        new_visit_date = get_data.get('new_visit_date')
        f_bags = get_data.get('f_bags')
        b_supplies = get_data.get('b_supplies')
        p_food = get_data.get('p_food')
        g_items = get_data.get('g_items')
        c = get_data.get('c')
        p_care = get_data.get('p_care')
        sf = get_data.get('sf')
        p = get_data.get('pj')
        cloth = get_data.get('cloth')
        w = get_data.get('w')
        o = get_data.get('o')
        try:
            response_object = db.update_client(transactional_id, new_visit_date, f_bags, b_supplies, p_food, g_items, c, 
                   p_care, sf, p, cloth, w, o )
        except Exception as ex:
            return flask.jsonify([False, str(ex)])
    return flask.jsonify([True, response_object])


# Delete entry for the user
@app.route('/api/delete', methods = ['POST'])
def delete_row():
    transactional_id = flask.request.args.get("transactional_id")

    try:
        db.delete_row(transactional_id)

    except Exception as ex:
        raise Exception(ex)

@app.route('/api/delete_t_client', methods=['POST'])
def delete_transactional_client():
    data = flask.request.get_json()  # Use 'request' directly if it's imported
    transactional_id = data.get("transactional_id")
    
    if not transactional_id:
        return flask.jsonify({"error": "Missing transactional_id"}), 400  # Bad Request for missing ID

    try:
        db.delete_transactional_id_records(transactional_id)
        return flask.jsonify({"success": "Client records deleted successfully"}), 200  # OK Success

    except ValueError as ve:
        # Handle specific known error scenarios, e.g., ID not found
        return flask.jsonify({"error": str(ve)}), 404  # Not Found
    except Exception as ex:
        # Log the exception here if possible
        return flask.jsonify({"error": "Internal server error"}), 500  # Internal Server Error

@app.route('/api/delete_client_visithistory', methods=['POST'])
def delete_client_visithistory():
    data = flask.request.get_json()
    transactional_id = data.get("transactional_id")
    visit_id = data.get("visit_id")

    if not transactional_id:
        return flask.jsonify({"error": "Missing transactional_id"}), 400  # Bad Request for missing ID
    if not visit_id:
        return flask.jsonify({"error": "Missing visit_id"}), 400  # Bad Request for missing ID
    
    try:
        db.delete_client_visithistory(transactional_id, visit_id)
        return flask.jsonify({"success": "Client visit history deleted successfully"}), 200  # OK Success
    except ValueError as ve:
        # Handle specific known error scenarios, e.g., ID not found
        return flask.jsonify({"error": str(ve)}), 404  # Not Found
    except Exception as ex:
        # Log the exception here if possible
        return flask.jsonify({"error": "Internal server error"}), 500  # Internal Server Error

# Login reroute
# @app.route('/api/login', methods = ["POST"])
# def login():

#     # JSON schema
#     # {
#     #     "username": <username>,
#     #     "password": <password>
#     # }
#     get_data = flask.request.get_json()

#     # A matching login will return true in response object
#     try:
#         response_object = user_db.check_user(get_data["username"], get_data["password"])

#     except Exception as ex:
#         print("debug: login failed:", ex)
#         response_object = False
    
#     # Return JSON Schema
#     # {
#     # "status": <True or False>
#     # }
#     return flask.jsonify(response_object)


# @app.route("/logout")
# @login_required
# def logout():
#     flask_login.logout_user()
#     return flask_login.redirect("/login")

# Flask template code to get user session id

# # Instantiate a generic user session Object
# class User(flask_login.UserMixin):
#     def __init__(self):
#         super().__init__()

# @login_manager.user_loader
# def load_user(user_id):
#     return User.get(user_id)


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    return flask.render_template("index.html")

@app.route('/api/add', methods = ['POST'])
def add_client():

    get_data = flask.request.get_json()
    if flask.request.method == 'POST':
        first_name = get_data.get("first_name")
        last_name = get_data.get("last_name")
        phone = get_data.get("phone")
        dob = get_data.get("dob")
        date = get_data.get("date")
        foodbags = get_data.get("foodbags")
    try:
        db.add_client(first_name, last_name, phone, dob, date, foodbags)
    except Exception as ex:
        return flask.jsonify([False, "A server error occured"])
    return flask.jsonify([True, "Success"])

@app.route('/api/history', methods = ['POST'])
def get_visit_history():
    get_data = flask.request.get_json()
    if flask.request.method == 'POST':
        id = get_data.get("transactional_id")
        try:
            response_object = db.get_history(id)
        except Exception as ex:
            raise Exception(ex)
    return flask.jsonify(response_object)

@app.route('/api/monthEmpower', methods = ['POST'])
def monthEmpower():
    get_data = flask.request.get_json()
    month = get_data.get("month")
    year = get_data.get("year")
    csv_data =  db.monthEmpower(month, year)
    response = flask.Response(csv_data, mimetype="text/csv")
    response.headers["Content-Disposition"] = "attachment;filename=EmpowerMonthlyReport.csv"
    return response


@app.route('/api/monthSummary', methods = ['POST'])
def monthSummary():
    get_data = flask.request.get_json()
    year = get_data.get("year")
    csv_data =  db.monthSummary(year)
    response = flask.Response(csv_data, mimetype="text/csv")
    response.headers["Content-Disposition"] = "attachment;filename=MonthSummaryReport.csv"
    return response

@app.route('/api/walkInReport', methods = ['POST'])
def walkInSummary():
    get_data = flask.request.get_json()
    year = get_data.get("year")
    csv_data =  db.walkInReport(year)
    response = flask.Response(csv_data, mimetype="text/csv")
    response.headers["Content-Disposition"] = "attachment;filename=MonthSummaryReport.csv"
    return response


# Route for general reports, 
# returns list of numVisits from startDate to endDate
@app.route('/api/report_basic', methods = ["POST"])
def report_basic():
    '''
    input schema
    {
        "sender_role": "...",
        "start_date": "...",
        "end_date": "..."
    }
    '''
    '''
    output schema
    {
        "num_visit_per_day_list": list
    }
    '''

    request = flask.request.get_json()

    start_date = request.get("start_date")
    end_date = request.get("end_date")

    # print("check basic report:", type(start_date), "  END ", type(end_date))

    visit_list = db.get_visit_history(start= start_date, end= end_date)

    # print("check visit list in server: ", visit_list)
    return flask.jsonify(visit_list)

@app.route('/api/importcsv', methods = ['POST'])
def masterdbimport():
    file = flask.request.files.get("file") 
    try:
        db.importCsv(file)
    except Exception as ex:
        return flask.jsonify([False, str(ex)])
    return flask.jsonify([True, "success"])

# Run flask server
if __name__ == '__main__':
    app.run()


# @app.route('/search/get_query', methods=['GET'])
# def search():
#     get_data = flask.request.get_json()

#     client_id = get_data.get('client_id')
#     first_name = get_data.get('first_name')
#     last_name = get_data.get('last_name')
#     phone = get_data.get('phone')
#     dob = get_data.get('dob')
#     response_object = db.get_client(client_id, first_name, last_name, phone, dob)

#     return flask.jsonify(response_object)

# @app.route('/search/update_query', methods=['GET'])
# def search():
#     get_data = flask.request.get_json()

#     transactional_id = get_data.get('transactional_id')
#     new_visit_date = get_data.get('new_visit_date')
#     special_item_list = get_data.get('special_item_list')
#     response_object = db.update_client(transactional_id, new_visit_date, special_item_list)

#     return flask.jsonify(response_object)


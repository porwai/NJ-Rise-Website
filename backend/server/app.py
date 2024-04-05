import flask
from flask import Flask
import requests
#from flask_cors import CORS
from database import databaseaccess as db

app = Flask(__name__, static_folder="../../frontend/dist/static", template_folder="../../frontend/dist", static_url_path="/static")
app.config.from_object(__name__)
#CORS(app, resources={r'/*': {'origins': '*'}})

# search for the user 
@app.route('/api/search', methods=['GET', 'POST'])
def search():
    get_data = flask.request.get_json()
    if flask.request.method == 'POST':
        client_id = get_data.get('client_id')
        first_name = get_data.get('first_name')
        last_name = get_data.get('last_name')
        phone = get_data.get('phone')
        dob = get_data.get('dob')
    # dummy = {
    #     "client_id" : "1234",
    #     "first_name" : "John",
    #     "last_name" : "Smith",
    #     "phone_number" : "6307700880"
    # }
    #response_object = db.get_client(dummy['client_id'], dummy['first_name'], dummy['last_name'], dummy['phone_number'], "11052003")
        response_object = db.get_client(client_id, first_name, last_name, phone, dob)
    # else:
        # transactional_id = get_data.get('transactional_id')
        # new_visit_date = get_data.get('new_visit_date')
        # special_item_list = get_data.get('special_item_list')
        # response_object = db.update_client(transactional_id, new_visit_date, special_item_list)
    return flask.jsonify(response_object)

# add row for the user
@app.route('/api/newdate', methods = ['POST'])
def add_date():
    transactional_id = flask.request.args.get('transactional_id')
    special_item_list = flask.request.args.get('special_item_list')
    new_visit_date = flask.request.args.get('new_visit_date')
    try:
        db.update_client(transactional_id, new_visit_date, special_item_list)
    except Exception as ex:
        raise Exception (ex)

    return

# Delete entry for the user
@app.route('/api/delete', methods = ['POST'])
def delete_row():

    transactional_id = flask.request.args.get("transactional_id")

    try:
        db.delete_row(transactional_id)

    except Exception as ex:
        raise Exception(ex)

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    if app.debug:
        return requests.get('http://localhost:5173/{}'.format(path)).text
    return flask.render_template("index.html")

@app.route('/api/add', methods = ['POST'])
def add_client():

    client_type = flask.request.args.get("client_type")
    first_name = flask.request.args.get("first_name")
    last_name = flask.request.args.get("last_name")
    phone = flask.request.args.get("phone")
    DOB = flask.request.args.get("DOB")
    visit_date_list = flask.request.args.get("visit_date_list")

    try:
        db.add(client_type, first_name, last_name, phone, DOB, visit_date_list)

    except Exception as ex:
        raise Exception(ex)
    
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


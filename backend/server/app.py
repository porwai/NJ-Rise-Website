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
        p = get_data.get('p')
        w = get_data.get('w')
        o = get_data.get('o')
        try:
            db.update_client(transactional_id, new_visit_date, f_bags, b_supplies, p_food, g_items, c, 
                   p_care, p, w, o )
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
        raise Exception(ex)
    
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



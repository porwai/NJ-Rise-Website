from flask import Flask, render_template
import json
import numpy as np

app = Flask(__name__, static_folder="dist/static", template_folder="dist", static_url_path="/static")


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def index(path):
    return render_template("index.html")

@app.route("/increment/<int:count>")
def increment(count):
    return f"{count + 1}"


@app.route("/talk/")
def talker(name):

    ret_val = {
        "paragraph" : "blah blah blah",
        "author": "Por",
    }

    num = np.random.randint(0, 2)

    if num < 1:
        ret_val = {
        "paragraph" : "blaasdfasdfasdfasdfh blah blah",
        "author": "Por",
        }
    
    print(ret_val)
    return json.dumps(ret_val)
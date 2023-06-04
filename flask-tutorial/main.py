from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

with open("/templates/config.json", "r") as c:
    params = json.load(c)["params"]

app = Flask(__name__)


if params["local_server"]:
    app.config["SQLALCHEMY_DATABASE_URI"] = params["local_uri"]
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = params["prod_uri"]

db = SQLAlchemy(app)


class Contacts(db.Model):
    # slno name message phone_num email date
    slno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    message = db.Column(db.String, nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    email = db.Column(db.String, nullable=False)
    date = db.Column(db.String, nullable=True)


@app.route("/")
def home():
    return render_template("index.html", params=params)


@app.route("/about")
def about():
    return render_template("about.html", params=params)


@app.route("/post")
def post():
    return render_template("post.html", params=params)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    # Add entry to the database
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone_num = request.form.get("phone_num")
        message = request.form.get("message")

        entry = Contacts(name=name, phone_num=phone_num, message=message, email=email, date=datetime.now())
        db.session.add(entry)
        db.session.commit()
    return render_template("contact.html", params=params)


if __name__ == "__main__":
    app.run(debug=True)
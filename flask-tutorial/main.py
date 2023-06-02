from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/prayash_blog"
db = SQLAlchemy(app)


class Contacts(db.Model):
    # slno name message phone_num email date
    slno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    message = db.Column(db.String, nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    email = db.Column(db.String, nullable=False)
    date = db.Column(db.String, nullable=False)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/post")
def post():
    return render_template("post.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    # Add entry to the database
    if request.method == "POST":
        name = request.form.get("name")
        email = request.forms.get("email")
        phone_num = request.form.get("phone_num")
        message = request.form.get("message")

        entry = Contacts(name=name, phone_num=phone_num, message=message, email=email)
        db.session.add(entry)
        db.session.commit()
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
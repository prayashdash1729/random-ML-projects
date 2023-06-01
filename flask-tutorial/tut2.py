from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    name = "sohan"
    return render_template('index.html', name=name)


@app.route("/bootstrap")
def bootstrap():
    return render_template("bootstrap.html")


if __name__ == "__main__":
    app.run(debug=True)

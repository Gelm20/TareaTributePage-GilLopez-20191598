from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/historia")
def about():
    return render_template("historia.html")

@app.route("/recepcion")
def about():
    return render_template("recepcion.html")

@app.route("/developer")
def about():
    return render_template("developer.html")

@app.route("/referencias")
def about():
    return render_template("referencias.html")


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request

app = Flask(__name__)

# @ signifies a decorator - way to wrap a function and modifying its behavior
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/", methods=["GET", "POST"])
def submit():
    output = "You entered: {}".format(request.form["text"])
    return render_template("index.html", output=output)


if __name__ == "__main__":
    app.run(debug=True, port=5001)

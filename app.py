from flask import Flask, render_template, request
import generate

app = Flask(__name__)

# @ signifies a decorator - way to wrap a function and modifying its behavior
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/", methods=["GET", "POST"])
def submit():
    lyrics = generate.get_words_from_text("lyrics/lyrics.txt")
    g = generate.make_graph(lyrics)
    composition = generate.compose(g, lyrics, 100)
    output = " ".join(composition)
    return render_template("index.html", output=output)


if __name__ == "__main__":
    app.run(debug=True, port=5001)

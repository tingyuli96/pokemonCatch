from flask import Flask, request, render_template, g, redirect, Response,session,flash
import os

app = Flask(__name__)
tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)

@app.route("/")
def hello():
    hello = "Hello World!"
    context = dict(data=hello)
    return render_template("index.html", **context)

if __name__ == "__main__":
    app.run(debug=True)
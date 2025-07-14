from flask import Flask, render_template

skills_app = Flask(__name__)

@skills_app.route("/")
def homepage():
    return render_template("index22.html", title="Homepage")

if __name__ == "__main__":

    skills_app.run()
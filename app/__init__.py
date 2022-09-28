from flask import Flask, redirect, render_template, session, url_for
from flask_babel import Babel, request
from flask_session import Session

app = Flask(__name__)

# Use development configuration.
app.config.from_object("config.DevConfig")

babel = Babel(app)
Session(app)


@app.route("/")
def homepage():
    return render_template("homepage.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/areas")
def areas():
    return render_template("areas.html")


@app.route("/team")
def team():
    return render_template("team.html")


@app.route("/news")
def news():
    return render_template("news.html")


@app.route("/career")
def career():
    return render_template("career.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/language/<language>")
def set_language(language=None):
    session["language"] = language
    return redirect(request.referrer)


@babel.localeselector
def get_locale():
    # if the user has set up the language manually it will be stored in the session,
    # so we use the locale from the user settings
    language = session.get("language", "tr")
    if language is not None:
        return language


if __name__ == "__main__":
    app.run(debug=True)

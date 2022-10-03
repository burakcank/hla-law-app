import pathlib

import aspose.words as aw
from bs4 import BeautifulSoup
from flask import Flask, redirect, render_template, session, url_for
from flask_babel import Babel, request
from flask_mailman import Mail
from flask_session import Session
from sassutils.wsgi import SassMiddleware

app = Flask(__name__)

app.wsgi_app = SassMiddleware(
    app.wsgi_app,
    {"app": ("static/scss", "static/css", "/static/css")},
)

# Use development configuration.
app.config.from_object("config.DevConfig")

babel = Babel(app)
Session(app)
Mail(app)


@app.route("/")
def homepage():
    return render_template("homepage.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/areas")
def areas():
    from app.data import areas

    return render_template("areas.html", areas=areas)


@app.route("/team")
def team():
    from app.data import team

    return render_template("team.html", team=team)


@app.route("/resume/<member>")
def resume(member):
    from app.data import team

    if member == "mmh":
        member = team[0]
    elif member == "mtl":
        member = team[1]
    elif member == "da":
        member = team[2]

    return render_template("resume.html", member=member)


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


@app.route("/serve_document/<doc_type>")
def serve_document(doc_type):
    doc_name = None
    lang = session.get("language", "tr").upper()
    if doc_type == "legal_notice":
        doc_name = f"Kullanım Koşulları {lang}"
        strip_paragraphs = [0]
    elif doc_type == "privacy_policy":
        doc_name = f"KVKK Gizlilik ve Çerez Politikası {lang}"
        strip_paragraphs = [0, 1, -3, -2, -1]
    elif doc_type == "career_notice":
        doc_name = f"Kariyer Aydınlatma Metni {lang}"
        strip_paragraphs = [0, 1, -3, -2, -1]

    html_file = pathlib.Path(f"{app.root_path}/static/files/html/{doc_name}.html")
    if not html_file.is_file():
        doc = aw.Document(f"{app.root_path}/static/files/{doc_name}.docx")
        doc.save(f"{app.root_path}/static/files/html/{doc_name}.html")
    with open(f"{app.root_path}/static/files/html/{doc_name}.html") as html_file:
        soup = BeautifulSoup(html_file)

    # Remove the watermark from aspose.
    paragraphs = soup.body.div.find_all("p")
    for i in strip_paragraphs:
        paragraphs[i].extract()
    html_content = soup.body.div

    return render_template("document.html", html_content=html_content)


@app.route("/send_mail")
def send_mail():
    mail_data = request.form.get_json()
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

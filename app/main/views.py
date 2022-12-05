import logging
import pathlib

import aspose.words as aw
from bs4 import BeautifulSoup
from flask import abort, current_app, flash, redirect, render_template, session
from flask_babel import lazy_gettext, request
from flask_mailing import Message

from app import db, mail
from app.data import areas_data, news_data, team_data
from app.email import send_email
from app.main import main_bp
from app.models import EmailRequest


@main_bp.route("/")
def homepage():
    """Render homepage with news."""
    return render_template("homepage.html", news_data=news_data)


@main_bp.route("/new/<int:new_id>")
def new(new_id):
    """Page for each individual new."""
    try:
        new = news_data[new_id]
    except IndexError:
        abort(404)
    return render_template("new.html", new=new)


@main_bp.route("/about")
def about():
    """Render about page."""
    return render_template("about.html")


@main_bp.route("/areas")
def areas():
    """Render practice areas page."""
    return render_template("areas.html", areas=areas_data)


@main_bp.route("/team")
@main_bp.route("/team/<member>")
def team(member=None):
    """Render team page or team member's resume page if given."""
    if not member:
        return render_template("team.html", team=team_data)

    if member == "mmh":
        member = team_data[0]
    elif member == "mtl":
        member = team_data[1]
    elif member == "da":
        member = team_data[2]
    else:
        abort(404)

    return render_template("resume.html", member=member)


@main_bp.route("/news")
def news():
    """Render news page."""
    return render_template("news.html")


@main_bp.route("/career")
def career():
    """Render career page."""
    return render_template("career.html")


@main_bp.route("/contact")
def contact():
    """Render contact page."""
    return render_template("contact.html")


@main_bp.route("/language/<language>")
def set_language(language=None):
    """Set the language for the session."""
    session["language"] = language
    return redirect(request.referrer)


@main_bp.route("/serve_document/<doc_type>")
def serve_document(doc_type):
    """
    Serve documents from the `static/files` folder.

    1. Convert .docx files to .html files.
    2. Remove the watermarked paragraphs from the document.
    3. Pass the converted html document into the `document.html` and render.
    """
    # Fetch the language for the document.
    lang = session.get("language", "en").upper()

    # According to the doc_name we need to decide which paragraphs to strip.
    doc_name = None
    if doc_type == "legal_notice":
        doc_name = f"Kullanım Koşulları {lang}"
        strip_paragraphs = [0]
    elif doc_type == "privacy_policy":
        doc_name = f"KVKK Gizlilik ve Çerez Politikası {lang}"
        strip_paragraphs = [0, 1, -3, -2, -1]
    elif doc_type == "career_notice":
        doc_name = f"Kariyer Aydınlatma Metni {lang}"
        strip_paragraphs = [0, 1, -3, -2, -1]
    elif doc_type == "privacy_policy_contact":
        doc_name = f"İletişim Formu Aydınlatma Metni {lang}"
        strip_paragraphs = [0, 1, -3, -2, -1]
    else:
        # The file does not exist.
        abort(404)

    html_file = pathlib.Path(
        f"{current_app.root_path}/static/files/html/{doc_name}.html"
    )
    # If the already converted html file does not exist, convert and save it.
    if not html_file.is_file():
        doc = aw.Document(f"{current_app.root_path}/static/files/{doc_name}.docx")
        doc.save(f"{current_app.root_path}/static/files/html/{doc_name}.html")

    # Open the converted html document for stripping.
    with open(
        f"{current_app.root_path}/static/files/html/{doc_name}.html"
    ) as html_file:
        soup = BeautifulSoup(html_file)

    # Remove the watermark from aspose.
    paragraphs = soup.body.div.find_all("p")
    for i in strip_paragraphs:
        paragraphs[i].extract()
    html_content = soup.body.div

    return render_template("document.html", html_content=html_content)


@main_bp.route("/send_mail", methods=["POST"])
def send_mail():
    mail_data = request.form.to_dict()
    try:
        # send_email(
        #     subject="HLA Law - Info email",
        #     recipients=[mail_data["email"]],
        #     body=mail_data["request"],
        # )
        email_request = EmailRequest(
            sent_to=mail_data["email"],
            sent_from=current_app.config["MAIL_USERNAME"],
            content=mail_data["request"],
        )
        flash(
            lazy_gettext(
                "Talebiniz alınmıştır, en kısa zamanda size geri döneceğiz. Teşekkürler."
            )
        )
        db.session.add(email_request)
        db.session.commit()
    except Exception as ex:
        print(ex)

    return redirect(request.referrer)

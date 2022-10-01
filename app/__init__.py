from flask import Flask, redirect, render_template, session, url_for
from flask_babel import Babel, request
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


@app.route("/legal_notice")
def legal_notice():
    if session["language"] == "en":
        return render_template("legal_notice_en.html")
    text = """YASAL UYARI
İşbu Yasal Uyarı, Helvacı Laik Aşar Hukuk Bürosu (“Helvacı Laik Aşar”) tarafından yönetilen
www.hla-law.com alan adlı internet sitesi ile buna bağlı internet sitelerini (“İnternet Sitesi”) ziyaret
eden kişiler (“Kullanıcı”) için hazırlanmıştır.
Kullanıcı, İnternet Sitesi’ni kullanırken işbu Yasal Uyarı’da bildirilen hususları kabul etmiş
sayılmaktadır. Kullanıcı tarafından, açıklanan hususların kabul edilmemesi halinde İnternet Sitesi
kullanılmamalıdır.
Helvacı Laik Aşar tarafından İnternet Sitesi üzerinden paylaşılan bilgiler yalnızca bilgi verme amaçlı
olarak hazırlanmış olup herhangi bir şekilde hukuki görüş olarak kullanılmamalıdır. İnternet Sitesi’nde
yer alan bilgiler; yasal mevzuatta meydana gelen değişikliklere bağlı olarak güncelliğini yitirebilecek
ve yürürlükte olan yasal gelişmelerin son halini yansıtmayabilecek olup, bilgilerin güncelliği garanti
edilmemektedir. Bu nedenle, Helvacı Laik Aşar, İnternet Sitesi’nin kullanımı sonucunda meydana gelen
zararlardan dolayı sorumluluk kabul etmemekte olup İnternet Sitesi’ndeki bilgileri kullanarak herhangi
bir işlem yapmadan önce yetkili kişilere yasal danışmanlık için başvurmanızı önerir.
Helvacı Laik Aşar ile avukat-müvekkil ilişkisi kurulabilmesi için açık ve yazılı bir öneri veya davet ile
yine bunların kabul edildiğine dair açık ve yazılı bir bildirim gerekmektedir. Açık ve yazılı mutabakat
veya sözleşme olmaksızın, İnternet Sitesi’nde yayınlanan içeriklere ulaşmak, onları kullanmak, Helvacı
Laik Aşar ile İnternet Sitesi üzerinden iletişime geçmek ve bültene abone olmak avukat-müvekkil ilişkisi
oluşturmamaktadır.
İnternet Sitesi ve İnternet Sitesi’ndeki yazılı bilgi, belge, bülten ve benzeri yayın faaliyetlerinin her nevi
mülkiyet ve kullanım hakkı, Helvacı Laik Aşar’a aittir. Fikri mülkiyet hakkı dahilindeki yazılı tüm bilgi
ve belgeler ile görsel materyaller; Helvacı Laik Aşar’ın yazılı izni olmadıkça kullanılamaz, çoğaltılamaz
ve yayınlanamaz. İnternet Sitesi, iş veya buna benzer başka bir kazanım talep etmek ve/veya reklam
amaçlı olarak kullanılamaz.
Helvacı Laik Aşar, işbu Yasal Uyarı’da ve İnternet Sitesi’nde dilediği zaman değişiklik yapma, yayını
durdurma ve güncelleme yapma hakkına sahiptir. Bu düzenlemeler, İnternet Sitesi’nde yayınlandığı
andan itibaren geçerlilik kazanır ve Kullanıcı tarafından kabul edilmiş sayılır. İnternet Sitesi’ne her yeni
erişim ile birlikte güncel Yasal Uyarı kabul edilmiş sayılmaktadır."""
    return render_template("legal_notice_tr.html", text=text)


@babel.localeselector
def get_locale():
    # if the user has set up the language manually it will be stored in the session,
    # so we use the locale from the user settings
    language = session.get("language", "tr")
    if language is not None:
        return language


if __name__ == "__main__":
    app.run(debug=True)

from flask_babel import gettext

areas = [
    {
        "id": 1,
        "name": gettext("Bilişim ve İnternet Teknolojileri Hukuku"),
        "icon": '<i class="fa-solid fa-laptop"></i>',
        "paragraphs": [
            gettext(
                "Ulusal ve uluslararası gelişmeleri, gerek teknik anlamda gerekse hukuken ilgili mevzuatlar kapsamında takip ederek çalışan özel ekibimiz ile günden güne gelişen ve büyüyen bilişim ve internet teknolojileri alanında, hukuki danışmanlık hizmeti sunmaktayız. Danışmanlık hizmetimizin yanında, karşılaşmış oldukları uyuşmazlıklarda müvekkillerimizi, arabuluculuk, dava ve diğer uyuşmazlık çözüm yöntemleri aşamalarında etkin bir şekilde temsil etmekteyiz."
            )
        ],
    },
    {
        "id": 2,
        "name": gettext("Finans Teknolojileri Hukuku"),
        "icon": '<i class="fa-solid fa-credit-card"></i>',
        "paragraphs": [
            gettext(
                "Teknoloji ile finans ve bankacılık hizmetlerinin görülmesini amaçlayan teknoloji kuruluşları, ülkemizde faaliyetlerini yoğunlaştırmış ve bu kapsamda gerekli hukuksal zeminler oluşturulmuştur. 27.06.2013 tarihli Resmî Gazete'de yayımlanan 6493 Sayılı Ödeme ve Menkul Kıymet Mutabakat Sistemleri, Ödeme Hizmetleri ve Elektronik Para Kuruluşları Hakkında Kanun (“Kanun”) uyarınca, ödeme hizmetleri sunan ve elektronik para ihracı faaliyetleri yürüten kuruluşların bu Kanun kapsamında uyum süreçlerinin gerçekleştirilmesi gerekmektedir."
            ),
            gettext(
                "Helvacı Laik Aşar olarak, ülkemizde ödeme hizmetleri ve elektronik para ihracı faaliyetleri yürüten yerli ve yabancı kuruluşların; Kanun ve ilgili tebliğ ve yönetmelikler kapsamındaki uyum süreçlerini gerçekleştirmekteyiz. Bu kapsamda, Kanun’un düzenlediği alanlarda faaliyet gösteren kuruluşlara yönelik olarak; ürün ve faaliyetlerinin Kanun ve ilgili diğer mevzuata uygun hale getirilmesi için gerekli yol haritasının oluşturulması; BDDK (Bankacılık Düzenleme Ve Denetleme Kurumu)ve TCMB (Türkiye Cumhuriyeti Merkez Bankası) nezdinde faaliyet izni başvurusu için gerekli her türlü belgenin hazırlanarak başvuru sürecinin yürütülmesi; alınacak hizmetlere ve gerçekleştirilecek iş modeline yönelik sözleşmelerin hazırlanması gibi hizmetler sunmaktayız."
            ),
        ],
    },
    {
        "id": 3,
        "name": gettext("Elektronik Ticaret Hukuku"),
        "icon": '<i class="fa-solid fa-bag-shopping"></i>',
        "paragraphs": [
            gettext(
                "Elektronik ticaret sektörü, tüm dünyada olduğu gibi ülkemizde de pazardaki payı açısından çok önemli bir konuma gelmiştir. Bu durum, teknolojinin de katkılarıyla, birçok düzenlemeyi ve hukuki gerekliliği de beraberinde getirmiştir. Helvacı Laik Aşar olarak, ülkemizde ödeme hizmetleri ve elektronik para ihracı faaliyetleri yürüten yerli ve yabancı kuruluşların; Kanun ve ilgili tebliğ ve yönetmelikler kapsamındaki uyum süreçlerini gerçekleştirmekteyiz."
            ),
            gettext(
                "Helvacı Laik Aşar olarak, e-ticaret sektöründe faaliyet gösteren şirketlerin ilgili hukuki düzenlemelere yönelik uyum süreçlerini yürütmekteyiz. Aracı hizmet sağlayıcılarının, hizmet sağlayıcıları ve tüketicilerle olan hukuki ve ticari ilişkilerinde kendilerine destek veriyor, tarafların yükümlülüklerini yerine getirmelerini sağlıyor ve böylece tüketicilerin internet üzerinden güvenilir alışveriş yapmalarına katkı sunuyoruz."
            ),
            gettext(
                "Bu kapsamda; e-ticaret faaliyeti yürütecek şirketlerin yapılandırılması, finansmanı ve e-ticaret faaliyetlerinin gerçekleştirilmesi için gerekli tüm sözleşmelerin ve belgelerin hazırlanması, revize edilmesi; 6563 sayılı Elektronik Ticaretin Düzenlenmesi Hakkında Kanun ve ilgili düzenlemeler nezdindeki yükümlülüklerine uyumun sağlanması; tüketicilerle olan ilişkilerden ve tüketici hukukundan kaynaklanan uyuşmazlıkların takibi; fikri mülkiyet haklarının korunmasına yönelik başvuruların yapılması ve gerekli önlemlerin alınması; 6698 Sayılı Kişisel Verilerin Korunması Kanunu’na uyumun sağlanması; internet alan adı alınması hizmeti kapsamındaki süreçlerin yürütülmesi, tüketicilere yönelik olarak internet sitesi için gerekli sözleşme ve belgelerin hazırlanması ve benzeri birçok konuda müvekkillerimize danışmanlık hizmeti sunmaktayız."
            ),
        ],
    },
    {
        "id": 4,
        "name": gettext("Kişisel Veri Hukuku"),
        "icon": '<i class="fa-solid fa-unlock-keyhole"></i>',
        "paragraphs": [
            gettext(
                "Kişisel verilerin korunmasına ilişkin ulusal ve uluslararası gelişmeleri yakından takip eden ekibimiz ile müvekkillerimizin, 6698 sayılı Kişisel Verilerin Korunması Hakkında Kanun ve ilgili mevzuata uyum süreçlerini yürütmekteyiz. Bu kapsamda, öncelikle müvekkillerimizin kişisel veri işleme süreçlerinin analizini yaparak mevcut durumlarının tespit edilmesi, akabinde ise veri envanterinin hazırlanması, Veri Sorumluları Sicil Bilgi Sistemi’ne kayıt sürecinin yürütülmesi, veri işleme, saklama, anonim hale getirme ve imha politikalarının ve aydınlatma metinleri ile açık rıza beyan formlarının hazırlanması, gerekli idari ve teknik tedbirlerin alınması, veri sahiplerinin başvurularının cevaplanması, herhangi bir ihlal durumunda gerekli bildirimlerin yapılması, üçüncü kişiler ile imzalanacak sözleşmelerin hazırlanması ve revize edilmesi, ticari iletilere ilişkin uyum sürecinin tamamlanması, ulusal ve uluslararası gelişmelerin müvekkillerimize raporlanması ve şirket içi farkındalığı artırmak adına eğitim verilmesi gibi konularda müvekkillerimize hukuki danışmanlık sunmaktayız."
            ),
        ],
    },
    {
        "id": 5,
        "name": gettext("Fikri Mülkiyet Hukuku"),
        "icon": '<i class="fa-regular fa-copyright"></i>',
        "paragraphs": [
            gettext(
                "Helvacı Laik Aşar olarak, müvekkillerimize başta 5846 sayılı Fikir ve Sanat Eserleri Kanunu olmak üzere ilgili tüm mevzuat kapsamında fikri ve sınai haklarından en etkin şekilde yararlanmaları ve bu haklarını koruyabilmeleri için hukuki danışmanlık hizmeti sunmaktayız."
            ),
            gettext(
                "Fikri Mülkiyet Hukuku kapsamında; patent, faydalı model, marka, telif hakları, coğrafi işaretler, tasarım, internet alan adları, müzik, fotoğrafik eserler, edebiyat, mimari ve artistik eserler, sinematografik eserler, televizyon program formatları ve bilgisayar yazılımı ile veri tabanı gibi konuları kapsayacak şekilde danışmanlık hizmeti vermekteyiz. Bu çerçevede; fikri mülkiyet haklarına ilişkin sözleşmelerinin hazırlanması ve revize edilmesi ve fikri mülkiyet haklarının kullanılması ile devir işlemlerinin gerçekleştirilmesi gibi faaliyetleri yürütmekteyiz."
            ),
            gettext(
                "Ayrıca, müvekkillerimizin haklarının ihlal edildiği durumlarda tecavüzün önlenmesi, haksız rekabet, maddi ve manevi tazminat gibi davalarda müvekkillerimizi uyuşmazlık aşamalarında temsil etmekteyiz."
            ),
        ],
    },
    {
        "id": 6,
        "name": gettext("Şirketler ve Ticaret Hukuku"),
        "icon": '<i class="fa-solid fa-building-columns"></i>',
        "paragraphs": [
            gettext(
                "Ulusal ve uluslararası düzeyde faaliyet gösteren veya göstermeyi hedefleyen müvekkillerimize, şirket kuruluş ve sona erme işlemleri, şirket ana sözleşmesinin hazırlanması ve incelenmesi, hissedarlık, hisse devir veya iştirak sözleşmelerinin hazırlanması ve incelenmesi, genel kurul ve yönetim kurulu toplantılarının gerçekleştirilmesi, şirketlerin şube açılış işlemlerinin gerçekleştirilmesi, şirket imza sirküleri ile iç yönergelerinin hazırlanması, şirketin taraf olacağı alım-satım, kira, bayilik, acentelik, tedarik, dağıtım, franchise ve benzeri her türlü ticari sözleşmenin hazırlanması ve revize edilmesi, faaliyet alanlarına ilişkin mevzuata uyumun sağlanması ve faaliyet alanlarına ilişkin her türlü güncel gelişmenin raporlanması gibi konularda danışmanlık hizmeti sunmakta ve müvekkillerimizin kurumsallaşma süreçlerini yürütmekteyiz. Diğer taraftan, müvekkillerimizi; aralarında akdetmiş oldukları sözleşmeler, genel kurul toplantıları ve kararlarından ve 6102 sayılı Türk Ticaret Kanunu ile ilgili mevzuattan doğan haksız rekabete dayalı tazminat davaları, ortaklığın feshi gibi uyuşmazlıklarda arabuluculuk ve dava aşamalarında temsil etmekteyiz."
            )
        ],
    },
    {
        "id": 7,
        "name": gettext("Sözleşmeler Hukuku"),
        "icon": '<i class="fa-regular fa-handshake"></i>',
        "paragraphs": [
            gettext(
                "Helvacı Laik Aşar olarak; sözleşmelerin usul ve maddi hukuk kuralları gereğince uygulanabilirliği ve müvekkillerimizin talepleri doğrultusunda; taraf iradelerinin sağlıklı bir şekilde ifade edilmesi, sözleşmesel ilişkinin doğru bir şekilde tanımlanması, karşılıklı borç ve yükümlülüklerin belirlenmesi, sözleşmeye aykırı hareket edilmesi halinde doğacak sorumluluk ve sonuçların belirlenmesi açısından sözleşme müzakerelerinin yürütülmesi, sözleşmelerin hazırlanması ve revize edilmesi, sözleşmelere ilişkin hukuki risk analizlerinin yapılması ve raporlanması süreçlerinde danışmanlık hizmeti sunmakta ve müvekkillerimizi taraf oldukları sözleşmelerden doğan uyuşmazlıklarda temsil etmekteyiz."
            )
        ],
    },
    {
        "id": 8,
        "name": gettext("İdare ve Vergi Hukuku"),
        "icon": '<i class="fa-solid fa-scale-balanced"></i>',
        "paragraphs": [
            gettext(
                "Gerçek ve tüzel kişi müvekkillerimizi, idari otoriteler ile olan hukuki ilişkilerinde etkin bir şekilde temsil etmekteyiz. Bu kapsamda müvekkillerimize; idari düzenleme, tebliğ, kararname, rehber, kılavuz, karar, idari işlemler ve idari eylemler, imar, kamulaştırma ve kamu ihaleleri gibi konularda gerekli idari başvuruların yapılması aşamasında danışmanlık hizmeti vermekteyiz. Ayrıca, ilk derece mahkemelerinde ve Danıştay’da görülecek davalarda temsil etmekteyiz."
            ),
            gettext(
                "Vergi hukuku kapsamında ise, tahakkuk eden vergiler, bu vergiler kapsamında doğan vergi suçları, harç ve cezalarına ilişkin olarak hukuki danışmanlık hizmeti vermekte olduğumuz gibi aynı zamanda müvekkillerimizi doğacak uyuşmazlıklarda temsil etmekteyiz."
            ),
        ],
    },
    {
        "id": 9,
        "name": gettext("İş ve Sosyal Güvenlik Hukuku"),
        "icon": '<i class="fa-solid fa-briefcase"></i>',
        "paragraphs": [
            gettext(
                "Helvacı Laik Aşar olarak; müvekkillerimizin çalışanlarına sağladıkları çalışma koşullarının hukuka uygunluğunun denetlenmesi ve hukuka uygun hale getirilmesi; çalışanları ile girdikleri her türlü hukuki ilişki ve sürecin yürütülmesi ve muhtemel dava ile arabuluculuk süreçlerinde doğabilecek risklerin minimize edilmesi için önleyici hukuk hizmeti sağlamaktayız."
            ),
            gettext(
                "Danışmanlık hizmetimiz ile müvekkillerimizin mevcut iş sözleşmelerinin hukuka uygunluk denetiminin yapılması, yeniden düzenlenmesi, imzalanması ve sona erdirilmesi; iş hukuku ikincil metinlerinin hazırlanması; müvekkillerimizin çalışanlarına iş hukuku eğitimlerinin verilmesi ve çalışanların disiplin süreçlerinin yürütülmesi; iş kazası, meslek hastalığı ve sair hallerde müvekkillerimizin haklarının korunması kapsamındaki süreçleri yürütüyor ve tüm bu konulardan doğan uyuşmazlık aşamalarında aktif bir şekilde rol alıyoruz."
            ),
        ],
    },
    {
        "id": 10,
        "name": gettext("Uluslararası İlişkiler Hukuku"),
        "icon": '<i class="fa-solid fa-earth-americas"></i>',
        "paragraphs": [
            gettext(
                "Helvacı Laik Aşar olarak, sivil toplumun faaliyetlerinin desteklenmesinin ülkemiz ve dünyamızın geleceği için çok önemli olduğuna inanıyoruz. Bu inancımız doğrultusunda, ülkemizde faaliyet göstermek isteyen yerli ve yabancı sivil toplum kuruluşları ile, faaliyetlerinin hukuka uygun bir şekilde yürütülebilmesi için çalışıyoruz. Sivil Toplum Kuruluşlarının Türkiye’deki faaliyetlerinin Türk Hukuk sistemine uyum süreçleri, hukuken kurulabilmeleri ve devamlılıklarını sağlayabilmeleri için gerekli danışmanlık hizmetini sağlamaktayız. Sivil toplum kuruluşu olan müvekkillerimizin ihtiyaçları doğrultusunda, Dernekler Hukuku, İş hukuku, Kişisel Veri Hukuku, Şirketler Hukuku, Sözleşmeler Hukuku ve İdare Hukuku alanlarında mevzuata uyum süreçlerini yürütmekteyiz."
            )
        ],
    },
    {
        "id": 11,
        "name": gettext("Gayrimenkul ve Kat Mülkiyeti Hukuku"),
        "icon": '<i class="fa-solid fa-building"></i>',
        "paragraphs": [
            gettext(
                "Helvacı Laik Aşar olarak, müvekkillerimiz için, gayrimenkullerin hukuki incelemesinin yapılması ve raporlanması, gayrimenkul satış vaadi ve satış, kira, üst hakkı, intifa hakkı ve inşaat gibi gayrimenkul sözleşmelerinin hazırlanması ve revize edilmesi ve 634 sayılı Kat Mülkiyeti Kanunu kapsamında hukuki danışmanlık hizmeti vermekteyiz."
            ),
            gettext(
                "Müvekkillerimize sunmuş olduğumuz hukuki danışmanlık hizmeti yanında müvekkillerimizi; tapu iptali ve tescili, tahliye, tapu kaydının düzeltilmesi, müdahalenin önlenmesi ve haksız işgal tazminatı, ortaklığın giderilmesi, kamulaştırma ve benzeri hukuki uyuşmazlıklar ile 634 sayılı Kat Mülkiyeti Kanunu kapsamındaki uyuşmazlıklarda, mahkemeler ve ilgili kamu kurum ve kuruluşları nezdinde temsil etmekteyiz."
            ),
        ],
    },
    {
        "id": 12,
        "name": gettext("Yabancılar ve Vatandaşlık Hukuku"),
        "icon": '<i class="fa-solid fa-people-group"></i>',
        "paragraphs": [
            gettext(
                "Türkiye, yakın coğrafyasında ve kendi dinamikleri çerçevesinde yaşanan değişikliklerin etkisiyle göç alan bir ülke konumuna gelmiştir. Bu nedenle yabancıların Türkiye’deki hukuki statüleri ve hak ile yükümlülüklerinin belirlenmesi önemli bir hal almıştır. Helvacı Laik Aşar olarak; Türkiye’de bulunan yabancıların hak ve yükümlülüklerini ilgilendiren her türlü idari ve hukuki gelişmeyi takip etmekteyiz. Yabancıların Türkiye’de; oturma izni, çalışma izni, vatandaşlık ve gayrimenkul sahibi olması gibi konularda da bireysel ve kurumsal müvekkillerimize danışmanlık hizmeti vermekteyiz."
            )
        ],
    },
]

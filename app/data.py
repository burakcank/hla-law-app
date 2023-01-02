from flask_babel import lazy_gettext

areas_data = [
    {
        "id": 1,
        "name": lazy_gettext("Bilişim ve İnternet Teknolojileri Hukuku"),
        "icon": '<i class="fa-solid fa-laptop"></i>',
        "paragraphs": [
            lazy_gettext(
                "Ulusal ve uluslararası gelişmeleri, gerek teknik anlamda gerekse hukuken ilgili mevzuatlar kapsamında takip ederek çalışan özel ekibimiz ile günden güne gelişen ve büyüyen bilişim ve internet teknolojileri alanında, hukuki danışmanlık hizmeti sunmaktayız. Danışmanlık hizmetimizin yanında, karşılaşmış oldukları uyuşmazlıklarda müvekkillerimizi, arabuluculuk, dava ve diğer uyuşmazlık çözüm yöntemleri aşamalarında etkin bir şekilde temsil etmekteyiz."
            )
        ],
    },
    {
        "id": 2,
        "name": lazy_gettext("Finans Teknolojileri Hukuku"),
        "icon": '<i class="fa-solid fa-credit-card"></i>',
        "paragraphs": [
            lazy_gettext(
                "Teknoloji ile finans ve bankacılık hizmetlerinin görülmesini amaçlayan teknoloji kuruluşları, ülkemizde faaliyetlerini yoğunlaştırmış ve bu kapsamda gerekli hukuksal zeminler oluşturulmuştur. 27.06.2013 tarihli Resmî Gazete'de yayımlanan 6493 Sayılı Ödeme ve Menkul Kıymet Mutabakat Sistemleri, Ödeme Hizmetleri ve Elektronik Para Kuruluşları Hakkında Kanun (“Kanun”) uyarınca, ödeme hizmetleri sunan ve elektronik para ihracı faaliyetleri yürüten kuruluşların bu Kanun kapsamında uyum süreçlerinin gerçekleştirilmesi gerekmektedir."
            ),
            lazy_gettext(
                "Helvacı Laik Aşar olarak, ülkemizde ödeme hizmetleri ve elektronik para ihracı faaliyetleri yürüten yerli ve yabancı kuruluşların; Kanun ve ilgili tebliğ ve yönetmelikler kapsamındaki uyum süreçlerini gerçekleştirmekteyiz. Bu kapsamda, Kanun’un düzenlediği alanlarda faaliyet gösteren kuruluşlara yönelik olarak; ürün ve faaliyetlerinin Kanun ve ilgili diğer mevzuata uygun hale getirilmesi için gerekli yol haritasının oluşturulması; BDDK (Bankacılık Düzenleme Ve Denetleme Kurumu)ve TCMB (Türkiye Cumhuriyeti Merkez Bankası) nezdinde faaliyet izni başvurusu için gerekli her türlü belgenin hazırlanarak başvuru sürecinin yürütülmesi; alınacak hizmetlere ve gerçekleştirilecek iş modeline yönelik sözleşmelerin hazırlanması gibi hizmetler sunmaktayız."
            ),
        ],
    },
    {
        "id": 3,
        "name": lazy_gettext("Elektronik Ticaret Hukuku"),
        "icon": '<i class="fa-solid fa-bag-shopping"></i>',
        "paragraphs": [
            lazy_gettext(
                "Elektronik ticaret sektörü, tüm dünyada olduğu gibi ülkemizde de pazardaki payı açısından çok önemli bir konuma gelmiştir. Bu durum, teknolojinin de katkılarıyla, birçok düzenlemeyi ve hukuki gerekliliği de beraberinde getirmiştir. Helvacı Laik Aşar olarak, ülkemizde ödeme hizmetleri ve elektronik para ihracı faaliyetleri yürüten yerli ve yabancı kuruluşların; Kanun ve ilgili tebliğ ve yönetmelikler kapsamındaki uyum süreçlerini gerçekleştirmekteyiz."
            ),
            lazy_gettext(
                "Helvacı Laik Aşar olarak, e-ticaret sektöründe faaliyet gösteren şirketlerin ilgili hukuki düzenlemelere yönelik uyum süreçlerini yürütmekteyiz. Aracı hizmet sağlayıcılarının, hizmet sağlayıcıları ve tüketicilerle olan hukuki ve ticari ilişkilerinde kendilerine destek veriyor, tarafların yükümlülüklerini yerine getirmelerini sağlıyor ve böylece tüketicilerin internet üzerinden güvenilir alışveriş yapmalarına katkı sunuyoruz."
            ),
            lazy_gettext(
                "Bu kapsamda; e-ticaret faaliyeti yürütecek şirketlerin yapılandırılması, finansmanı ve e-ticaret faaliyetlerinin gerçekleştirilmesi için gerekli tüm sözleşmelerin ve belgelerin hazırlanması, revize edilmesi; 6563 sayılı Elektronik Ticaretin Düzenlenmesi Hakkında Kanun ve ilgili düzenlemeler nezdindeki yükümlülüklerine uyumun sağlanması; tüketicilerle olan ilişkilerden ve tüketici hukukundan kaynaklanan uyuşmazlıkların takibi; fikri mülkiyet haklarının korunmasına yönelik başvuruların yapılması ve gerekli önlemlerin alınması; 6698 Sayılı Kişisel Verilerin Korunması Kanunu’na uyumun sağlanması; internet alan adı alınması hizmeti kapsamındaki süreçlerin yürütülmesi, tüketicilere yönelik olarak internet sitesi için gerekli sözleşme ve belgelerin hazırlanması ve benzeri birçok konuda müvekkillerimize danışmanlık hizmeti sunmaktayız."
            ),
        ],
    },
    {
        "id": 4,
        "name": lazy_gettext("Kişisel Veri Hukuku"),
        "icon": '<i class="fa-solid fa-unlock-keyhole"></i>',
        "paragraphs": [
            lazy_gettext(
                "Kişisel verilerin korunmasına ilişkin ulusal ve uluslararası gelişmeleri yakından takip eden ekibimiz ile müvekkillerimizin, 6698 sayılı Kişisel Verilerin Korunması Hakkında Kanun ve ilgili mevzuata uyum süreçlerini yürütmekteyiz. Bu kapsamda, öncelikle müvekkillerimizin kişisel veri işleme süreçlerinin analizini yaparak mevcut durumlarının tespit edilmesi, akabinde ise veri envanterinin hazırlanması, Veri Sorumluları Sicil Bilgi Sistemi’ne kayıt sürecinin yürütülmesi, veri işleme, saklama, anonim hale getirme ve imha politikalarının ve aydınlatma metinleri ile açık rıza beyan formlarının hazırlanması, gerekli idari ve teknik tedbirlerin alınması, veri sahiplerinin başvurularının cevaplanması, herhangi bir ihlal durumunda gerekli bildirimlerin yapılması, üçüncü kişiler ile imzalanacak sözleşmelerin hazırlanması ve revize edilmesi, ticari iletilere ilişkin uyum sürecinin tamamlanması, ulusal ve uluslararası gelişmelerin müvekkillerimize raporlanması ve şirket içi farkındalığı artırmak adına eğitim verilmesi gibi konularda müvekkillerimize hukuki danışmanlık sunmaktayız."
            ),
        ],
    },
    {
        "id": 5,
        "name": lazy_gettext("Fikri Mülkiyet Hukuku"),
        "icon": '<i class="fa-regular fa-copyright"></i>',
        "paragraphs": [
            lazy_gettext(
                "Helvacı Laik Aşar olarak, müvekkillerimize başta 5846 sayılı Fikir ve Sanat Eserleri Kanunu olmak üzere ilgili tüm mevzuat kapsamında fikri ve sınai haklarından en etkin şekilde yararlanmaları ve bu haklarını koruyabilmeleri için hukuki danışmanlık hizmeti sunmaktayız."
            ),
            lazy_gettext(
                "Fikri Mülkiyet Hukuku kapsamında; patent, faydalı model, marka, telif hakları, coğrafi işaretler, tasarım, internet alan adları, müzik, fotoğrafik eserler, edebiyat, mimari ve artistik eserler, sinematografik eserler, televizyon program formatları ve bilgisayar yazılımı ile veri tabanı gibi konuları kapsayacak şekilde danışmanlık hizmeti vermekteyiz. Bu çerçevede; fikri mülkiyet haklarına ilişkin sözleşmelerinin hazırlanması ve revize edilmesi ve fikri mülkiyet haklarının kullanılması ile devir işlemlerinin gerçekleştirilmesi gibi faaliyetleri yürütmekteyiz."
            ),
            lazy_gettext(
                "Ayrıca, müvekkillerimizin haklarının ihlal edildiği durumlarda tecavüzün önlenmesi, haksız rekabet, maddi ve manevi tazminat gibi davalarda müvekkillerimizi uyuşmazlık aşamalarında temsil etmekteyiz."
            ),
        ],
    },
    {
        "id": 6,
        "name": lazy_gettext("Şirketler ve Ticaret Hukuku"),
        "icon": '<i class="fa-solid fa-building-columns"></i>',
        "paragraphs": [
            lazy_gettext(
                "Ulusal ve uluslararası düzeyde faaliyet gösteren veya göstermeyi hedefleyen müvekkillerimize, şirket kuruluş ve sona erme işlemleri, şirket ana sözleşmesinin hazırlanması ve incelenmesi, hissedarlık, hisse devir veya iştirak sözleşmelerinin hazırlanması ve incelenmesi, genel kurul ve yönetim kurulu toplantılarının gerçekleştirilmesi, şirketlerin şube açılış işlemlerinin gerçekleştirilmesi, şirket imza sirküleri ile iç yönergelerinin hazırlanması, şirketin taraf olacağı alım-satım, kira, bayilik, acentelik, tedarik, dağıtım, franchise ve benzeri her türlü ticari sözleşmenin hazırlanması ve revize edilmesi, faaliyet alanlarına ilişkin mevzuata uyumun sağlanması ve faaliyet alanlarına ilişkin her türlü güncel gelişmenin raporlanması gibi konularda danışmanlık hizmeti sunmakta ve müvekkillerimizin kurumsallaşma süreçlerini yürütmekteyiz. Diğer taraftan, müvekkillerimizi; aralarında akdetmiş oldukları sözleşmeler, genel kurul toplantıları ve kararlarından ve 6102 sayılı Türk Ticaret Kanunu ile ilgili mevzuattan doğan haksız rekabete dayalı tazminat davaları, ortaklığın feshi gibi uyuşmazlıklarda arabuluculuk ve dava aşamalarında temsil etmekteyiz."
            )
        ],
    },
    {
        "id": 7,
        "name": lazy_gettext("Sözleşmeler Hukuku"),
        "icon": '<i class="fa-regular fa-handshake"></i>',
        "paragraphs": [
            lazy_gettext(
                "Helvacı Laik Aşar olarak; sözleşmelerin usul ve maddi hukuk kuralları gereğince uygulanabilirliği ve müvekkillerimizin talepleri doğrultusunda; taraf iradelerinin sağlıklı bir şekilde ifade edilmesi, sözleşmesel ilişkinin doğru bir şekilde tanımlanması, karşılıklı borç ve yükümlülüklerin belirlenmesi, sözleşmeye aykırı hareket edilmesi halinde doğacak sorumluluk ve sonuçların belirlenmesi açısından sözleşme müzakerelerinin yürütülmesi, sözleşmelerin hazırlanması ve revize edilmesi, sözleşmelere ilişkin hukuki risk analizlerinin yapılması ve raporlanması süreçlerinde danışmanlık hizmeti sunmakta ve müvekkillerimizi taraf oldukları sözleşmelerden doğan uyuşmazlıklarda temsil etmekteyiz."
            )
        ],
    },
    {
        "id": 8,
        "name": lazy_gettext("İdare ve Vergi Hukuku"),
        "icon": '<i class="fa-solid fa-scale-balanced"></i>',
        "paragraphs": [
            lazy_gettext(
                "Gerçek ve tüzel kişi müvekkillerimizi, idari otoriteler ile olan hukuki ilişkilerinde etkin bir şekilde temsil etmekteyiz. Bu kapsamda müvekkillerimize; idari düzenleme, tebliğ, kararname, rehber, kılavuz, karar, idari işlemler ve idari eylemler, imar, kamulaştırma ve kamu ihaleleri gibi konularda gerekli idari başvuruların yapılması aşamasında danışmanlık hizmeti vermekteyiz. Ayrıca, ilk derece mahkemelerinde ve Danıştay’da görülecek davalarda temsil etmekteyiz."
            ),
            lazy_gettext(
                "Vergi hukuku kapsamında ise, tahakkuk eden vergiler, bu vergiler kapsamında doğan vergi suçları, harç ve cezalarına ilişkin olarak hukuki danışmanlık hizmeti vermekte olduğumuz gibi aynı zamanda müvekkillerimizi doğacak uyuşmazlıklarda temsil etmekteyiz."
            ),
        ],
    },
    {
        "id": 9,
        "name": lazy_gettext("İş ve Sosyal Güvenlik Hukuku"),
        "icon": '<i class="fa-solid fa-briefcase"></i>',
        "paragraphs": [
            lazy_gettext(
                "Helvacı Laik Aşar olarak; müvekkillerimizin çalışanlarına sağladıkları çalışma koşullarının hukuka uygunluğunun denetlenmesi ve hukuka uygun hale getirilmesi; çalışanları ile girdikleri her türlü hukuki ilişki ve sürecin yürütülmesi ve muhtemel dava ile arabuluculuk süreçlerinde doğabilecek risklerin minimize edilmesi için önleyici hukuk hizmeti sağlamaktayız."
            ),
            lazy_gettext(
                "Danışmanlık hizmetimiz ile müvekkillerimizin mevcut iş sözleşmelerinin hukuka uygunluk denetiminin yapılması, yeniden düzenlenmesi, imzalanması ve sona erdirilmesi; iş hukuku ikincil metinlerinin hazırlanması; müvekkillerimizin çalışanlarına iş hukuku eğitimlerinin verilmesi ve çalışanların disiplin süreçlerinin yürütülmesi; iş kazası, meslek hastalığı ve sair hallerde müvekkillerimizin haklarının korunması kapsamındaki süreçleri yürütüyor ve tüm bu konulardan doğan uyuşmazlık aşamalarında aktif bir şekilde rol alıyoruz."
            ),
        ],
    },
    {
        "id": 10,
        "name": lazy_gettext("Uluslararası İlişkiler Hukuku"),
        "icon": '<i class="fa-solid fa-earth-americas"></i>',
        "paragraphs": [
            lazy_gettext(
                "Helvacı Laik Aşar olarak, sivil toplumun faaliyetlerinin desteklenmesinin ülkemiz ve dünyamızın geleceği için çok önemli olduğuna inanıyoruz. Bu inancımız doğrultusunda, ülkemizde faaliyet göstermek isteyen yerli ve yabancı sivil toplum kuruluşları ile, faaliyetlerinin hukuka uygun bir şekilde yürütülebilmesi için çalışıyoruz. Sivil Toplum Kuruluşlarının Türkiye’deki faaliyetlerinin Türk Hukuk sistemine uyum süreçleri, hukuken kurulabilmeleri ve devamlılıklarını sağlayabilmeleri için gerekli danışmanlık hizmetini sağlamaktayız. Sivil toplum kuruluşu olan müvekkillerimizin ihtiyaçları doğrultusunda, Dernekler Hukuku, İş hukuku, Kişisel Veri Hukuku, Şirketler Hukuku, Sözleşmeler Hukuku ve İdare Hukuku alanlarında mevzuata uyum süreçlerini yürütmekteyiz."
            )
        ],
    },
    {
        "id": 11,
        "name": lazy_gettext("Gayrimenkul ve Kat Mülkiyeti Hukuku"),
        "icon": '<i class="fa-solid fa-building"></i>',
        "paragraphs": [
            lazy_gettext(
                "Helvacı Laik Aşar olarak, müvekkillerimiz için, gayrimenkullerin hukuki incelemesinin yapılması ve raporlanması, gayrimenkul satış vaadi ve satış, kira, üst hakkı, intifa hakkı ve inşaat gibi gayrimenkul sözleşmelerinin hazırlanması ve revize edilmesi ve 634 sayılı Kat Mülkiyeti Kanunu kapsamında hukuki danışmanlık hizmeti vermekteyiz."
            ),
            lazy_gettext(
                "Müvekkillerimize sunmuş olduğumuz hukuki danışmanlık hizmeti yanında müvekkillerimizi; tapu iptali ve tescili, tahliye, tapu kaydının düzeltilmesi, müdahalenin önlenmesi ve haksız işgal tazminatı, ortaklığın giderilmesi, kamulaştırma ve benzeri hukuki uyuşmazlıklar ile 634 sayılı Kat Mülkiyeti Kanunu kapsamındaki uyuşmazlıklarda, mahkemeler ve ilgili kamu kurum ve kuruluşları nezdinde temsil etmekteyiz."
            ),
        ],
    },
    {
        "id": 12,
        "name": lazy_gettext("Yabancılar ve Vatandaşlık Hukuku"),
        "icon": '<i class="fa-solid fa-people-group"></i>',
        "paragraphs": [
            lazy_gettext(
                "Türkiye, yakın coğrafyasında ve kendi dinamikleri çerçevesinde yaşanan değişikliklerin etkisiyle göç alan bir ülke konumuna gelmiştir. Bu nedenle yabancıların Türkiye’deki hukuki statüleri ve hak ile yükümlülüklerinin belirlenmesi önemli bir hal almıştır. Helvacı Laik Aşar olarak; Türkiye’de bulunan yabancıların hak ve yükümlülüklerini ilgilendiren her türlü idari ve hukuki gelişmeyi takip etmekteyiz. Yabancıların Türkiye’de; oturma izni, çalışma izni, vatandaşlık ve gayrimenkul sahibi olması gibi konularda da bireysel ve kurumsal müvekkillerimize danışmanlık hizmeti vermekteyiz."
            )
        ],
    },
]

team_data = [
    {
        "id": 1,
        "name": "Av. Muhammed M. Helvacı",
        "title": lazy_gettext("Kurucu Avukat"),
        "city": "İstanbul",
        "img": "/static/images/mmh.jpeg",
        "email": "muhammed.helvaci@hla-law.com",
        "foreign-language": lazy_gettext("İngilizce"),
        "linkedin-url": "https://www.linkedin.com/in/muhammed-m-helvac%C4%B1-76685a174/",
        "url": "/team/mmh",
        "areas": [
            lazy_gettext("Elektronik Ticaret Hukuku"),
            lazy_gettext("Finans Teknolojileri Hukuku"),
            lazy_gettext("İdare ve Vergi Hukuku"),
            lazy_gettext("İş ve Sosyal Güvenlik Hukuku"),
            lazy_gettext("Kişisel Veri Hukuku"),
            lazy_gettext("Şirketler ve Ticaret Hukuku"),
            lazy_gettext("Sözleşmeler Hukuku"),
        ],
        "biography": [
            lazy_gettext(
                "Dijitalleşen dünyayı aktif olarak takip eden Muhammed; finans teknolojileri, elektronik ticaret ve kişisel veri hukuku alanlarında çalışmalar yapmaktadır. Helvacı Laik Aşar’dan önce ; e-ticaret, eğitim, medya, turizm, lojistik, inşaat, üretim gibi çeşitli sektörlerde faaliyet göstermekte olan şirketlere danışmanlık hizmeti sağlamış ve uyuşmazlık aşamalarında temsil etmiştir."
            ),
            lazy_gettext(
                "Bilişim ve internet teknolojileri hukukunun yanı sıra; sözleşmeler hukuku, şirketler ve ticaret hukuku, iş ve sosyal güvenlik hukuku, idare ve vergi hukuku alanlarında danışmanlık, dava ve uyuşmazlık çözüm yöntemleri aşamalarında avukatlık hizmeti vermeye devam etmektedir. Muhammed, yüksek lisans eğitimine devam etmekte olup çalışmalarını bilişim suçları üzerine yoğunlaştırmaktadır. İş, hukuk ve sosyal girişimcilik alanlarında faaliyet gösteren sivil toplum kuruluşlarında aktif olarak yer almaktadır."
            ),
        ],
        "education": [
            lazy_gettext("İstanbul Üniversitesi, Kamu Hukuku Yüksek Lisans"),
            lazy_gettext("İstanbul Üniversitesi, Yönetim Bilişim Sistemleri"),
            lazy_gettext("İstanbul Üniversitesi, Hukuk Fakültesi"),
            lazy_gettext("Kadıköy Anadolu Lisesi"),
        ],
    },
    {
        "id": 2,
        "name": "Av. Mustafa Tayfun Laik",
        "title": lazy_gettext("Kurucu Avukat"),
        "city": "İstanbul",
        "img": "/static/images/mtl.jpeg",
        "email": "mustafa.laik@hla-law.com",
        "foreign-language": lazy_gettext("İngilizce"),
        "linkedin-url": "https://www.linkedin.com/in/mtayfunlaik/",
        "url": "/team/mtl",
        "areas": [
            lazy_gettext("Bilişim ve İnternet Teknolojileri Hukuku"),
            lazy_gettext("Elektronik Ticaret Hukuku"),
            lazy_gettext("Finans Teknolojileri Hukuku"),
            lazy_gettext("İş ve Sosyal Güvenlik Hukuku"),
            lazy_gettext("Kişisel Veri Hukuku"),
            lazy_gettext("Uluslararası Kuruluşlar ve STK"),
            lazy_gettext("Yabancılar ve Vatandaşlık Hukuku"),
        ],
        "biography": [
            lazy_gettext(
                "Mustafa; finansal teknolojiler, kişisel verilerin korunması ve elektronik ticaret alanlarında çalışmalar yapmaktadır."
            ),
            lazy_gettext(
                "Helvacı Laik Aşar’ın kuruluşu öncesinde, ödeme ve elektronik para hizmetleri alanında Türkiye’nin ve Avrupa’nın önde gelen start-up’larından birisinde kariyerine başlayan Mustafa; uluslararası kuruluş ve sivil toplum örgütleri ile de yakından çalışmak fırsatı yakalamış ve bunların Türk hukukuna uyum süreçlerinde danışmanlık hizmeti vermiştir. Bu kapsamda daha çok; bilişim ve internet teknolojileri hukuku, iş ve sosyal güvenlik hukuku, uluslararası kuruluşlar, sivil toplum örgütleri, yabancılar ve vatandaşlık hukuku alanlarında danışmanlık ve dava avukatlığı yapmaktadır."
            ),
            lazy_gettext(
                "İş, girişimcilik ve hukuk dünyasını bir araya getiren, girişimcilik ekosistemini ve özellikle sosyal girişimciliği destekleyen sivil toplum kuruluşlarında yönetici ve üye olarak aktif görev almaktadır."
            ),
        ],
        "education": [
            lazy_gettext("İstanbul Üniversitesi, Yönetim Bilişim Sistemleri"),
            lazy_gettext("İstanbul Üniversitesi, Hukuk Fakültesi"),
            lazy_gettext("Kadıköy Anadolu Lisesi"),
        ],
    },
    {
        "id": 3,
        "name": "Av. Doğukan Aşar",
        "title": lazy_gettext("Kurucu Avukat"),
        "city": "İstanbul",
        "img": "/static/images/da.jpeg",
        "email": "dogukan.asar@hla-law.com",
        "foreign-language": lazy_gettext("İngilizce"),
        "linkedin-url": "https://www.linkedin.com/in/do%C4%9Fukan-a%C5%9Far-443068154/",
        "url": "/team/da",
        "areas": [
            lazy_gettext("Elektronik Ticaret Hukuku"),
            lazy_gettext("Fikri Mülkiyet Hukuku"),
            lazy_gettext("Finans Teknolojileri Hukuku"),
            lazy_gettext("Gayrimenkul ve Kat Mülkiyeti Hukuku"),
            lazy_gettext("Kişisel Veri Hukuku"),
            lazy_gettext("Şirketler ve Ticaret Hukuku"),
            lazy_gettext("Sözleşmeler Hukuku"),
        ],
        "biography": [
            lazy_gettext(
                "Doğukan; bilişim ve internet teknolojileri ile fikri mülkiyet hukuku alanlarında çalışmalar yapmaktadır. Kariyeri boyunca ödeme hizmetleri, e-ticaret, medya, eğitim, tekstil ve gayrimenkul alanlarında, ulusal ve uluslararası faaliyet göstermekte olan şirketlere avukatlık ve danışmanlık hizmeti sunmuştur."
            ),
            lazy_gettext(
                "Doğukan; finansal teknolojiler hukuku, kişisel veri hukuku ve elektronik ticaret hukuku alanlarında, kurumsal müvekkillerinin hukuka uyum süreçlerini yürütürken; gayrimenkul hukuku, şirketler ve ticaret hukuku, sözleşmeler hukuku ve fikri mülkiyet hukuku alanlarında, davalarda edinmiş olduğu uygulamaya yönelik tecrübelerinden faydalanarak, danışmanlık, dava ve uyuşmazlık çözüm yöntemleri aşamalarında avukatlık hizmeti vermeye devam etmektedir."
            ),
            lazy_gettext(
                "Doğukan; girişimcilik ve iş alanında faaliyet gösteren sivil toplum kuruluşlarında yönetici ve üye sıfatları ile aktif olarak çalışmalar yapmaktadır."
            ),
        ],
        "education": [
            lazy_gettext("İstanbul Üniversitesi, Yönetim Bilişim Sistemleri"),
            lazy_gettext("İstanbul Üniversitesi, Hukuk Fakültesi"),
            lazy_gettext("Hayrullah Kefoğlu Anadolu Lisesi"),
        ],
    },
]

news_data = [
    {
        "id": 0,
        "title": lazy_gettext(
            "Ödeme ve Elektronik Para Kuruluşlarının Asgari Öz Sermaye Yükümlülüğü Tutarlarının Artırılmasına Yönelik TCMB Tebliği Hakkında Duyuru"
        ),
        "date": "14.02.2022",
        "content": lazy_gettext(
            """
<div class="content">
    <p>22.01.2022 tarihli Resmi Gazete'de yayımlanan tebliğ ile Türkiye Cumhuriyeti Merkez Bankası (“TCMB”) tarafından ödeme ve elektronik para kuruluşlarının asgari öz sermaye yükümlülüğü tutarları arttırılmıştır.</p>
    <p>Ödeme Hizmetleri ve Elektronik Para İhracı ile Ödeme Hizmeti Sağlayıcıları Hakkında Yönetmelik kapsamında TCMB, ödeme ve elektronik para kuruluşlarının asgari özkaynak yükümlülüğü için belirlenen tutarları, Türkiye İstatistik Kurumu tarafından yayımlanan fiyat endekslerindeki yıllık değişimler göz önünde bulundurularak her yıl Ocak ayında tekrar değerlendirme yetkisine sahiptir.</p>
    <p>Tebliğ ile;</p>
    <ul>
        <li>Fatura ödemelerine aracılık edilmesine yönelik hizmetler sunan ödeme kuruluşları için asgari öz sermaye yükümlülüğü tutarı 3 milyon TL'den 5.5 milyon TL'ye,</li>
        <li>Münhasıran ödeme hesabına ilişkin bilgilerin çevrim içi platformlarda sunulması hizmetini sunanlar hariç olmak üzere diğer ödeme kuruluşları için asgari öz sermaye yükümlülüğü tutarı 5 milyon TL'den 9 milyon TL'ye ve,</li>
        <li>Elektronik para kuruluşları için asgari öz sermaye yükümlülüğü tutarı 13 milyon TL'den 25 milyon TL'ye yükseltilmiştir.</li>
    </ul>
    <p>Ödeme ve elektronik para kuruluşlarının yeni yükümlülükleri 1 Nisan 2022 tarihinde yürürlüğe girecektir. Tebliğe <a target="_blank" href="https://www.resmigazete.gov.tr/eskiler/2022/01/20220122-21.htm">buradan</a> ulaşabilirsiniz.</p>
</div>
"""
        ),
        "news_link": "https://www.resmigazete.gov.tr/eskiler/2022/01/20220122-21.htm",
        "tag": lazy_gettext("Finans Teknolojileri Hukuku"),
    },
    {
        "id": 1,
        "title": lazy_gettext(
            "TCMB Tarafından FAST ve TR Karekod Sistemlerinin Kullanılması Hakkında Basın Duyurusu"
        ),
        "date": "14.02.2022",
        "content": lazy_gettext(
            """
<div class="content">
    <p>Türkiye Cumhuriyet Merkez Bankası (TCMB) 14.02.2022 tarihinde, FAST (Fonların Anlık ve Sürekli Transferi) ve TR Karekod kullanılarak yapılacak para transferlerine yönelik basın duyurusu yayınlamıştır.</p>
    <p>Söz konusu basın duyurusuna göre:</p>
    <ul>
        <li>“TR Karekod” kullanılarak gerçekleştirilecek iş yeri ödemelerinde tek seferde 10.000 TL’ye kadar işlem yapılabilecektir.</li>
        <li>Para transferlerinde 2.000 TL olan FAST işlem tutar limiti, 21.02.2022 tarihi itibarıyla 5.000 TL’ye yükseltilecektir.</li>
    </ul>
    <p>Bununla beraber, FAST aracılığıyla yapılan ödeme miktarının günlük ortalama 3,5 milyona; hızlı bir şekilde FAST ödemesi yapılabilmesine olanak sağlayan Kolay Adresleme Sistemine kaydolan kullanıcı sayısının ise 15,5 milyona ulaşmış olduğu da belirtilmiştir.</p>
    <p>Basın duyurusuna <a target="_blank" href="https://www.tcmb.gov.tr/wps/wcm/connect/TR/TCMB+TR/Main+Menu/Duyurular/Basin/2022/DUY2022-13">buradan</a> ulaşabilirsiniz.</p>
</div>
"""
        ),
        "news_link": "https://www.tcmb.gov.tr/wps/wcm/connect/TR/TCMB+TR/Main+Menu/Duyurular/Basin/2022/DUY2022-13",
        "tag": lazy_gettext("Finans Teknolojileri Hukuku"),
    },
    {
        "id": 2,
        "title": lazy_gettext(
            "MASAK Tarafından Kripto Varlık Hizmet Sağlayıcılara Yönelik Şüpheli İşlem Bildirimi Rehberi’nin Yayımlanması"
        ),
        "date": "18.04.2022",
        "content": lazy_gettext(
            """
<div class="content">
    <p>MASAK tarafından, kripto varlık hizmet sağlayıcıların elektronik ortamda şüpheli işlem bildirimi gönderebilmelerine ilişkin usul ve esasların düzenlenmesi amacı ile “Şüpheli İşlem Bildirimi Rehberi” (“Rehber”) yayımlanmıştır.</p>
    <p>Rehber içerisinde öncelikle şüpheli işlem bildirimlerinin elektronik ortamda gönderimine dair süreçler anlatılmış, daha sonra şüpheli işlem bildirim formlarının nasıl düzenleneceğine dair detaylı bilgilere yer verilmiştir.</p>
    <p>Kripto varlık hizmet sağlayıcılar, 18/04/2022 tarihinden itibaren şüpheli işlem bildirimlerini Rehber’de belirtilen esas ve usuller çerçevesinde göndereceklerdir.</p>
    <p>Şüpheli işlemler, yükümlüler tarafından; şüpheli işlemin gerçekleştiğine ilişkin şüphenin oluştuğu tarihten itibaren en geç on iş günü içinde MASAK Başkanlığı’na bildireceklerdir.</p>
    <p>Rehber ve ilgili formlara <a target="_blank" href="https://ms.hmb.gov.tr/uploads/sites/12/2022/04/KVHS-Rehberi-16.04.2022.pdf">buradan</a> ulaşabilirsiniz.</p>
</div>
"""
        ),
        "news_link": "https://ms.hmb.gov.tr/uploads/sites/12/2022/04/KVHS-Rehberi-16.04.2022.pdf",
        "tag": lazy_gettext("Finans Teknolojileri Hukuku"),
    },
    {
        "id": 3,
        "title": lazy_gettext(
            "Bankacılık Düzenleme ve Denetleme Kurumu Tarafından İlk Dijital Banka Kuruluş İzninin Verilmesi"
        ),
        "date": "22.04.2022",
        "content": lazy_gettext(
            """
<div class="content">
    <p>22.04.2022 tarihli Resmi Gazete’de yayımlanan Bankacılık Düzenleme ve Denetleme Kurulu’nun 21.04.2022 tarihli kararı ile Bankacılık Düzenleme ve Denetleme Kurumu (“BDDK”) tarafından ilk dijital bankacılık izni verilmiştir.</p>
    <p>Söz konusu karara göre BDDK tarafından; Hayat Holding A.Ş., Hayat Kimya Sanayi A.Ş., As Tüketim Malları Ticaret A.Ş., Kastamonu Entegre Ağaç Sanayi ve Ticaret A.Ş., ve Limaş Liman İşletmeciliği A.Ş.'nin ortaklığında, 1.5 milyar TL sermayeli ve Hayat Katılım Bankası A.Ş. unvanlı dijital katılım bankası kurulmasına izin verilmiştir.</p>
    <p>Dijital Bankaların Faaliyet Esasları ile Servis Modeli Bankacılığı Hakkında Yönetmelik (“Yönetmelik”) 01.01.2022 tarihinde yürürlüğe girmişti. Yönetmelik kapsamında dijital banka; bankacılık hizmetlerini fiziksel şubeler yerine elektronik bankacılık hizmetleri dağıtım kanalları aracılığıyla sunan kredi kuruluşu şeklinde tanımlanmıştı.</p>
    <p>Yönetmelik’in yürürlüğe girmesi ile birlikte, Hayat Katılım Bankası A.Ş., elektronik hizmet dağıtım kanalları aracılığı ile uzaktan bankacılık faaliyetleri gösterebilecek ilk şubesiz katılım bankası olarak dijital bankacılık izni almış bulunmaktadır.</p>
    <p>Dijital Bankaların Faaliyet Esasları ile Servis Modeli Bankacılığı Hakkında Yönetmelik’e <a target="_blank" href="https://www.resmigazete.gov.tr/eskiler/2021/12/20211229-6.htm">buradan</a> ulaşabilirsiniz.</p>
</div>
"""
        ),
        "news_link": "https://www.resmigazete.gov.tr/eskiler/2021/12/20211229-6.htm",
        "tag": lazy_gettext("Finans Teknolojileri Hukuku"),
    },
]

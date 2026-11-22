import json, sys
def r(nom,url,fr,en,ar,ber): return dict(nom=nom,url=url,desc=dict(fr=fr,en=en,ar=ar,ber=ber))
RES = dict(
 logiciels=[
  r("QGIS","https://qgis.org","SIG libre et gratuit (choisir la version LTR) : cartes et inventaires des espaces verts.","Free open-source GIS (choose the LTR version): green-space maps and inventories.","نظام معلومات جغرافية حر ومجاني (اختر إصدار LTR): خرائط وجرد المساحات الخضراء.","SIG ilelli u baṭel (fren lqem LTR)."),
  r("QField","https://qfield.org","Application mobile gratuite pour les relevés de terrain (inventaire des arbres) avec QGIS.","Free mobile app for field surveys (tree inventory) with QGIS.","تطبيق مجاني للهاتف لجمع البيانات الميدانية (جرد الأشجار) مع QGIS.","Asnas n tiliɣri i uxeddim deg wakal, s QGIS."),
  r("KoboToolbox","https://www.kobotoolbox.org","Formulaires d'enquête et de relevé gratuits, utilisables hors connexion.","Free survey and data-collection forms, usable offline.","استمارات مجانية للتحقيقات وجمع البيانات تعمل دون اتصال.","Tiferkiwin n usteqsi baṭel, war tuqqna."),
  r("Pl@ntNet","https://plantnet.org","Identifier une plante à partir d'une photo (à vérifier avec un second critère).","Identify a plant from a photo (check with a second criterion).","التعرف على نبات من صورة (تحقق بمعيار ثانٍ).","Issin imɣi seg tugna."),
  r("Sweet Home 3D","https://www.sweethome3d.com","Logiciel gratuit pour esquisser un aménagement en 2D/3D.","Free software to sketch a layout in 2D/3D.","برنامج مجاني لرسم تهيئة أولية ثنائية وثلاثية الأبعاد.","Aseɣzan baṭel i usuneɣ s 2D/3D."),
  r("LibreOffice","https://www.libreoffice.org","Suite bureautique gratuite : tableur pour les devis et les calculs d'arrosage.","Free office suite: spreadsheet for estimates and irrigation calculations.","حزمة مكتبية مجانية: جداول للكشوف وحسابات السقي.","Tagrumma n lebiru baṭel."),
 ],
 donnees=[
  r("Copernicus Browser","https://browser.dataspace.copernicus.eu","Images Sentinel-2 gratuites (10 m) pour calculer le NDVI.","Free Sentinel-2 imagery (10 m) to compute NDVI.","صور Sentinel-2 مجانية (10 م) لحساب NDVI.","Tugniwin Sentinel-2 baṭel i NDVI."),
  r("OpenStreetMap","https://www.openstreetmap.org","Carte libre : parcs, rues, bâtiments ; fond de carte dans QGIS.","Free map: parks, streets, buildings; basemap in QGIS.","خريطة حرة: حدائق وشوارع ومبانٍ؛ خلفية في QGIS.","Takarḍa tilellit: tibḥirin, iberdan."),
  r("GBIF","https://www.gbif.org","Observations d'espèces (arbres, oiseaux) dans le monde et en Algérie.","Species occurrences (trees, birds) worldwide and in Algeria.","مشاهدات الأنواع (أشجار، طيور) في العالم والجزائر.","Tiwalin n telmas deg umaḍal."),
  r("Journal officiel (JORADP)","https://www.joradp.dz","Textes officiels algériens, dont la loi n° 07-06 sur les espaces verts.","Algerian official texts, including Law 07-06 on green spaces.","النصوص الرسمية الجزائرية، ومنها القانون 07-06 المتعلق بالمساحات الخضراء.","Iḍrisen unṣiben n Lezzayer."),
  r("Euro+Med PlantBase","https://europlusmed.org","Noms scientifiques valides des plantes de la région méditerranéenne.","Valid scientific names of Mediterranean plants.","الأسماء العلمية الصحيحة لنباتات حوض المتوسط.","Ismawen usnanen n yimɣan."),
 ],
 apprendre=[
  r("Plante & Cité","https://www.plante-et-cite.fr","Centre technique français des espaces verts : fiches, guides, retours d'expérience.","French technical centre for green spaces: sheets, guides, case studies.","المركز التقني الفرنسي للمساحات الخضراء: بطاقات وأدلة وتجارب.","Ammas atiknik n tallunin tizegzawin."),
  r("Documentation QGIS","https://docs.qgis.org","Manuel officiel de QGIS, en français et en anglais.","Official QGIS manual, in French and English.","الدليل الرسمي لـ QGIS بالفرنسية والإنجليزية.","Adlis unṣib n QGIS."),
  r("Tela Botanica","https://www.tela-botanica.org","Réseau de botanistes francophones : fiches espèces, outils d'identification.","French-speaking botanists' network: species sheets, identification tools.","شبكة علماء النبات الناطقين بالفرنسية: بطاقات الأنواع وأدوات التعرف.","Azeṭṭa n yimusnawen n yimɣan."),
 ],
 glossaire=[
  ["Espace vert","Green space","مساحة خضراء"],["Parc urbain","Urban park","حظيرة حضرية"],["Jardin public","Public garden","حديقة عمومية"],
  ["Alignement d'arbres","Tree alignment / street trees","صف أشجار"],["Forêt urbaine","Urban forest","غابة حضرية"],["Trame verte","Green network / green corridor","شبكة خضراء"],
  ["Service écosystémique","Ecosystem service","خدمة إيكولوجية"],["Îlot de chaleur urbain","Urban heat island","جزيرة حرارية حضرية"],["Évapotranspiration","Evapotranspiration","التبخر-النتح"],
  ["Canopée","Canopy","الغطاء الشجري"],["Taux de canopée","Canopy cover","نسبة الغطاء الشجري"],["Nom scientifique","Scientific name","الاسم العلمي"],
  ["Genre / espèce","Genus / species","الجنس / النوع"],["Cultivar","Cultivar","صنف مزروع"],["Feuillage persistant","Evergreen foliage","أوراق دائمة الخضرة"],
  ["Feuillage caduc","Deciduous foliage","أوراق متساقطة"],["Port (d'un arbre)","Habit / form","الشكل العام (للشجرة)"],["Strate arbustive","Shrub layer","الطبقة الشجيرية"],
  ["Couvre-sol","Ground cover","نبات مغطٍّ للتربة"],["Palette végétale","Plant palette","تشكيلة نباتية"],["Espèce envahissante","Invasive species","نوع غازٍ"],
  ["Inventaire du patrimoine arboré","Tree inventory","جرد رصيد الأشجار"],["Circonférence à 1,30 m","Girth at breast height","المحيط على ارتفاع 1,30 م"],["Diamètre","Diameter","القطر"],
  ["Houppier / couronne","Crown","التاج"],["Collet","Root collar","العنق (عنق الجذر)"],["Clinomètre","Clinometer","مقياس الميل"],
  ["Diagnostic sanitaire","Health assessment","التشخيص الصحي"],["Cavité","Cavity","تجويف"],["Écorce incluse","Included bark","لحاء محصور"],
  ["Bois mort","Deadwood","خشب ميت"],["Abattage","Felling","قطع (الشجرة)"],["Plan de masse","Master plan / site plan","المخطط الكتلي"],
  ["Programme d'aménagement","Design brief","برنامج التهيئة"],["Allée","Path","ممر"],["Aire de jeux","Playground","فضاء لعب"],
  ["Sol amortissant","Impact-absorbing surface","أرضية ماصة للصدمات"],["Terre végétale","Topsoil","تربة زراعية"],["Fosse de plantation","Planting pit","حفرة الغرس"],
  ["Tuteur","Stake","دعامة"],["Paillage","Mulch / mulching","التغطية (النشارة)"],["Racines nues","Bare root","جذور عارية"],
  ["Goutte-à-goutte","Drip irrigation","السقي بالتقطير"],["Aspersion","Sprinkler irrigation","السقي بالرش"],["Hydrozone","Hydrozone","منطقة مائية"],
  ["Xéropaysagisme","Xeriscaping","البستنة الجافة"],["Gestion différenciée","Differentiated management","التسيير المتمايز"],["Taille de formation","Formative pruning","تقليم التكوين"],
  ["Étêtage","Topping","التطويش (قطع الرأس)"],["Col de la branche","Branch collar","طوق الغصن"],["Lutte intégrée","Integrated pest management","المكافحة المتكاملة"],
  ["Processionnaire du pin","Pine processionary moth","دودة الصنوبر الجرارة"],["Compost","Compost","سماد عضوي (كومبوست)"],["Zone tampon","Buffer","منطقة عازلة"],
  ["NDVI","NDVI (vegetation index)","مؤشر الغطاء النباتي NDVI"],["Métré","Bill of quantities","كشف الكميات"],["Devis estimatif","Cost estimate","الكشف التقديري"],
  ["Prix unitaire","Unit price","السعر الوحدوي"],["Plan de gestion","Management plan","مخطط التسيير"],["Cahier des charges","Specifications","دفتر الشروط"],
  ["Participation citoyenne","Public participation","مشاركة المواطنين"],["Jardin partagé","Community garden","حديقة مشتركة"],
 ])
h="""/*
 * RESSOURCES GRATUITES ET GLOSSAIRE — Espaces verts ENIV
 * Pour ajouter un lien : copiez un bloc { nom, url, desc } dans la bonne liste.
 * desc : description en fr (obligatoire), en, ar et ber (facultatives : le français s'affiche sinon).
 * Glossaire : un terme par ligne, en français, anglais et arabe.
 */
window.RESSOURCES = """
open(sys.argv[1],"w",encoding="utf-8").write(h+json.dumps(RES,ensure_ascii=False,indent=1)+";\n")
print(len(RES["glossaire"]),"termes")

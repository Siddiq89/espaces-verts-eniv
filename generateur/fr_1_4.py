from outils import C, lecon, q

N1 = dict(id="v1", numero=1, titre="Comprendre les espaces verts urbains", echelle="1:25 000",
  resume="Définir et classer les espaces verts, connaître leurs rôles pour la ville et ses habitants, et situer le cadre réglementaire et les acteurs en Algérie.",
  lecons=[
  lecon("v1-l1", "Qu'est-ce qu'un espace vert ? Définitions et typologie", "20 min",
    ["Définir un espace vert urbain et ses composantes",
     "Distinguer les grandes catégories d'espaces verts",
     "Reconnaître ces catégories dans une ville comme Tlemcen"],
    """
<p>Un <b>espace vert</b> est un espace, public ou privé, en grande partie couvert de végétation (arbres, arbustes, pelouses, fleurs), aménagé ou non, situé dans la ville ou à sa périphérie. Il peut être grand (un parc, une forêt urbaine) ou très petit (une jardinière, une rangée d'arbres le long d'un boulevard).</p>
<p>Un espace vert est toujours un <b>système vivant</b> : du sol, de l'eau, des végétaux, de la faune (oiseaux, insectes, hérissons), des équipements (allées, bancs, jeux, éclairage) et des <b>usagers</b>. Le gérer, c'est s'occuper de tout cela à la fois.</p>
<h4>Les grandes catégories</h4>
<p>La loi algérienne de 2007 sur les espaces verts (voir la leçon 3) distingue plusieurs catégories. Elles sont utiles pour organiser un inventaire :</p>
<ul>
  <li><b>Parcs urbains et périurbains</b> : grands espaces (souvent plus de quelques hectares) avec promenades, aires de jeux, plans d'eau, accueil du public.</li>
  <li><b>Jardins publics</b> : espaces plus petits, de quartier : squares, placettes plantées, jardins de cité.</li>
  <li><b>Jardins spécialisés</b> : jardin botanique, roseraie, jardin d'exposition, arboretum.</li>
  <li><b>Jardins collectifs ou résidentiels</b> : espaces verts au pied des immeubles, des écoles, des hôpitaux.</li>
  <li><b>Jardins particuliers</b> : jardins privés des maisons.</li>
  <li><b>Forêts urbaines</b> : boisements dans ou contre la ville, ouverts à la promenade.</li>
  <li><b>Alignements boisés</b> : arbres plantés le long des rues, boulevards et routes.</li>
</ul>
<p>On ajoute souvent les <b>espaces verts d'accompagnement</b> (talus, ronds-points, terre-pleins centraux) et les <b>espaces naturels</b> (berges d'oued, friches, coteaux) qui jouent aussi un grand rôle écologique.</p>
<h4>Exemples autour de Tlemcen</h4>
<p>Le plateau de Lalla Setti (forêt et espace de loisirs dominant la ville), les jardins publics du centre-ville, les alignements de micocouliers et de platanes des grands boulevards, les oliveraies et vergers périurbains : chaque type demande une gestion différente.</p>
<div class="astuce"><b>À retenir :</b> classer les espaces verts par catégorie est la première étape de tout diagnostic. Sans typologie, on ne peut ni compter, ni comparer, ni planifier l'entretien.</div>""",
    """<ol>
  <li>Sur un plan de votre ville (ou sur Google Earth), repérez au moins un exemple de chaque catégorie.</li>
  <li>Pour chaque exemple, notez : nom, catégorie, surface approximative, quartier.</li>
  <li>Ouvrez la couche <code>espaces_verts.geojson</code> du TP dans QGIS et regardez le champ <code>categorie</code> : quelles catégories sont représentées dans la zone d'étude fictive ?</li>
</ol>"""),
  lecon("v1-l2", "Les rôles des espaces verts : services écosystémiques", "25 min",
    ["Citer les services rendus par les espaces verts",
     "Expliquer le rôle des arbres contre les îlots de chaleur",
     "Connaître les principaux indicateurs (m² par habitant, règle 3-30-300)"],
    """
<p>Les espaces verts ne sont pas un « décor ». Ils rendent à la ville des <b>services écosystémiques</b>, c'est-à-dire des bénéfices gratuits apportés par la nature.</p>
<h4>Services de régulation</h4>
<ul>
  <li><b>Climat local</b> : l'ombre des arbres et l'évapotranspiration des feuilles rafraîchissent l'air. Sous un grand arbre, la température ressentie en été peut baisser de plusieurs degrés. Les espaces verts réduisent les <b>îlots de chaleur urbains</b> (quartiers minéraux beaucoup plus chauds que leurs alentours).</li>
  <li><b>Eau</b> : un sol végétalisé infiltre la pluie, réduit le ruissellement et les inondations, recharge les nappes.</li>
  <li><b>Air et bruit</b> : le feuillage retient une partie des poussières ; les haies épaisses atténuent un peu le bruit et coupent le vent.</li>
  <li><b>Sol</b> : les racines retiennent la terre sur les talus et coteaux (lutte contre l'érosion).</li>
</ul>
<h4>Services de support et biodiversité</h4>
<p>Arbres, haies et prairies offrent abri et nourriture aux oiseaux, aux insectes pollinisateurs et à la petite faune. Reliés entre eux (alignements, berges d'oued), ils forment une <b>trame verte</b> qui permet aux espèces de circuler.</p>
<h4>Services culturels et sociaux</h4>
<p>Détente, sport, jeux d'enfants, rencontres, santé physique et mentale, éducation à l'environnement, valeur des logements, identité et paysage de la ville.</p>
<h4>Quelques indicateurs</h4>
<ul>
  <li><b>Surface d'espaces verts par habitant</b> (m²/hab) : surface totale des espaces verts publics ÷ population. Une valeur souvent citée (attribuée à l'OMS) est d'au moins <b>9 m² par habitant</b> ; beaucoup de villes visent 10 à 15 m².</li>
  <li><b>Taux de canopée</b> : part de la surface couverte par la couronne des arbres, vue du ciel.</li>
  <li><b>Règle 3-30-300</b> : chaque habitant devrait voir au moins <b>3 arbres</b> depuis son logement, vivre dans un quartier avec <b>30 %</b> de canopée, et habiter à moins de <b>300 m</b> d'un espace vert.</li>
</ul>
<div class="astuce"><b>Calcul rapide :</b> un quartier de 12 000 habitants avec 7,2 ha d'espaces verts publics dispose de 72 000 ÷ 12 000 = <b>6 m²/hab</b>, en dessous du repère de 9 m²/hab.</div>""",
    """<ol>
  <li>Choisissez un espace vert que vous connaissez et classez ses bénéfices dans les trois familles (régulation, biodiversité, social).</li>
  <li>Avec le fichier <code>quartiers_population.csv</code> du TP, calculez la surface d'espaces verts par habitant d'un quartier dont vous connaissez la surface d'espaces verts (champ <code>surface_ev_m2</code>).</li>
  <li>Le quartier atteint-il 9 m²/hab ? Combien de m² faudrait-il créer pour l'atteindre ?</li>
</ol>"""),
  lecon("v1-l3", "Cadre réglementaire et acteurs en Algérie", "20 min",
    ["Connaître la loi n° 07-06 du 13 mai 2007 relative aux espaces verts",
     "Identifier les acteurs de la création et de la gestion des espaces verts",
     "Savoir où trouver les textes officiels"],
    """
<p>En Algérie, le texte de référence est la <b>loi n° 07-06 du 13 mai 2007 relative à la gestion, à la protection et au développement des espaces verts</b>, publiée au Journal officiel (JORADP). Elle a pour objectifs principaux :</p>
<ul>
  <li>d'améliorer le cadre de vie urbain et de développer les espaces verts dans chaque ville ;</li>
  <li>de <b>classer</b> les espaces verts par catégories (celles vues en leçon 1) ;</li>
  <li>de <b>protéger</b> les espaces verts classés contre les changements d'affectation et les dégradations ;</li>
  <li>d'imposer la prise en compte des espaces verts dans les <b>instruments d'urbanisme</b> (PDAU, POS) et dans les projets de construction.</li>
</ul>
<p>Des textes d'application précisent les modalités (classement, gestion, cahiers des charges). Ils évoluent : vérifiez toujours la version en vigueur sur le site du Journal officiel.</p>
<h4>Les acteurs</h4>
<ul>
  <li><b>La commune (APC)</b> : gestion et entretien de la plupart des espaces verts publics, souvent par un service des espaces verts ou une entreprise communale.</li>
  <li><b>La wilaya</b> : direction de l'environnement, direction de l'urbanisme, financement de projets.</li>
  <li><b>La conservation des forêts</b> : forêts périurbaines et récréatives.</li>
  <li><b>Les entreprises et bureaux d'études</b> : conception, travaux de plantation, entretien sous contrat.</li>
  <li><b>Les associations et les habitants</b> : plantations, sensibilisation, jardins partagés, signalement des dégradations.</li>
</ul>
<h4>Les documents d'urbanisme</h4>
<p>Le <b>PDAU</b> (plan directeur d'aménagement et d'urbanisme) fixe les grandes orientations à l'échelle de la commune, le <b>POS</b> (plan d'occupation des sols) précise les règles par secteur. C'est dans ces documents qu'on réserve des terrains pour les futurs parcs et qu'on fixe les surfaces de verdure exigées.</p>
<div class="astuce"><b>Bon réflexe :</b> avant tout projet, demandez le POS du secteur et repérez les espaces verts existants ou prévus. Un espace vert classé ne peut pas devenir un parking ou un terrain à bâtir.</div>""",
    """<ol>
  <li>Cherchez la loi n° 07-06 du 13 mai 2007 sur le site du Journal officiel (joradp.dz) et relevez la liste exacte des catégories d'espaces verts.</li>
  <li>Faites un schéma des acteurs de votre commune : qui conçoit, qui finance, qui entretient, qui contrôle ?</li>
  <li>En une demi-page, expliquez à un élu pourquoi un espace vert classé doit être protégé.</li>
</ol>"""),
  ],
  quiz=[
    q("Selon la loi n° 07-06, une rangée d'arbres le long d'un boulevard appartient à quelle catégorie ?", ["Les alignements boisés", "Les jardins spécialisés", "Les parcs urbains", "Les jardins particuliers"], 0, "Les arbres d'alignement des rues et routes forment la catégorie des alignements boisés."),
    q("Un quartier de 20 000 habitants a 12 ha d'espaces verts publics. Combien de m² par habitant ?", ["0,6 m²/hab", "6 m²/hab", "60 m²/hab", "16 m²/hab"], 1, "12 ha = 120 000 m² ; 120 000 ÷ 20 000 = 6 m²/hab."),
    q("Que signifie le « 300 » de la règle 3-30-300 ?", ["300 arbres par quartier", "300 m au plus jusqu'à un espace vert", "300 m² de pelouse par école", "300 litres d'eau par arbre"], 1, "Chaque habitant devrait habiter à moins de 300 m d'un espace vert."),
    q("Comment les arbres réduisent-ils les îlots de chaleur ?", ["Par l'ombre et l'évapotranspiration", "En absorbant le bruit", "En augmentant le ruissellement", "En réfléchissant la lumière des lampadaires"], 0, "L'ombre et l'eau évaporée par les feuilles rafraîchissent l'air."),
    q("Quel document d'urbanisme précise les règles d'occupation des sols secteur par secteur ?", ["Le PDAU", "Le POS", "Le cahier des charges d'entretien", "L'inventaire des arbres"], 1, "Le POS précise, à l'échelle du secteur, ce que fixe le PDAU à l'échelle de la commune."),
  ])

N2 = dict(id="v2", numero=2, titre="Le végétal en milieu urbain", echelle="1:20",
  resume="Nommer et reconnaître les plantes, connaître les strates et les ports, choisir une palette végétale adaptée au climat de Tlemcen.",
  lecons=[
  lecon("v2-l1", "Nommer les plantes : bases de botanique appliquée", "20 min",
    ["Écrire correctement un nom scientifique",
     "Distinguer les strates de végétation",
     "Décrire une plante : feuillage, port, taille adulte"],
    """
<p>Un même arbre peut avoir plusieurs noms communs selon les régions (en français, en arabe, en tamazight). Pour éviter les erreurs dans un inventaire ou une commande de pépinière, on utilise le <b>nom scientifique</b>, en latin, valable dans le monde entier.</p>
<h4>Le nom scientifique</h4>
<ul>
  <li>Il comporte deux mots : le <b>genre</b> (majuscule) et l'<b>espèce</b> (minuscule), écrits en <i>italique</i> : <i>Pinus halepensis</i> (pin d'Alep), <i>Olea europaea</i> (olivier).</li>
  <li>On peut ajouter un <b>cultivar</b> entre apostrophes : <i>Nerium oleander</i> 'Album' (laurier-rose à fleurs blanches).</li>
  <li>La <b>famille</b> regroupe les genres apparentés : Pinaceae, Oleaceae, Fabaceae…</li>
</ul>
<h4>Les strates</h4>
<ul>
  <li><b>Arborée</b> : arbres, plus de 7 à 8 m à l'âge adulte.</li>
  <li><b>Arbustive</b> : arbustes et arbrisseaux, de 1 à 7 m (haies, massifs).</li>
  <li><b>Herbacée</b> : gazon, prairie, vivaces, plantes annuelles à fleurs.</li>
  <li><b>Couvre-sols et grimpantes</b> : plantes rampantes qui couvrent le sol, plantes qui montent sur les murs et pergolas.</li>
</ul>
<p>Un espace vert agréable et riche en biodiversité combine plusieurs strates.</p>
<h4>Décrire une plante</h4>
<ul>
  <li><b>Feuillage</b> : persistant (garde ses feuilles l'hiver) ou caduc (les perd).</li>
  <li><b>Port</b> : forme générale : érigé, étalé, pleureur, colonnaire, en boule.</li>
  <li><b>Taille adulte</b> : hauteur et largeur après 20 à 30 ans. C'est elle qui décide de la distance de plantation par rapport aux façades et aux réseaux.</li>
  <li><b>Exigences</b> : soleil ou ombre, eau, type de sol, résistance au froid et au vent.</li>
</ul>
<div class="astuce"><b>Erreur fréquente :</b> planter un arbre en fonction de sa taille à l'achat. Un pin d'Alep de 2 m en pépinière dépassera 15 m : il ne doit pas être planté à 2 m d'une façade.</div>""",
    """<ol>
  <li>Choisissez 5 arbres de votre quartier ou de l'école. Pour chacun, relevez le nom commun, le nom scientifique (aidez-vous de l'application Pl@ntNet), le feuillage (persistant ou caduc) et le port.</li>
  <li>Écrivez correctement les noms scientifiques (genre en majuscule, italique).</li>
  <li>Classez-les par strate et estimez leur taille adulte.</li>
</ol>"""),
  lecon("v2-l2", "Choisir une palette végétale adaptée à Tlemcen", "30 min",
    ["Relier le choix des plantes au climat méditerranéen de Tlemcen",
     "Utiliser une palette d'arbres, d'arbustes et de couvre-sols économes en eau",
     "Éviter les espèces envahissantes et très allergisantes"],
    """
<p>Tlemcen a un <b>climat méditerranéen</b> : pluies concentrées d'octobre à avril, été chaud et sec, gelées possibles en hiver (la ville est vers 800 m d'altitude). Les bonnes plantes doivent donc <b>supporter la sécheresse estivale ET le froid hivernal</b>.</p>
<h4>Principes de choix</h4>
<ul>
  <li><b>Le bon végétal au bon endroit</b> : taille adulte compatible avec l'espace disponible, exposition, sol.</li>
  <li><b>Préférer les espèces locales ou bien adaptées</b> : elles demandent moins d'eau et d'entretien et nourrissent la faune locale.</li>
  <li><b>Diversifier</b> : éviter plus de 10 % d'une même espèce dans un patrimoine arboré, pour limiter les risques de maladie ou de ravageur.</li>
  <li><b>Penser à l'eau</b> : regrouper les plantes selon leurs besoins (hydrozones).</li>
</ul>
<h4>Exemple de palette (fichier <code>palette_vegetale.csv</code> du TP)</h4>
<div class="tab-wrap"><table class="tab"><thead><tr><th>Strate</th><th>Espèce</th><th>Atouts</th></tr></thead><tbody>
<tr><td>Arbre</td><td><i>Pinus halepensis</i> (pin d'Alep)</td><td>Local, très résistant à la sécheresse ; attention à la processionnaire.</td></tr>
<tr><td>Arbre</td><td><i>Celtis australis</i> (micocoulier)</td><td>Excellent arbre d'alignement, ombre dense, rustique.</td></tr>
<tr><td>Arbre</td><td><i>Fraxinus angustifolia</i> (frêne oxyphylle)</td><td>Local, pousse vite, aime les sols frais (berges).</td></tr>
<tr><td>Arbre</td><td><i>Olea europaea</i> (olivier)</td><td>Symbole méditerranéen, très sobre en eau.</td></tr>
<tr><td>Arbre</td><td><i>Ceratonia siliqua</i> (caroubier)</td><td>Persistant, sobre ; sensible aux fortes gelées.</td></tr>
<tr><td>Arbre</td><td><i>Quercus ilex</i> (chêne vert)</td><td>Local, longévif, résiste au froid et à la sécheresse.</td></tr>
<tr><td>Arbuste</td><td><i>Pistacia lentiscus</i> (lentisque)</td><td>Local, haies libres, très sobre.</td></tr>
<tr><td>Arbuste</td><td><i>Nerium oleander</i> (laurier-rose)</td><td>Floraison estivale ; plante toxique, à éviter près des aires de jeux.</td></tr>
<tr><td>Arbuste</td><td><i>Myrtus communis</i> (myrte)</td><td>Local, parfumé, supporte la taille.</td></tr>
<tr><td>Couvre-sol</td><td><i>Rosmarinus officinalis</i> (romarin rampant)</td><td>Mellifère, sans arrosage une fois installé.</td></tr>
</tbody></table></div>
<h4>Espèces à éviter ou à surveiller</h4>
<ul>
  <li><b>Envahissantes</b> : l'ailante (<i>Ailanthus altissima</i>) drageonne partout et étouffe la végétation locale. Ne pas la planter, l'éliminer progressivement.</li>
  <li><b>Très allergisantes</b> : cyprès, platanes, bouleaux : ne pas en planter de grandes quantités près des écoles et des hôpitaux.</li>
  <li><b>Gourmandes en eau</b> : grandes pelouses de gazon fin en plein soleil, à réserver aux surfaces réellement utilisées.</li>
</ul>""",
    """<ol>
  <li>Ouvrez <code>palette_vegetale.csv</code> du TP (dans un tableur ou dans QGIS) et triez les espèces par besoin en eau.</li>
  <li>Proposez une palette pour un square de quartier de 2 000 m² : 3 arbres, 4 arbustes, 2 couvre-sols, en justifiant chaque choix.</li>
  <li>Vérifiez qu'aucune espèce ne représente plus de 10 % des arbres proposés pour l'ensemble des squares de la zone.</li>
</ol>"""),
  lecon("v2-l3", "Reconnaître les plantes sur le terrain", "20 min",
    ["Utiliser des critères d'identification simples",
     "Se servir d'une application d'identification et vérifier son résultat",
     "Constituer un petit herbier ou une fiche d'identification"],
    """
<p>Sur le terrain, on identifie une plante en observant plusieurs <b>critères</b>, du plus général au plus précis :</p>
<ol>
  <li><b>Le port et l'écorce</b> : silhouette, écorce lisse, crevassée, qui se détache en plaques (platane).</li>
  <li><b>Les feuilles</b> : simples ou composées (plusieurs folioles), alternes ou opposées sur le rameau, forme du bord (entier, denté, lobé), aiguilles (conifères) groupées par 2, 3 ou 5.</li>
  <li><b>Les fleurs et les fruits</b> : cônes (pins), gousses (caroubier, sophora), drupes (olive, micocoule), samares ailées (frêne).</li>
</ol>
<h4>Les applications d'identification</h4>
<p><b>Pl@ntNet</b> (gratuite) reconnaît une plante à partir d'une photo de feuille, de fleur ou de fruit. Elle propose plusieurs noms avec un pourcentage de confiance. <b>Vérifiez toujours</b> avec un second critère (fruit, écorce) ou un guide : les applications se trompent souvent sur les plantes ornementales et les jeunes plants.</p>
<h4>La fiche d'identification</h4>
<p>Pour chaque espèce rencontrée, préparez une fiche : nom scientifique, famille, nom commun en français et en arabe, photo du port, de la feuille, de l'écorce et du fruit, taille adulte, usages en espaces verts. Rassemblées, ces fiches forment un <b>herbier numérique</b> très utile pour les inventaires.</p>
<div class="astuce"><b>Astuce terrain :</b> photographiez toujours une feuille posée sur votre carnet avec une règle : la taille réelle aide beaucoup à l'identification.</div>""",
    """<ol>
  <li>Sortie de 30 minutes dans l'établissement ou un jardin proche : identifiez 8 espèces avec Pl@ntNet.</li>
  <li>Pour chacune, vérifiez le résultat avec un second critère (fruit, écorce, disposition des feuilles).</li>
  <li>Réalisez 3 fiches d'identification complètes et partagez-les avec la classe.</li>
</ol>"""),
  ],
  quiz=[
    q("Comment écrit-on correctement le nom scientifique du pin d'Alep ?", ["<i>Pinus halepensis</i>", "<i>pinus Halepensis</i>", "PINUS HALEPENSIS", "<i>Pinus Halepensis</i>"], 0, "Genre avec majuscule, espèce en minuscule, le tout en italique."),
    q("Un arbre qui garde ses feuilles en hiver a un feuillage…", ["caduc", "persistant", "composé", "colonnaire"], 1, "Persistant : il garde ses feuilles toute l'année."),
    q("Pourquoi éviter plus de 10 % d'une même espèce dans un patrimoine arboré ?", ["Pour réduire le risque qu'une maladie ou un ravageur détruise une grande partie des arbres", "Parce que la loi l'interdit", "Pour simplifier l'arrosage", "Parce que les pépinières n'en ont pas assez"], 0, "La diversité limite les pertes en cas d'attaque d'un ravageur spécifique."),
    q("Quelle espèce est envahissante et ne doit pas être plantée ?", ["<i>Quercus ilex</i>", "<i>Celtis australis</i>", "<i>Ailanthus altissima</i>", "<i>Myrtus communis</i>"], 2, "L'ailante drageonne et étouffe la végétation locale."),
    q("Le frêne produit comme fruit…", ["des cônes", "des samares ailées", "des gousses", "des drupes"], 1, "Les fruits du frêne sont des samares munies d'une aile."),
  ])

N3 = dict(id="v3", numero=3, titre="Inventaire et diagnostic du patrimoine arboré", echelle="1:100",
  resume="Organiser un inventaire, mesurer les arbres (circonférence, hauteur, couronne) et évaluer leur état sanitaire et leur risque.",
  lecons=[
  lecon("v3-l1", "Organiser un inventaire des arbres", "25 min",
    ["Comprendre à quoi sert un inventaire du patrimoine arboré",
     "Remplir une fiche arbre complète",
     "Préparer le relevé GPS et la codification"],
    """
<p>L'<b>inventaire du patrimoine arboré</b> est la liste localisée de tous les arbres gérés par une commune, avec leurs caractéristiques. C'est l'outil de base pour planifier l'entretien, estimer les budgets, suivre l'évolution du patrimoine et justifier les décisions (abattage, replantation).</p>
<h4>La fiche arbre</h4>
<div class="tab-wrap"><table class="tab"><thead><tr><th>Champ</th><th>Exemple</th><th>Remarque</th></tr></thead><tbody>
<tr><td>Identifiant</td><td>ARB-0042</td><td>Unique, jamais réutilisé</td></tr>
<tr><td>Espèce</td><td><i>Celtis australis</i></td><td>Nom scientifique + nom commun</td></tr>
<tr><td>Coordonnées</td><td>X = 653 812 ; Y = 3 860 455</td><td>UTM 30N (EPSG 32630), GPS ou carte</td></tr>
<tr><td>Circonférence à 1,30 m</td><td>142 cm</td><td>Mètre ruban</td></tr>
<tr><td>Hauteur</td><td>11 m</td><td>Clinomètre ou dendromètre</td></tr>
<tr><td>Diamètre de couronne</td><td>8 m</td><td>Moyenne de deux mesures perpendiculaires</td></tr>
<tr><td>Stade</td><td>Adulte</td><td>Jeune, adulte, mature, sénescent</td></tr>
<tr><td>État sanitaire</td><td>Moyen</td><td>Bon, moyen, mauvais, mort</td></tr>
<tr><td>Défauts</td><td>Branche morte</td><td>Liste codée (leçon 3)</td></tr>
<tr><td>Action proposée</td><td>Taille de sécurité</td><td>Avec un délai</td></tr>
</tbody></table></div>
<h4>Préparer la campagne</h4>
<ul>
  <li><b>Découper</b> la ville en secteurs (quartiers, rues) et attribuer un code par secteur.</li>
  <li><b>Codifier</b> à l'avance les valeurs (listes de choix) pour éviter les fautes de frappe : « Moyen », « moyen », « MOY » doivent devenir une seule valeur.</li>
  <li><b>Outils</b> : fiche papier ou formulaire numérique (QField, ODK Collect, KoboToolbox), GPS ou smartphone, mètre ruban, clinomètre, appareil photo.</li>
  <li><b>Photographier</b> chaque arbre et nommer la photo avec son identifiant.</li>
</ul>
<div class="astuce"><b>Bon réflexe :</b> testez la fiche sur 10 arbres avant de lancer la campagne. On découvre toujours un champ manquant ou une liste de choix incomplète.</div>""",
    """<ol>
  <li>Ouvrez <code>inventaire_arbres.csv</code> du TP dans un tableur. Repérez les champs et comparez-les avec la fiche de la leçon.</li>
  <li>Combien d'arbres compte l'inventaire ? Combien d'espèces différentes ? Quelle est l'espèce la plus fréquente, et dépasse-t-elle 10 % ?</li>
  <li>Inventoriez 10 arbres de votre établissement avec la fiche <code>fiche_inventaire_arbre.csv</code> (modèle vide du TP).</li>
</ol>"""),
  lecon("v3-l2", "Mesurer un arbre : circonférence, hauteur, couronne", "30 min",
    ["Mesurer la circonférence à 1,30 m et en déduire le diamètre",
     "Calculer la hauteur d'un arbre avec un angle et une distance",
     "Estimer la surface de couronne"],
    """
<h4>Circonférence et diamètre</h4>
<p>On mesure la <b>circonférence</b> (C) du tronc au mètre ruban à <b>1,30 m</b> du sol (hauteur de poitrine), côté amont si le terrain est en pente. Le diamètre se calcule par :</p>
<p class="formule">D = C ÷ π &nbsp;&nbsp; (exemple : 142 cm ÷ 3,1416 ≈ 45 cm)</p>
<p>La <b>surface terrière</b> (section du tronc) vaut g = π × D² ÷ 4. Pour D = 0,45 m : g ≈ 0,16 m².</p>
<h4>Hauteur avec un clinomètre</h4>
<p>Placez-vous à une distance <b>d</b> connue du tronc (par exemple 15 m, mesurée au ruban), visez la cime et lisez l'angle <b>α</b>. Alors :</p>
<p class="formule">h = d × tan(α) + hauteur des yeux</p>
<p>Exemple : d = 15 m, α = 32°, yeux à 1,60 m : h = 15 × 0,625 + 1,60 ≈ <b>11 m</b>. Un smartphone avec une application de clinomètre suffit pour un TP.</p>
<h4>Méthode du bâton (sans instrument)</h4>
<p>Tenez un bâton verticalement à bout de bras, de même longueur que la distance œil-main. Reculez jusqu'à ce que le bas et le haut du bâton coïncident avec le pied et la cime de l'arbre : votre distance au tronc est à peu près égale à la hauteur de l'arbre.</p>
<h4>Couronne</h4>
<p>Mesurez le diamètre de la couronne au sol dans deux directions perpendiculaires (nord-sud et est-ouest) et faites la moyenne. Surface de couronne ≈ π × (diamètre moyen ÷ 2)². Pour 8 m : ≈ 50 m² d'ombre au sol.</p>
<div class="astuce"><b>Calcul dans QGIS :</b> une fois l'inventaire importé, la calculatrice de champs donne le diamètre avec l'expression <code>"circonference_cm" / pi()</code>.</div>""",
    """<ol>
  <li>Mesurez 3 arbres : circonférence à 1,30 m, hauteur (clinomètre et méthode du bâton), diamètre de couronne.</li>
  <li>Calculez pour chacun le diamètre, la surface terrière et la surface de couronne.</li>
  <li>Comparez les deux méthodes de mesure de la hauteur : quel écart trouvez-vous ?</li>
  <li>Dans le tableur, ajoutez au fichier <code>inventaire_arbres.csv</code> une colonne <code>diametre_cm</code> calculée.</li>
</ol>"""),
  lecon("v3-l3", "Diagnostic sanitaire et évaluation du risque", "30 min",
    ["Reconnaître les principaux défauts d'un arbre",
     "Appliquer la logique de l'évaluation visuelle (VTA)",
     "Classer un arbre et proposer une action avec un délai"],
    """
<p>Un arbre en mauvaise santé peut perdre une branche ou tomber. En ville, la <b>sécurité des usagers</b> est la priorité. Le diagnostic se fait d'abord à l'œil, selon la méthode d'<b>évaluation visuelle de l'arbre</b> (VTA, <i>Visual Tree Assessment</i>), puis, si besoin, avec des instruments (résistographe, tomographe) par un spécialiste.</p>
<h4>Ce qu'on observe, du pied à la cime</h4>
<ul>
  <li><b>Collet et racines</b> : champignons au pied, racines coupées par des travaux, sol soulevé (signe de basculement).</li>
  <li><b>Tronc</b> : cavités, fissures, écorce décollée, écoulements, blessures de choc (voitures, débroussailleuses), inclinaison récente.</li>
  <li><b>Charpentières</b> : fourches en V avec écorce incluse (point de rupture fréquent), chicots de mauvaise taille.</li>
  <li><b>Houppier</b> : branches mortes, feuillage clairsemé ou jauni, attaques de ravageurs.</li>
</ul>
<h4>Classer et décider</h4>
<div class="tab-wrap"><table class="tab"><thead><tr><th>État</th><th>Signes</th><th>Action type</th></tr></thead><tbody>
<tr><td>Bon</td><td>Pas de défaut notable</td><td>Surveillance normale (tous les 3 à 5 ans)</td></tr>
<tr><td>Moyen</td><td>Défauts limités : bois mort, petite blessure</td><td>Taille d'entretien, nouvelle visite dans 1 à 2 ans</td></tr>
<tr><td>Mauvais</td><td>Défaut grave : grande cavité, fissure, champignon au pied</td><td>Expertise approfondie, mise en sécurité rapide</td></tr>
<tr><td>Mort / dangereux</td><td>Arbre mort ou rupture imminente</td><td>Périmètre de sécurité, abattage urgent, replantation</td></tr>
</tbody></table></div>
<p>Le <b>risque</b> dépend aussi de la <b>cible</b> : un arbre fragile au-dessus d'une aire de jeux est bien plus prioritaire que le même arbre au milieu d'un boisement peu fréquenté.</p>
<div class="astuce"><b>Règle d'or :</b> on n'abat jamais un arbre sans diagnostic écrit et photographié. Et chaque arbre abattu doit être remplacé (si possible par deux).</div>""",
    """<ol>
  <li>Dans <code>inventaire_arbres.csv</code>, filtrez les arbres dont l'état est « Mauvais » ou « Mort ». Combien y en a-t-il ? Dans quels espaces ?</li>
  <li>Croisez avec le champ <code>cible</code> (fréquentation) : établissez une liste des 5 arbres les plus prioritaires.</li>
  <li>Pour chacun, proposez une action et un délai (immédiat, 3 mois, 1 an).</li>
</ol>"""),
  ],
  quiz=[
    q("À quelle hauteur mesure-t-on la circonférence d'un arbre ?", ["Au ras du sol", "À 1,30 m", "À 2 m", "Sous la première branche"], 1, "La mesure standard se fait à 1,30 m, hauteur de poitrine."),
    q("Un tronc mesure 157 cm de circonférence. Son diamètre est d'environ…", ["25 cm", "50 cm", "78 cm", "157 cm"], 1, "157 ÷ 3,14 ≈ 50 cm."),
    q("Distance 20 m, angle 30° (tan = 0,577), yeux à 1,5 m. Hauteur de l'arbre ?", ["≈ 10 m", "≈ 13 m", "≈ 20 m", "≈ 31,5 m"], 1, "20 × 0,577 + 1,5 ≈ 13 m."),
    q("Quel défaut est un point de rupture fréquent ?", ["Une fourche en V avec écorce incluse", "Des feuilles persistantes", "Une écorce lisse", "Une floraison abondante"], 0, "L'écorce incluse empêche la soudure des deux branches de la fourche."),
    q("Pourquoi un même défaut est-il plus grave au-dessus d'une aire de jeux ?", ["Parce que l'arbre y pousse moins bien", "Parce que la cible (enfants) y est très présente", "Parce que la loi interdit les arbres près des jeux", "Ce n'est pas plus grave"], 1, "Le risque combine la probabilité de rupture et la présence de cibles."),
  ])

N4 = dict(id="v4", numero=4, titre="Concevoir et aménager un espace vert", echelle="1:500",
  resume="Analyser un site, établir un programme, composer un plan de masse et choisir des équipements accessibles et sûrs.",
  lecons=[
  lecon("v4-l1", "Analyser le site et établir le programme", "25 min",
    ["Réaliser l'analyse d'un site avant de dessiner",
     "Identifier les usagers et leurs besoins",
     "Rédiger un programme d'aménagement"],
    """
<p>Un bon projet commence <b>sur le terrain</b>, pas sur la feuille. L'analyse du site recense tout ce qui va contraindre ou enrichir le projet.</p>
<h4>Grille d'analyse du site</h4>
<ul>
  <li><b>Situation</b> : quartier, accès, voies, arrêts de bus, écoles et équipements voisins.</li>
  <li><b>Topographie</b> : pentes, points hauts et bas (où va l'eau de pluie ?).</li>
  <li><b>Climat local</b> : ensoleillement (où est l'ombre à 15 h en juillet ?), vents dominants, zones gelées en hiver.</li>
  <li><b>Sol</b> : terre végétale, remblais, roche, compaction.</li>
  <li><b>Existant</b> : arbres à conserver, murs, réseaux (eau, électricité, gaz, assainissement) aériens et enterrés.</li>
  <li><b>Usages actuels</b> : chemins tracés par les piétons, terrains de foot improvisés, dépôts sauvages.</li>
  <li><b>Paysage</b> : vues à garder (montagne, minaret, médina), vues à masquer.</li>
</ul>
<h4>Les usagers</h4>
<p>Qui viendra ? Enfants, adolescents, familles, personnes âgées, personnes en fauteuil roulant, sportifs, travailleurs en pause. Une <b>enquête rapide</b> (questionnaire de 10 questions, observation à différentes heures) évite de construire un parc qui ne correspond à personne.</p>
<h4>Le programme</h4>
<p>Le programme est la liste écrite de ce que le projet doit contenir, avec des surfaces : par exemple « aire de jeux 2-6 ans (150 m²), aire de jeux 6-12 ans (250 m²), pelouse ouverte (800 m²), allée principale accessible, 20 bancs dont 10 à l'ombre, point d'eau, toilettes, 30 arbres d'ombrage ». Il fixe aussi le <b>budget</b> et le niveau d'entretien acceptable.</p>
<div class="astuce"><b>Astuce :</b> les chemins tracés par les piétons dans l'herbe (« lignes de désir ») montrent où il faut placer les allées.</div>""",
    """<ol>
  <li>Dans QGIS, ouvrez la couche <code>site_projet.geojson</code> (terrain fictif de 1,2 ha) avec le fond de carte OpenStreetMap.</li>
  <li>Réalisez une carte d'analyse : accès, écoles voisines, orientation, vents dominants (nord-ouest l'hiver), réseaux (couche <code>reseaux.geojson</code>).</li>
  <li>Rédigez un programme d'une page avec les surfaces de chaque élément.</li>
</ol>"""),
  lecon("v4-l2", "Composer le plan : esquisse et plan de masse", "30 min",
    ["Passer du programme à une esquisse de zonage",
     "Dessiner un plan de masse lisible à la bonne échelle",
     "Appliquer les règles d'accessibilité et de confort"],
    """
<h4>1. Le zonage (esquisse)</h4>
<p>On dessine d'abord des « bulles » : zone calme, zone de jeux, zone sportive, entrée principale, zone ombragée. On place les zones bruyantes loin des logements et les jeux d'enfants près des bancs des parents. On teste plusieurs variantes.</p>
<h4>2. Les circulations</h4>
<ul>
  <li>Une <b>allée principale</b> qui relie les entrées et suit les lignes de désir.</li>
  <li>Des <b>allées secondaires</b> vers chaque zone, une boucle de promenade si la place le permet.</li>
  <li><b>Accessibilité</b> : repères couramment admis : largeur d'au moins 1,40 m, pente de préférence inférieure ou égale à 5 %, revêtement stable, bancs avec accoudoirs tous les 50 m environ.</li>
</ul>
<h4>3. Le végétal comme structure</h4>
<p>Les arbres forment l'ossature : rangées pour guider, bosquets pour l'ombre, arbres isolés pour signaler un lieu. Placez les arbres d'ombrage au <b>sud et à l'ouest</b> des bancs et des jeux (ombre de l'après-midi). Une haie brise-vent au nord-ouest protège du vent d'hiver.</p>
<h4>4. Le plan de masse</h4>
<p>Le plan de masse représente le projet vu du dessus, à l'échelle (souvent 1:200 ou 1:500), avec : le nord, l'échelle graphique, la légende, les arbres (cercles de la taille adulte de la couronne), les allées, les équipements, les cotes principales et un cartouche (titre, auteur, date). Il peut être dessiné à la main, avec un logiciel de DAO ou dans QGIS (mise en page).</p>
<div class="astuce"><b>Vérification :</b> dessinez les couronnes à leur taille adulte. Si elles se chevauchent beaucoup ou touchent les façades, éloignez ou changez d'espèce.</div>""",
    """<ol>
  <li>À partir de votre programme (leçon 1), dessinez deux variantes de zonage du site de projet.</li>
  <li>Choisissez-en une et dessinez le plan de masse au 1:500 (papier ou QGIS) avec nord, échelle, légende et cartouche.</li>
  <li>Vérifiez la largeur et la pente des allées principales avec les courbes de niveau de <code>courbes_site.geojson</code> (champ <code>altitude</code>).</li>
</ol>"""),
  lecon("v4-l3", "Équipements, mobilier et sécurité", "20 min",
    ["Choisir le mobilier d'un espace vert",
     "Connaître les principes de sécurité des aires de jeux",
     "Penser l'éclairage, l'eau et la propreté"],
    """
<h4>Le mobilier</h4>
<ul>
  <li><b>Bancs</b> : à l'ombre, orientés vers une vue ou une activité, avec dossier ; prévoir des bancs pour les personnes âgées près des entrées.</li>
  <li><b>Corbeilles</b> : près des entrées, des bancs et des jeux ; un espace propre reste respecté.</li>
  <li><b>Points d'eau potable</b>, toilettes dans les grands parcs.</li>
  <li><b>Signalétique</b> : plan d'entrée, règlement, nom des arbres remarquables (éducation).</li>
  <li><b>Clôture et portails</b> si le parc ferme la nuit.</li>
</ul>
<h4>Les aires de jeux</h4>
<p>Les références européennes souvent utilisées sont les normes <b>EN 1176</b> (équipements de jeux) et <b>EN 1177</b> (sols amortissants). Principes clés :</p>
<ul>
  <li>Séparer les jeux des petits (2-6 ans) et des grands (6-12 ans).</li>
  <li>Sous chaque jeu, un <b>sol amortissant</b> (copeaux, sable, gazon synthétique adapté, dalles) sur une zone de sécurité autour de l'équipement.</li>
  <li>Pas de plantes toxiques ou épineuses à proximité (laurier-rose, par exemple).</li>
  <li>Ombre indispensable : les toboggans métalliques en plein soleil brûlent en été.</li>
  <li>Contrôle régulier : visuel fréquent, contrôle approfondi annuel.</li>
</ul>
<h4>Éclairage et sécurité</h4>
<p>Éclairer les allées principales sans éclairer tout le parc (la faune nocturne a besoin d'obscurité) ; garder des vues dégagées pour que les usagers se sentent en sécurité (pas de massifs denses de 1,5 m le long des allées).</p>""",
    """<ol>
  <li>Placez sur votre plan de masse le mobilier : bancs (dont la moitié à l'ombre), corbeilles, point d'eau, signalétique.</li>
  <li>Dessinez l'aire de jeux avec ses zones de sécurité et le type de sol amortissant.</li>
  <li>Faites la liste des quantités de mobilier : elle servira au devis du niveau 8.</li>
</ol>"""),
  ],
  quiz=[
    q("Que montrent les « lignes de désir » tracées dans l'herbe ?", ["Les zones à clôturer", "Les trajets réels des piétons, où placer les allées", "Les réseaux enterrés", "Les zones gelées"], 1, "Elles révèlent les trajets que les usagers prennent vraiment."),
    q("Où placer les arbres pour ombrager un banc l'après-midi ?", ["Au nord du banc", "Au sud et à l'ouest du banc", "À l'est uniquement", "Peu importe"], 1, "Le soleil de l'après-midi vient du sud-ouest."),
    q("Quelle largeur minimale retient-on couramment pour une allée accessible ?", ["0,80 m", "1,00 m", "1,40 m", "3,00 m"], 2, "1,40 m permet le passage d'un fauteuil roulant et d'un piéton."),
    q("À quoi sert la norme EN 1177 ?", ["Aux sols amortissants des aires de jeux", "À l'éclairage public", "À l'arrosage", "À la taille des arbres"], 0, "EN 1177 concerne les sols amortissants ; EN 1176 les équipements."),
    q("Comment représente-t-on un arbre sur un plan de masse ?", ["Par un point de 1 mm", "Par un cercle de la taille adulte de sa couronne", "Par son nom uniquement", "On ne le représente pas"], 1, "La taille adulte permet de vérifier les distances et l'ombre future."),
  ])

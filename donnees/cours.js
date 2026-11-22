/*
 * CONTENU PÉDAGOGIQUE : parcours Espaces verts — Espaces verts ENIV, enseignant : BOUHAFSI SIDDIQ
 * ------------------------------------------------------------------
 * Niveaux, leçons, exercices et quiz. Texte en HTML simple.
 * Dans un quiz, "bonne" est le numéro de la bonne réponse en comptant à partir de 0.
 * Pour les VIDÉOS, utilisez donnees/videos.js (ou la page Administration du site).
 * Fichier généré par generateur/gen_cours.py : modifiez de préférence les fichiers fr_*.py,
 * ou modifiez directement ce fichier si vous n'utilisez pas Python.
 */
window.COURS = {
 "cle": "ev",
 "nom": "Espaces verts",
 "court": "le TP",
 "logiciel": "Espaces verts",
 "recherche": "espaces verts",
 "titre": "Espaces verts urbains : concevoir, planter, gérer",
 "accroche": "Les espaces verts, de l'arbre au projet urbain",
 "lead": "Un parcours progressif pour comprendre, concevoir et gérer les espaces verts de la ville : typologie et services rendus, palette végétale adaptée au climat de Tlemcen, inventaire et diagnostic des arbres, conception d'un square, plantation et irrigation économe, entretien et gestion différenciée, cartographie avec QGIS, devis et plan de gestion. Chaque leçon propose un exercice pratique, des vidéos et un quiz de fin de niveau.",
 "niveaux": [
  {
   "id": "v1",
   "numero": 1,
   "titre": "Comprendre les espaces verts urbains",
   "echelle": "1:25 000",
   "resume": "Définir et classer les espaces verts, connaître leurs rôles pour la ville et ses habitants, et situer le cadre réglementaire et les acteurs en Algérie.",
   "lecons": [
    {
     "id": "v1-l1",
     "titre": "Qu'est-ce qu'un espace vert ? Définitions et typologie",
     "duree": "20 min",
     "objectifs": [
      "Définir un espace vert urbain et ses composantes",
      "Distinguer les grandes catégories d'espaces verts",
      "Reconnaître ces catégories dans une ville comme Tlemcen"
     ],
     "contenu": "\n<p>Un <b>espace vert</b> est un espace, public ou privé, en grande partie couvert de végétation (arbres, arbustes, pelouses, fleurs), aménagé ou non, situé dans la ville ou à sa périphérie. Il peut être grand (un parc, une forêt urbaine) ou très petit (une jardinière, une rangée d'arbres le long d'un boulevard).</p>\n<p>Un espace vert est toujours un <b>système vivant</b> : du sol, de l'eau, des végétaux, de la faune (oiseaux, insectes, hérissons), des équipements (allées, bancs, jeux, éclairage) et des <b>usagers</b>. Le gérer, c'est s'occuper de tout cela à la fois.</p>\n<h4>Les grandes catégories</h4>\n<p>La loi algérienne de 2007 sur les espaces verts (voir la leçon 3) distingue plusieurs catégories. Elles sont utiles pour organiser un inventaire :</p>\n<ul>\n  <li><b>Parcs urbains et périurbains</b> : grands espaces (souvent plus de quelques hectares) avec promenades, aires de jeux, plans d'eau, accueil du public.</li>\n  <li><b>Jardins publics</b> : espaces plus petits, de quartier : squares, placettes plantées, jardins de cité.</li>\n  <li><b>Jardins spécialisés</b> : jardin botanique, roseraie, jardin d'exposition, arboretum.</li>\n  <li><b>Jardins collectifs ou résidentiels</b> : espaces verts au pied des immeubles, des écoles, des hôpitaux.</li>\n  <li><b>Jardins particuliers</b> : jardins privés des maisons.</li>\n  <li><b>Forêts urbaines</b> : boisements dans ou contre la ville, ouverts à la promenade.</li>\n  <li><b>Alignements boisés</b> : arbres plantés le long des rues, boulevards et routes.</li>\n</ul>\n<p>On ajoute souvent les <b>espaces verts d'accompagnement</b> (talus, ronds-points, terre-pleins centraux) et les <b>espaces naturels</b> (berges d'oued, friches, coteaux) qui jouent aussi un grand rôle écologique.</p>\n<h4>Exemples autour de Tlemcen</h4>\n<p>Le plateau de Lalla Setti (forêt et espace de loisirs dominant la ville), les jardins publics du centre-ville, les alignements de micocouliers et de platanes des grands boulevards, les oliveraies et vergers périurbains : chaque type demande une gestion différente.</p>\n<div class=\"astuce\"><b>À retenir :</b> classer les espaces verts par catégorie est la première étape de tout diagnostic. Sans typologie, on ne peut ni compter, ni comparer, ni planifier l'entretien.</div>",
     "exercice": "<ol>\n  <li>Sur un plan de votre ville (ou sur Google Earth), repérez au moins un exemple de chaque catégorie.</li>\n  <li>Pour chaque exemple, notez : nom, catégorie, surface approximative, quartier.</li>\n  <li>Ouvrez la couche <code>espaces_verts.geojson</code> du TP dans QGIS et regardez le champ <code>categorie</code> : quelles catégories sont représentées dans la zone d'étude fictive ?</li>\n</ol>"
    },
    {
     "id": "v1-l2",
     "titre": "Les rôles des espaces verts : services écosystémiques",
     "duree": "25 min",
     "objectifs": [
      "Citer les services rendus par les espaces verts",
      "Expliquer le rôle des arbres contre les îlots de chaleur",
      "Connaître les principaux indicateurs (m² par habitant, règle 3-30-300)"
     ],
     "contenu": "\n<p>Les espaces verts ne sont pas un « décor ». Ils rendent à la ville des <b>services écosystémiques</b>, c'est-à-dire des bénéfices gratuits apportés par la nature.</p>\n<h4>Services de régulation</h4>\n<ul>\n  <li><b>Climat local</b> : l'ombre des arbres et l'évapotranspiration des feuilles rafraîchissent l'air. Sous un grand arbre, la température ressentie en été peut baisser de plusieurs degrés. Les espaces verts réduisent les <b>îlots de chaleur urbains</b> (quartiers minéraux beaucoup plus chauds que leurs alentours).</li>\n  <li><b>Eau</b> : un sol végétalisé infiltre la pluie, réduit le ruissellement et les inondations, recharge les nappes.</li>\n  <li><b>Air et bruit</b> : le feuillage retient une partie des poussières ; les haies épaisses atténuent un peu le bruit et coupent le vent.</li>\n  <li><b>Sol</b> : les racines retiennent la terre sur les talus et coteaux (lutte contre l'érosion).</li>\n</ul>\n<h4>Services de support et biodiversité</h4>\n<p>Arbres, haies et prairies offrent abri et nourriture aux oiseaux, aux insectes pollinisateurs et à la petite faune. Reliés entre eux (alignements, berges d'oued), ils forment une <b>trame verte</b> qui permet aux espèces de circuler.</p>\n<h4>Services culturels et sociaux</h4>\n<p>Détente, sport, jeux d'enfants, rencontres, santé physique et mentale, éducation à l'environnement, valeur des logements, identité et paysage de la ville.</p>\n<h4>Quelques indicateurs</h4>\n<ul>\n  <li><b>Surface d'espaces verts par habitant</b> (m²/hab) : surface totale des espaces verts publics ÷ population. Une valeur souvent citée (attribuée à l'OMS) est d'au moins <b>9 m² par habitant</b> ; beaucoup de villes visent 10 à 15 m².</li>\n  <li><b>Taux de canopée</b> : part de la surface couverte par la couronne des arbres, vue du ciel.</li>\n  <li><b>Règle 3-30-300</b> : chaque habitant devrait voir au moins <b>3 arbres</b> depuis son logement, vivre dans un quartier avec <b>30 %</b> de canopée, et habiter à moins de <b>300 m</b> d'un espace vert.</li>\n</ul>\n<div class=\"astuce\"><b>Calcul rapide :</b> un quartier de 12 000 habitants avec 7,2 ha d'espaces verts publics dispose de 72 000 ÷ 12 000 = <b>6 m²/hab</b>, en dessous du repère de 9 m²/hab.</div>",
     "exercice": "<ol>\n  <li>Choisissez un espace vert que vous connaissez et classez ses bénéfices dans les trois familles (régulation, biodiversité, social).</li>\n  <li>Avec le fichier <code>quartiers_population.csv</code> du TP, calculez la surface d'espaces verts par habitant d'un quartier dont vous connaissez la surface d'espaces verts (champ <code>surface_ev_m2</code>).</li>\n  <li>Le quartier atteint-il 9 m²/hab ? Combien de m² faudrait-il créer pour l'atteindre ?</li>\n</ol>"
    },
    {
     "id": "v1-l3",
     "titre": "Cadre réglementaire et acteurs en Algérie",
     "duree": "20 min",
     "objectifs": [
      "Connaître la loi n° 07-06 du 13 mai 2007 relative aux espaces verts",
      "Identifier les acteurs de la création et de la gestion des espaces verts",
      "Savoir où trouver les textes officiels"
     ],
     "contenu": "\n<p>En Algérie, le texte de référence est la <b>loi n° 07-06 du 13 mai 2007 relative à la gestion, à la protection et au développement des espaces verts</b>, publiée au Journal officiel (JORADP). Elle a pour objectifs principaux :</p>\n<ul>\n  <li>d'améliorer le cadre de vie urbain et de développer les espaces verts dans chaque ville ;</li>\n  <li>de <b>classer</b> les espaces verts par catégories (celles vues en leçon 1) ;</li>\n  <li>de <b>protéger</b> les espaces verts classés contre les changements d'affectation et les dégradations ;</li>\n  <li>d'imposer la prise en compte des espaces verts dans les <b>instruments d'urbanisme</b> (PDAU, POS) et dans les projets de construction.</li>\n</ul>\n<p>Des textes d'application précisent les modalités (classement, gestion, cahiers des charges). Ils évoluent : vérifiez toujours la version en vigueur sur le site du Journal officiel.</p>\n<h4>Les acteurs</h4>\n<ul>\n  <li><b>La commune (APC)</b> : gestion et entretien de la plupart des espaces verts publics, souvent par un service des espaces verts ou une entreprise communale.</li>\n  <li><b>La wilaya</b> : direction de l'environnement, direction de l'urbanisme, financement de projets.</li>\n  <li><b>La conservation des forêts</b> : forêts périurbaines et récréatives.</li>\n  <li><b>Les entreprises et bureaux d'études</b> : conception, travaux de plantation, entretien sous contrat.</li>\n  <li><b>Les associations et les habitants</b> : plantations, sensibilisation, jardins partagés, signalement des dégradations.</li>\n</ul>\n<h4>Les documents d'urbanisme</h4>\n<p>Le <b>PDAU</b> (plan directeur d'aménagement et d'urbanisme) fixe les grandes orientations à l'échelle de la commune, le <b>POS</b> (plan d'occupation des sols) précise les règles par secteur. C'est dans ces documents qu'on réserve des terrains pour les futurs parcs et qu'on fixe les surfaces de verdure exigées.</p>\n<div class=\"astuce\"><b>Bon réflexe :</b> avant tout projet, demandez le POS du secteur et repérez les espaces verts existants ou prévus. Un espace vert classé ne peut pas devenir un parking ou un terrain à bâtir.</div>",
     "exercice": "<ol>\n  <li>Cherchez la loi n° 07-06 du 13 mai 2007 sur le site du Journal officiel (joradp.dz) et relevez la liste exacte des catégories d'espaces verts.</li>\n  <li>Faites un schéma des acteurs de votre commune : qui conçoit, qui finance, qui entretient, qui contrôle ?</li>\n  <li>En une demi-page, expliquez à un élu pourquoi un espace vert classé doit être protégé.</li>\n</ol>"
    }
   ],
   "quiz": [
    {
     "question": "Selon la loi n° 07-06, une rangée d'arbres le long d'un boulevard appartient à quelle catégorie ?",
     "choix": [
      "Les jardins spécialisés",
      "Les jardins particuliers",
      "Les alignements boisés",
      "Les parcs urbains"
     ],
     "bonne": 2,
     "explication": "Les arbres d'alignement des rues et routes forment la catégorie des alignements boisés."
    },
    {
     "question": "Un quartier de 20 000 habitants a 12 ha d'espaces verts publics. Combien de m² par habitant ?",
     "choix": [
      "0,6 m²/hab",
      "16 m²/hab",
      "6 m²/hab",
      "60 m²/hab"
     ],
     "bonne": 2,
     "explication": "12 ha = 120 000 m² ; 120 000 ÷ 20 000 = 6 m²/hab."
    },
    {
     "question": "Que signifie le « 300 » de la règle 3-30-300 ?",
     "choix": [
      "300 m² de pelouse par école",
      "300 arbres par quartier",
      "300 litres d'eau par arbre",
      "300 m au plus jusqu'à un espace vert"
     ],
     "bonne": 3,
     "explication": "Chaque habitant devrait habiter à moins de 300 m d'un espace vert."
    },
    {
     "question": "Comment les arbres réduisent-ils les îlots de chaleur ?",
     "choix": [
      "En absorbant le bruit",
      "En augmentant le ruissellement",
      "En réfléchissant la lumière des lampadaires",
      "Par l'ombre et l'évapotranspiration"
     ],
     "bonne": 3,
     "explication": "L'ombre et l'eau évaporée par les feuilles rafraîchissent l'air."
    },
    {
     "question": "Quel document d'urbanisme précise les règles d'occupation des sols secteur par secteur ?",
     "choix": [
      "Le POS",
      "Le PDAU",
      "L'inventaire des arbres",
      "Le cahier des charges d'entretien"
     ],
     "bonne": 0,
     "explication": "Le POS précise, à l'échelle du secteur, ce que fixe le PDAU à l'échelle de la commune."
    }
   ]
  },
  {
   "id": "v2",
   "numero": 2,
   "titre": "Le végétal en milieu urbain",
   "echelle": "1:20",
   "resume": "Nommer et reconnaître les plantes, connaître les strates et les ports, choisir une palette végétale adaptée au climat de Tlemcen.",
   "lecons": [
    {
     "id": "v2-l1",
     "titre": "Nommer les plantes : bases de botanique appliquée",
     "duree": "20 min",
     "objectifs": [
      "Écrire correctement un nom scientifique",
      "Distinguer les strates de végétation",
      "Décrire une plante : feuillage, port, taille adulte"
     ],
     "contenu": "\n<p>Un même arbre peut avoir plusieurs noms communs selon les régions (en français, en arabe, en tamazight). Pour éviter les erreurs dans un inventaire ou une commande de pépinière, on utilise le <b>nom scientifique</b>, en latin, valable dans le monde entier.</p>\n<h4>Le nom scientifique</h4>\n<ul>\n  <li>Il comporte deux mots : le <b>genre</b> (majuscule) et l'<b>espèce</b> (minuscule), écrits en <i>italique</i> : <i>Pinus halepensis</i> (pin d'Alep), <i>Olea europaea</i> (olivier).</li>\n  <li>On peut ajouter un <b>cultivar</b> entre apostrophes : <i>Nerium oleander</i> 'Album' (laurier-rose à fleurs blanches).</li>\n  <li>La <b>famille</b> regroupe les genres apparentés : Pinaceae, Oleaceae, Fabaceae…</li>\n</ul>\n<h4>Les strates</h4>\n<ul>\n  <li><b>Arborée</b> : arbres, plus de 7 à 8 m à l'âge adulte.</li>\n  <li><b>Arbustive</b> : arbustes et arbrisseaux, de 1 à 7 m (haies, massifs).</li>\n  <li><b>Herbacée</b> : gazon, prairie, vivaces, plantes annuelles à fleurs.</li>\n  <li><b>Couvre-sols et grimpantes</b> : plantes rampantes qui couvrent le sol, plantes qui montent sur les murs et pergolas.</li>\n</ul>\n<p>Un espace vert agréable et riche en biodiversité combine plusieurs strates.</p>\n<h4>Décrire une plante</h4>\n<ul>\n  <li><b>Feuillage</b> : persistant (garde ses feuilles l'hiver) ou caduc (les perd).</li>\n  <li><b>Port</b> : forme générale : érigé, étalé, pleureur, colonnaire, en boule.</li>\n  <li><b>Taille adulte</b> : hauteur et largeur après 20 à 30 ans. C'est elle qui décide de la distance de plantation par rapport aux façades et aux réseaux.</li>\n  <li><b>Exigences</b> : soleil ou ombre, eau, type de sol, résistance au froid et au vent.</li>\n</ul>\n<div class=\"astuce\"><b>Erreur fréquente :</b> planter un arbre en fonction de sa taille à l'achat. Un pin d'Alep de 2 m en pépinière dépassera 15 m : il ne doit pas être planté à 2 m d'une façade.</div>",
     "exercice": "<ol>\n  <li>Choisissez 5 arbres de votre quartier ou de l'école. Pour chacun, relevez le nom commun, le nom scientifique (aidez-vous de l'application Pl@ntNet), le feuillage (persistant ou caduc) et le port.</li>\n  <li>Écrivez correctement les noms scientifiques (genre en majuscule, italique).</li>\n  <li>Classez-les par strate et estimez leur taille adulte.</li>\n</ol>"
    },
    {
     "id": "v2-l2",
     "titre": "Choisir une palette végétale adaptée à Tlemcen",
     "duree": "30 min",
     "objectifs": [
      "Relier le choix des plantes au climat méditerranéen de Tlemcen",
      "Utiliser une palette d'arbres, d'arbustes et de couvre-sols économes en eau",
      "Éviter les espèces envahissantes et très allergisantes"
     ],
     "contenu": "\n<p>Tlemcen a un <b>climat méditerranéen</b> : pluies concentrées d'octobre à avril, été chaud et sec, gelées possibles en hiver (la ville est vers 800 m d'altitude). Les bonnes plantes doivent donc <b>supporter la sécheresse estivale ET le froid hivernal</b>.</p>\n<h4>Principes de choix</h4>\n<ul>\n  <li><b>Le bon végétal au bon endroit</b> : taille adulte compatible avec l'espace disponible, exposition, sol.</li>\n  <li><b>Préférer les espèces locales ou bien adaptées</b> : elles demandent moins d'eau et d'entretien et nourrissent la faune locale.</li>\n  <li><b>Diversifier</b> : éviter plus de 10 % d'une même espèce dans un patrimoine arboré, pour limiter les risques de maladie ou de ravageur.</li>\n  <li><b>Penser à l'eau</b> : regrouper les plantes selon leurs besoins (hydrozones).</li>\n</ul>\n<h4>Exemple de palette (fichier <code>palette_vegetale.csv</code> du TP)</h4>\n<div class=\"tab-wrap\"><table class=\"tab\"><thead><tr><th>Strate</th><th>Espèce</th><th>Atouts</th></tr></thead><tbody>\n<tr><td>Arbre</td><td><i>Pinus halepensis</i> (pin d'Alep)</td><td>Local, très résistant à la sécheresse ; attention à la processionnaire.</td></tr>\n<tr><td>Arbre</td><td><i>Celtis australis</i> (micocoulier)</td><td>Excellent arbre d'alignement, ombre dense, rustique.</td></tr>\n<tr><td>Arbre</td><td><i>Fraxinus angustifolia</i> (frêne oxyphylle)</td><td>Local, pousse vite, aime les sols frais (berges).</td></tr>\n<tr><td>Arbre</td><td><i>Olea europaea</i> (olivier)</td><td>Symbole méditerranéen, très sobre en eau.</td></tr>\n<tr><td>Arbre</td><td><i>Ceratonia siliqua</i> (caroubier)</td><td>Persistant, sobre ; sensible aux fortes gelées.</td></tr>\n<tr><td>Arbre</td><td><i>Quercus ilex</i> (chêne vert)</td><td>Local, longévif, résiste au froid et à la sécheresse.</td></tr>\n<tr><td>Arbuste</td><td><i>Pistacia lentiscus</i> (lentisque)</td><td>Local, haies libres, très sobre.</td></tr>\n<tr><td>Arbuste</td><td><i>Nerium oleander</i> (laurier-rose)</td><td>Floraison estivale ; plante toxique, à éviter près des aires de jeux.</td></tr>\n<tr><td>Arbuste</td><td><i>Myrtus communis</i> (myrte)</td><td>Local, parfumé, supporte la taille.</td></tr>\n<tr><td>Couvre-sol</td><td><i>Rosmarinus officinalis</i> (romarin rampant)</td><td>Mellifère, sans arrosage une fois installé.</td></tr>\n</tbody></table></div>\n<h4>Espèces à éviter ou à surveiller</h4>\n<ul>\n  <li><b>Envahissantes</b> : l'ailante (<i>Ailanthus altissima</i>) drageonne partout et étouffe la végétation locale. Ne pas la planter, l'éliminer progressivement.</li>\n  <li><b>Très allergisantes</b> : cyprès, platanes, bouleaux : ne pas en planter de grandes quantités près des écoles et des hôpitaux.</li>\n  <li><b>Gourmandes en eau</b> : grandes pelouses de gazon fin en plein soleil, à réserver aux surfaces réellement utilisées.</li>\n</ul>",
     "exercice": "<ol>\n  <li>Ouvrez <code>palette_vegetale.csv</code> du TP (dans un tableur ou dans QGIS) et triez les espèces par besoin en eau.</li>\n  <li>Proposez une palette pour un square de quartier de 2 000 m² : 3 arbres, 4 arbustes, 2 couvre-sols, en justifiant chaque choix.</li>\n  <li>Vérifiez qu'aucune espèce ne représente plus de 10 % des arbres proposés pour l'ensemble des squares de la zone.</li>\n</ol>"
    },
    {
     "id": "v2-l3",
     "titre": "Reconnaître les plantes sur le terrain",
     "duree": "20 min",
     "objectifs": [
      "Utiliser des critères d'identification simples",
      "Se servir d'une application d'identification et vérifier son résultat",
      "Constituer un petit herbier ou une fiche d'identification"
     ],
     "contenu": "\n<p>Sur le terrain, on identifie une plante en observant plusieurs <b>critères</b>, du plus général au plus précis :</p>\n<ol>\n  <li><b>Le port et l'écorce</b> : silhouette, écorce lisse, crevassée, qui se détache en plaques (platane).</li>\n  <li><b>Les feuilles</b> : simples ou composées (plusieurs folioles), alternes ou opposées sur le rameau, forme du bord (entier, denté, lobé), aiguilles (conifères) groupées par 2, 3 ou 5.</li>\n  <li><b>Les fleurs et les fruits</b> : cônes (pins), gousses (caroubier, sophora), drupes (olive, micocoule), samares ailées (frêne).</li>\n</ol>\n<h4>Les applications d'identification</h4>\n<p><b>Pl@ntNet</b> (gratuite) reconnaît une plante à partir d'une photo de feuille, de fleur ou de fruit. Elle propose plusieurs noms avec un pourcentage de confiance. <b>Vérifiez toujours</b> avec un second critère (fruit, écorce) ou un guide : les applications se trompent souvent sur les plantes ornementales et les jeunes plants.</p>\n<h4>La fiche d'identification</h4>\n<p>Pour chaque espèce rencontrée, préparez une fiche : nom scientifique, famille, nom commun en français et en arabe, photo du port, de la feuille, de l'écorce et du fruit, taille adulte, usages en espaces verts. Rassemblées, ces fiches forment un <b>herbier numérique</b> très utile pour les inventaires.</p>\n<div class=\"astuce\"><b>Astuce terrain :</b> photographiez toujours une feuille posée sur votre carnet avec une règle : la taille réelle aide beaucoup à l'identification.</div>",
     "exercice": "<ol>\n  <li>Sortie de 30 minutes dans l'établissement ou un jardin proche : identifiez 8 espèces avec Pl@ntNet.</li>\n  <li>Pour chacune, vérifiez le résultat avec un second critère (fruit, écorce, disposition des feuilles).</li>\n  <li>Réalisez 3 fiches d'identification complètes et partagez-les avec la classe.</li>\n</ol>"
    }
   ],
   "quiz": [
    {
     "question": "Comment écrit-on correctement le nom scientifique du pin d'Alep ?",
     "choix": [
      "<i>Pinus Halepensis</i>",
      "<i>Pinus halepensis</i>",
      "<i>pinus Halepensis</i>",
      "PINUS HALEPENSIS"
     ],
     "bonne": 1,
     "explication": "Genre avec majuscule, espèce en minuscule, le tout en italique."
    },
    {
     "question": "Un arbre qui garde ses feuilles en hiver a un feuillage…",
     "choix": [
      "composé",
      "caduc",
      "colonnaire",
      "persistant"
     ],
     "bonne": 3,
     "explication": "Persistant : il garde ses feuilles toute l'année."
    },
    {
     "question": "Pourquoi éviter plus de 10 % d'une même espèce dans un patrimoine arboré ?",
     "choix": [
      "Pour simplifier l'arrosage",
      "Parce que les pépinières n'en ont pas assez",
      "Pour réduire le risque qu'une maladie ou un ravageur détruise une grande partie des arbres",
      "Parce que la loi l'interdit"
     ],
     "bonne": 2,
     "explication": "La diversité limite les pertes en cas d'attaque d'un ravageur spécifique."
    },
    {
     "question": "Quelle espèce est envahissante et ne doit pas être plantée ?",
     "choix": [
      "<i>Quercus ilex</i>",
      "<i>Celtis australis</i>",
      "<i>Myrtus communis</i>",
      "<i>Ailanthus altissima</i>"
     ],
     "bonne": 3,
     "explication": "L'ailante drageonne et étouffe la végétation locale."
    },
    {
     "question": "Le frêne produit comme fruit…",
     "choix": [
      "des gousses",
      "des drupes",
      "des samares ailées",
      "des cônes"
     ],
     "bonne": 2,
     "explication": "Les fruits du frêne sont des samares munies d'une aile."
    }
   ]
  },
  {
   "id": "v3",
   "numero": 3,
   "titre": "Inventaire et diagnostic du patrimoine arboré",
   "echelle": "1:100",
   "resume": "Organiser un inventaire, mesurer les arbres (circonférence, hauteur, couronne) et évaluer leur état sanitaire et leur risque.",
   "lecons": [
    {
     "id": "v3-l1",
     "titre": "Organiser un inventaire des arbres",
     "duree": "25 min",
     "objectifs": [
      "Comprendre à quoi sert un inventaire du patrimoine arboré",
      "Remplir une fiche arbre complète",
      "Préparer le relevé GPS et la codification"
     ],
     "contenu": "\n<p>L'<b>inventaire du patrimoine arboré</b> est la liste localisée de tous les arbres gérés par une commune, avec leurs caractéristiques. C'est l'outil de base pour planifier l'entretien, estimer les budgets, suivre l'évolution du patrimoine et justifier les décisions (abattage, replantation).</p>\n<h4>La fiche arbre</h4>\n<div class=\"tab-wrap\"><table class=\"tab\"><thead><tr><th>Champ</th><th>Exemple</th><th>Remarque</th></tr></thead><tbody>\n<tr><td>Identifiant</td><td>ARB-0042</td><td>Unique, jamais réutilisé</td></tr>\n<tr><td>Espèce</td><td><i>Celtis australis</i></td><td>Nom scientifique + nom commun</td></tr>\n<tr><td>Coordonnées</td><td>X = 653 812 ; Y = 3 860 455</td><td>UTM 30N (EPSG 32630), GPS ou carte</td></tr>\n<tr><td>Circonférence à 1,30 m</td><td>142 cm</td><td>Mètre ruban</td></tr>\n<tr><td>Hauteur</td><td>11 m</td><td>Clinomètre ou dendromètre</td></tr>\n<tr><td>Diamètre de couronne</td><td>8 m</td><td>Moyenne de deux mesures perpendiculaires</td></tr>\n<tr><td>Stade</td><td>Adulte</td><td>Jeune, adulte, mature, sénescent</td></tr>\n<tr><td>État sanitaire</td><td>Moyen</td><td>Bon, moyen, mauvais, mort</td></tr>\n<tr><td>Défauts</td><td>Branche morte</td><td>Liste codée (leçon 3)</td></tr>\n<tr><td>Action proposée</td><td>Taille de sécurité</td><td>Avec un délai</td></tr>\n</tbody></table></div>\n<h4>Préparer la campagne</h4>\n<ul>\n  <li><b>Découper</b> la ville en secteurs (quartiers, rues) et attribuer un code par secteur.</li>\n  <li><b>Codifier</b> à l'avance les valeurs (listes de choix) pour éviter les fautes de frappe : « Moyen », « moyen », « MOY » doivent devenir une seule valeur.</li>\n  <li><b>Outils</b> : fiche papier ou formulaire numérique (QField, ODK Collect, KoboToolbox), GPS ou smartphone, mètre ruban, clinomètre, appareil photo.</li>\n  <li><b>Photographier</b> chaque arbre et nommer la photo avec son identifiant.</li>\n</ul>\n<div class=\"astuce\"><b>Bon réflexe :</b> testez la fiche sur 10 arbres avant de lancer la campagne. On découvre toujours un champ manquant ou une liste de choix incomplète.</div>",
     "exercice": "<ol>\n  <li>Ouvrez <code>inventaire_arbres.csv</code> du TP dans un tableur. Repérez les champs et comparez-les avec la fiche de la leçon.</li>\n  <li>Combien d'arbres compte l'inventaire ? Combien d'espèces différentes ? Quelle est l'espèce la plus fréquente, et dépasse-t-elle 10 % ?</li>\n  <li>Inventoriez 10 arbres de votre établissement avec la fiche <code>fiche_inventaire_arbre.csv</code> (modèle vide du TP).</li>\n</ol>"
    },
    {
     "id": "v3-l2",
     "titre": "Mesurer un arbre : circonférence, hauteur, couronne",
     "duree": "30 min",
     "objectifs": [
      "Mesurer la circonférence à 1,30 m et en déduire le diamètre",
      "Calculer la hauteur d'un arbre avec un angle et une distance",
      "Estimer la surface de couronne"
     ],
     "contenu": "\n<h4>Circonférence et diamètre</h4>\n<p>On mesure la <b>circonférence</b> (C) du tronc au mètre ruban à <b>1,30 m</b> du sol (hauteur de poitrine), côté amont si le terrain est en pente. Le diamètre se calcule par :</p>\n<p class=\"formule\">D = C ÷ π &nbsp;&nbsp; (exemple : 142 cm ÷ 3,1416 ≈ 45 cm)</p>\n<p>La <b>surface terrière</b> (section du tronc) vaut g = π × D² ÷ 4. Pour D = 0,45 m : g ≈ 0,16 m².</p>\n<h4>Hauteur avec un clinomètre</h4>\n<p>Placez-vous à une distance <b>d</b> connue du tronc (par exemple 15 m, mesurée au ruban), visez la cime et lisez l'angle <b>α</b>. Alors :</p>\n<p class=\"formule\">h = d × tan(α) + hauteur des yeux</p>\n<p>Exemple : d = 15 m, α = 32°, yeux à 1,60 m : h = 15 × 0,625 + 1,60 ≈ <b>11 m</b>. Un smartphone avec une application de clinomètre suffit pour un TP.</p>\n<h4>Méthode du bâton (sans instrument)</h4>\n<p>Tenez un bâton verticalement à bout de bras, de même longueur que la distance œil-main. Reculez jusqu'à ce que le bas et le haut du bâton coïncident avec le pied et la cime de l'arbre : votre distance au tronc est à peu près égale à la hauteur de l'arbre.</p>\n<h4>Couronne</h4>\n<p>Mesurez le diamètre de la couronne au sol dans deux directions perpendiculaires (nord-sud et est-ouest) et faites la moyenne. Surface de couronne ≈ π × (diamètre moyen ÷ 2)². Pour 8 m : ≈ 50 m² d'ombre au sol.</p>\n<div class=\"astuce\"><b>Calcul dans QGIS :</b> une fois l'inventaire importé, la calculatrice de champs donne le diamètre avec l'expression <code>\"circonference_cm\" / pi()</code>.</div>",
     "exercice": "<ol>\n  <li>Mesurez 3 arbres : circonférence à 1,30 m, hauteur (clinomètre et méthode du bâton), diamètre de couronne.</li>\n  <li>Calculez pour chacun le diamètre, la surface terrière et la surface de couronne.</li>\n  <li>Comparez les deux méthodes de mesure de la hauteur : quel écart trouvez-vous ?</li>\n  <li>Dans le tableur, ajoutez au fichier <code>inventaire_arbres.csv</code> une colonne <code>diametre_cm</code> calculée.</li>\n</ol>"
    },
    {
     "id": "v3-l3",
     "titre": "Diagnostic sanitaire et évaluation du risque",
     "duree": "30 min",
     "objectifs": [
      "Reconnaître les principaux défauts d'un arbre",
      "Appliquer la logique de l'évaluation visuelle (VTA)",
      "Classer un arbre et proposer une action avec un délai"
     ],
     "contenu": "\n<p>Un arbre en mauvaise santé peut perdre une branche ou tomber. En ville, la <b>sécurité des usagers</b> est la priorité. Le diagnostic se fait d'abord à l'œil, selon la méthode d'<b>évaluation visuelle de l'arbre</b> (VTA, <i>Visual Tree Assessment</i>), puis, si besoin, avec des instruments (résistographe, tomographe) par un spécialiste.</p>\n<h4>Ce qu'on observe, du pied à la cime</h4>\n<ul>\n  <li><b>Collet et racines</b> : champignons au pied, racines coupées par des travaux, sol soulevé (signe de basculement).</li>\n  <li><b>Tronc</b> : cavités, fissures, écorce décollée, écoulements, blessures de choc (voitures, débroussailleuses), inclinaison récente.</li>\n  <li><b>Charpentières</b> : fourches en V avec écorce incluse (point de rupture fréquent), chicots de mauvaise taille.</li>\n  <li><b>Houppier</b> : branches mortes, feuillage clairsemé ou jauni, attaques de ravageurs.</li>\n</ul>\n<h4>Classer et décider</h4>\n<div class=\"tab-wrap\"><table class=\"tab\"><thead><tr><th>État</th><th>Signes</th><th>Action type</th></tr></thead><tbody>\n<tr><td>Bon</td><td>Pas de défaut notable</td><td>Surveillance normale (tous les 3 à 5 ans)</td></tr>\n<tr><td>Moyen</td><td>Défauts limités : bois mort, petite blessure</td><td>Taille d'entretien, nouvelle visite dans 1 à 2 ans</td></tr>\n<tr><td>Mauvais</td><td>Défaut grave : grande cavité, fissure, champignon au pied</td><td>Expertise approfondie, mise en sécurité rapide</td></tr>\n<tr><td>Mort / dangereux</td><td>Arbre mort ou rupture imminente</td><td>Périmètre de sécurité, abattage urgent, replantation</td></tr>\n</tbody></table></div>\n<p>Le <b>risque</b> dépend aussi de la <b>cible</b> : un arbre fragile au-dessus d'une aire de jeux est bien plus prioritaire que le même arbre au milieu d'un boisement peu fréquenté.</p>\n<div class=\"astuce\"><b>Règle d'or :</b> on n'abat jamais un arbre sans diagnostic écrit et photographié. Et chaque arbre abattu doit être remplacé (si possible par deux).</div>",
     "exercice": "<ol>\n  <li>Dans <code>inventaire_arbres.csv</code>, filtrez les arbres dont l'état est « Mauvais » ou « Mort ». Combien y en a-t-il ? Dans quels espaces ?</li>\n  <li>Croisez avec le champ <code>cible</code> (fréquentation) : établissez une liste des 5 arbres les plus prioritaires.</li>\n  <li>Pour chacun, proposez une action et un délai (immédiat, 3 mois, 1 an).</li>\n</ol>"
    }
   ],
   "quiz": [
    {
     "question": "À quelle hauteur mesure-t-on la circonférence d'un arbre ?",
     "choix": [
      "Au ras du sol",
      "Sous la première branche",
      "À 2 m",
      "À 1,30 m"
     ],
     "bonne": 3,
     "explication": "La mesure standard se fait à 1,30 m, hauteur de poitrine."
    },
    {
     "question": "Un tronc mesure 157 cm de circonférence. Son diamètre est d'environ…",
     "choix": [
      "50 cm",
      "25 cm",
      "157 cm",
      "78 cm"
     ],
     "bonne": 0,
     "explication": "157 ÷ 3,14 ≈ 50 cm."
    },
    {
     "question": "Distance 20 m, angle 30° (tan = 0,577), yeux à 1,5 m. Hauteur de l'arbre ?",
     "choix": [
      "≈ 31,5 m",
      "≈ 20 m",
      "≈ 10 m",
      "≈ 13 m"
     ],
     "bonne": 3,
     "explication": "20 × 0,577 + 1,5 ≈ 13 m."
    },
    {
     "question": "Quel défaut est un point de rupture fréquent ?",
     "choix": [
      "Une écorce lisse",
      "Une floraison abondante",
      "Une fourche en V avec écorce incluse",
      "Des feuilles persistantes"
     ],
     "bonne": 2,
     "explication": "L'écorce incluse empêche la soudure des deux branches de la fourche."
    },
    {
     "question": "Pourquoi un même défaut est-il plus grave au-dessus d'une aire de jeux ?",
     "choix": [
      "Parce que la cible (enfants) y est très présente",
      "Parce que l'arbre y pousse moins bien",
      "Ce n'est pas plus grave",
      "Parce que la loi interdit les arbres près des jeux"
     ],
     "bonne": 0,
     "explication": "Le risque combine la probabilité de rupture et la présence de cibles."
    }
   ]
  },
  {
   "id": "v4",
   "numero": 4,
   "titre": "Concevoir et aménager un espace vert",
   "echelle": "1:500",
   "resume": "Analyser un site, établir un programme, composer un plan de masse et choisir des équipements accessibles et sûrs.",
   "lecons": [
    {
     "id": "v4-l1",
     "titre": "Analyser le site et établir le programme",
     "duree": "25 min",
     "objectifs": [
      "Réaliser l'analyse d'un site avant de dessiner",
      "Identifier les usagers et leurs besoins",
      "Rédiger un programme d'aménagement"
     ],
     "contenu": "\n<p>Un bon projet commence <b>sur le terrain</b>, pas sur la feuille. L'analyse du site recense tout ce qui va contraindre ou enrichir le projet.</p>\n<h4>Grille d'analyse du site</h4>\n<ul>\n  <li><b>Situation</b> : quartier, accès, voies, arrêts de bus, écoles et équipements voisins.</li>\n  <li><b>Topographie</b> : pentes, points hauts et bas (où va l'eau de pluie ?).</li>\n  <li><b>Climat local</b> : ensoleillement (où est l'ombre à 15 h en juillet ?), vents dominants, zones gelées en hiver.</li>\n  <li><b>Sol</b> : terre végétale, remblais, roche, compaction.</li>\n  <li><b>Existant</b> : arbres à conserver, murs, réseaux (eau, électricité, gaz, assainissement) aériens et enterrés.</li>\n  <li><b>Usages actuels</b> : chemins tracés par les piétons, terrains de foot improvisés, dépôts sauvages.</li>\n  <li><b>Paysage</b> : vues à garder (montagne, minaret, médina), vues à masquer.</li>\n</ul>\n<h4>Les usagers</h4>\n<p>Qui viendra ? Enfants, adolescents, familles, personnes âgées, personnes en fauteuil roulant, sportifs, travailleurs en pause. Une <b>enquête rapide</b> (questionnaire de 10 questions, observation à différentes heures) évite de construire un parc qui ne correspond à personne.</p>\n<h4>Le programme</h4>\n<p>Le programme est la liste écrite de ce que le projet doit contenir, avec des surfaces : par exemple « aire de jeux 2-6 ans (150 m²), aire de jeux 6-12 ans (250 m²), pelouse ouverte (800 m²), allée principale accessible, 20 bancs dont 10 à l'ombre, point d'eau, toilettes, 30 arbres d'ombrage ». Il fixe aussi le <b>budget</b> et le niveau d'entretien acceptable.</p>\n<div class=\"astuce\"><b>Astuce :</b> les chemins tracés par les piétons dans l'herbe (« lignes de désir ») montrent où il faut placer les allées.</div>",
     "exercice": "<ol>\n  <li>Dans QGIS, ouvrez la couche <code>site_projet.geojson</code> (terrain fictif de 1,2 ha) avec le fond de carte OpenStreetMap.</li>\n  <li>Réalisez une carte d'analyse : accès, écoles voisines, orientation, vents dominants (nord-ouest l'hiver), réseaux (couche <code>reseaux.geojson</code>).</li>\n  <li>Rédigez un programme d'une page avec les surfaces de chaque élément.</li>\n</ol>"
    },
    {
     "id": "v4-l2",
     "titre": "Composer le plan : esquisse et plan de masse",
     "duree": "30 min",
     "objectifs": [
      "Passer du programme à une esquisse de zonage",
      "Dessiner un plan de masse lisible à la bonne échelle",
      "Appliquer les règles d'accessibilité et de confort"
     ],
     "contenu": "\n<h4>1. Le zonage (esquisse)</h4>\n<p>On dessine d'abord des « bulles » : zone calme, zone de jeux, zone sportive, entrée principale, zone ombragée. On place les zones bruyantes loin des logements et les jeux d'enfants près des bancs des parents. On teste plusieurs variantes.</p>\n<h4>2. Les circulations</h4>\n<ul>\n  <li>Une <b>allée principale</b> qui relie les entrées et suit les lignes de désir.</li>\n  <li>Des <b>allées secondaires</b> vers chaque zone, une boucle de promenade si la place le permet.</li>\n  <li><b>Accessibilité</b> : repères couramment admis : largeur d'au moins 1,40 m, pente de préférence inférieure ou égale à 5 %, revêtement stable, bancs avec accoudoirs tous les 50 m environ.</li>\n</ul>\n<h4>3. Le végétal comme structure</h4>\n<p>Les arbres forment l'ossature : rangées pour guider, bosquets pour l'ombre, arbres isolés pour signaler un lieu. Placez les arbres d'ombrage au <b>sud et à l'ouest</b> des bancs et des jeux (ombre de l'après-midi). Une haie brise-vent au nord-ouest protège du vent d'hiver.</p>\n<h4>4. Le plan de masse</h4>\n<p>Le plan de masse représente le projet vu du dessus, à l'échelle (souvent 1:200 ou 1:500), avec : le nord, l'échelle graphique, la légende, les arbres (cercles de la taille adulte de la couronne), les allées, les équipements, les cotes principales et un cartouche (titre, auteur, date). Il peut être dessiné à la main, avec un logiciel de DAO ou dans QGIS (mise en page).</p>\n<div class=\"astuce\"><b>Vérification :</b> dessinez les couronnes à leur taille adulte. Si elles se chevauchent beaucoup ou touchent les façades, éloignez ou changez d'espèce.</div>",
     "exercice": "<ol>\n  <li>À partir de votre programme (leçon 1), dessinez deux variantes de zonage du site de projet.</li>\n  <li>Choisissez-en une et dessinez le plan de masse au 1:500 (papier ou QGIS) avec nord, échelle, légende et cartouche.</li>\n  <li>Vérifiez la largeur et la pente des allées principales avec les courbes de niveau de <code>courbes_site.geojson</code> (champ <code>altitude</code>).</li>\n</ol>"
    },
    {
     "id": "v4-l3",
     "titre": "Équipements, mobilier et sécurité",
     "duree": "20 min",
     "objectifs": [
      "Choisir le mobilier d'un espace vert",
      "Connaître les principes de sécurité des aires de jeux",
      "Penser l'éclairage, l'eau et la propreté"
     ],
     "contenu": "\n<h4>Le mobilier</h4>\n<ul>\n  <li><b>Bancs</b> : à l'ombre, orientés vers une vue ou une activité, avec dossier ; prévoir des bancs pour les personnes âgées près des entrées.</li>\n  <li><b>Corbeilles</b> : près des entrées, des bancs et des jeux ; un espace propre reste respecté.</li>\n  <li><b>Points d'eau potable</b>, toilettes dans les grands parcs.</li>\n  <li><b>Signalétique</b> : plan d'entrée, règlement, nom des arbres remarquables (éducation).</li>\n  <li><b>Clôture et portails</b> si le parc ferme la nuit.</li>\n</ul>\n<h4>Les aires de jeux</h4>\n<p>Les références européennes souvent utilisées sont les normes <b>EN 1176</b> (équipements de jeux) et <b>EN 1177</b> (sols amortissants). Principes clés :</p>\n<ul>\n  <li>Séparer les jeux des petits (2-6 ans) et des grands (6-12 ans).</li>\n  <li>Sous chaque jeu, un <b>sol amortissant</b> (copeaux, sable, gazon synthétique adapté, dalles) sur une zone de sécurité autour de l'équipement.</li>\n  <li>Pas de plantes toxiques ou épineuses à proximité (laurier-rose, par exemple).</li>\n  <li>Ombre indispensable : les toboggans métalliques en plein soleil brûlent en été.</li>\n  <li>Contrôle régulier : visuel fréquent, contrôle approfondi annuel.</li>\n</ul>\n<h4>Éclairage et sécurité</h4>\n<p>Éclairer les allées principales sans éclairer tout le parc (la faune nocturne a besoin d'obscurité) ; garder des vues dégagées pour que les usagers se sentent en sécurité (pas de massifs denses de 1,5 m le long des allées).</p>",
     "exercice": "<ol>\n  <li>Placez sur votre plan de masse le mobilier : bancs (dont la moitié à l'ombre), corbeilles, point d'eau, signalétique.</li>\n  <li>Dessinez l'aire de jeux avec ses zones de sécurité et le type de sol amortissant.</li>\n  <li>Faites la liste des quantités de mobilier : elle servira au devis du niveau 8.</li>\n</ol>"
    }
   ],
   "quiz": [
    {
     "question": "Que montrent les « lignes de désir » tracées dans l'herbe ?",
     "choix": [
      "Les zones à clôturer",
      "Les trajets réels des piétons, où placer les allées",
      "Les réseaux enterrés",
      "Les zones gelées"
     ],
     "bonne": 1,
     "explication": "Elles révèlent les trajets que les usagers prennent vraiment."
    },
    {
     "question": "Où placer les arbres pour ombrager un banc l'après-midi ?",
     "choix": [
      "Au sud et à l'ouest du banc",
      "Peu importe",
      "Au nord du banc",
      "À l'est uniquement"
     ],
     "bonne": 0,
     "explication": "Le soleil de l'après-midi vient du sud-ouest."
    },
    {
     "question": "Quelle largeur minimale retient-on couramment pour une allée accessible ?",
     "choix": [
      "1,40 m",
      "3,00 m",
      "1,00 m",
      "0,80 m"
     ],
     "bonne": 0,
     "explication": "1,40 m permet le passage d'un fauteuil roulant et d'un piéton."
    },
    {
     "question": "À quoi sert la norme EN 1177 ?",
     "choix": [
      "À la taille des arbres",
      "À l'éclairage public",
      "À l'arrosage",
      "Aux sols amortissants des aires de jeux"
     ],
     "bonne": 3,
     "explication": "EN 1177 concerne les sols amortissants ; EN 1176 les équipements."
    },
    {
     "question": "Comment représente-t-on un arbre sur un plan de masse ?",
     "choix": [
      "Par son nom uniquement",
      "On ne le représente pas",
      "Par un point de 1 mm",
      "Par un cercle de la taille adulte de sa couronne"
     ],
     "bonne": 3,
     "explication": "La taille adulte permet de vérifier les distances et l'ombre future."
    }
   ]
  },
  {
   "id": "v5",
   "numero": 5,
   "titre": "Sol, plantation et irrigation",
   "echelle": "1:20",
   "resume": "Préparer le sol, planter un arbre dans les règles, calculer les besoins en eau et concevoir un arrosage économe.",
   "lecons": [
    {
     "id": "v5-l1",
     "titre": "Le sol et la fosse de plantation",
     "duree": "25 min",
     "objectifs": [
      "Décrire les qualités d'une bonne terre végétale",
      "Dimensionner une fosse de plantation en ville",
      "Prévenir le tassement du sol"
     ],
     "contenu": "\n<p>Les racines vivent dans le sol : un arbre dans un mauvais sol restera chétif toute sa vie, quels que soient les soins. En ville, le sol est souvent fait de <b>remblais</b>, de gravats, compacté par les engins et les voitures.</p>\n<h4>Une bonne terre végétale</h4>\n<ul>\n  <li><b>Texture</b> équilibrée (sable, limon, argile) : ni trop collante, ni trop filtrante. Test simple : une poignée de terre humide forme une boule qui se casse sous une légère pression.</li>\n  <li><b>Matière organique</b> : 2 à 5 % ; on améliore avec du compost mûr.</li>\n  <li><b>Structure</b> aérée : l'air et l'eau doivent circuler. Un sol tassé asphyxie les racines.</li>\n  <li><b>pH</b> : les sols de la région de Tlemcen sont souvent calcaires (pH 7,5 à 8,5) ; choisir des espèces qui le tolèrent.</li>\n</ul>\n<h4>La fosse de plantation</h4>\n<ul>\n  <li>Volume : <b>le plus grand possible</b>. Pour un grand arbre d'alignement, on vise souvent 10 m³ de terre ou plus ; une petite fosse de 1 m³ condamne l'arbre à rester petit et à mourir jeune.</li>\n  <li>Quand le trottoir est étroit, on relie les fosses entre elles (<b>tranchée continue</b>) ou on utilise des <b>mélanges terre-pierre</b> porteurs qui laissent passer les racines sous les trottoirs.</li>\n  <li>Décompacter le fond et les parois, ne pas mettre de couche de gravier au fond.</li>\n</ul>\n<h4>Protéger le sol</h4>\n<p>Pendant les chantiers, on clôture la zone sous la couronne des arbres existants (aucun engin, aucun stockage). Dans les espaces verts, on évite que les voitures se garent sur les pelouses et au pied des arbres. Le <b>paillage</b> (copeaux de bois, broyat) protège le sol du soleil, garde l'humidité et nourrit la vie du sol.</p>",
     "exercice": "<ol>\n  <li>Prélevez un peu de terre dans deux endroits (pelouse, pied d'arbre de rue) : faites le test de la boule et observez la couleur, les cailloux, les racines.</li>\n  <li>Une rue fictive de 300 m doit recevoir des micocouliers tous les 8 m d'un seul côté. Combien d'arbres ? Quel volume total de terre pour 10 m³ par arbre ?</li>\n  <li>Proposez une solution si le trottoir ne fait que 2 m de large.</li>\n</ol>"
    },
    {
     "id": "v5-l2",
     "titre": "Planter un arbre dans les règles",
     "duree": "25 min",
     "objectifs": [
      "Choisir la période et le plant",
      "Réaliser une plantation étape par étape",
      "Assurer l'arrosage et le suivi des premières années"
     ],
     "contenu": "\n<h4>La période</h4>\n<p>On plante pendant le <b>repos végétatif</b>, de novembre à mars, hors périodes de gel ou de sol détrempé. Les plants en <b>racines nues</b> doivent absolument être plantés à cette période ; les plants en <b>conteneur</b> ou en <b>motte</b> tolèrent une période un peu plus longue, mais jamais en plein été à Tlemcen.</p>\n<h4>Choisir le plant</h4>\n<p>Tronc droit, flèche (pousse terminale) intacte, racines non enroulées en spirale dans le pot, pas de blessure. Un jeune plant (circonférence 10-14 cm) reprend souvent mieux qu'un gros sujet.</p>\n<h4>Étapes</h4>\n<ol>\n  <li>Ouvrir la fosse et ameublir le fond.</li>\n  <li>Placer le ou les <b>tuteurs</b> avant l'arbre (côté vent dominant), sans blesser les racines.</li>\n  <li>Démêler les racines qui tournent, couper les racines abîmées.</li>\n  <li>Placer l'arbre : le <b>collet</b> (jonction tronc-racines) au niveau du sol fini, jamais enterré.</li>\n  <li>Reboucher avec la terre végétale (amendée de compost), tasser légèrement au pied.</li>\n  <li>Former une <b>cuvette d'arrosage</b> et arroser abondamment (au moins 50 litres) même s'il pleut.</li>\n  <li>Attacher l'arbre au tuteur avec un lien souple qui ne blesse pas l'écorce ; pailler la cuvette.</li>\n</ol>\n<h4>Le suivi</h4>\n<p>Pendant les <b>2 à 3 premiers étés</b>, arroser régulièrement (par exemple 50 litres une fois par semaine, à adapter à la météo et au sol). Desserrer les liens chaque année, retirer les tuteurs après 2 à 3 ans. Remplacer les sujets morts dès l'hiver suivant.</p>\n<div class=\"astuce\"><b>Erreur fréquente :</b> enterrer le collet. L'écorce du tronc pourrit, l'arbre dépérit lentement. Le collet doit rester visible.</div>",
     "exercice": "<ol>\n  <li>Rédigez une fiche de chantier illustrée (schéma de la fosse, tuteur, cuvette) pour la plantation d'un frêne.</li>\n  <li>Si possible, participez à la plantation d'un arbre dans l'établissement et photographiez chaque étape.</li>\n  <li>Prévoyez le calendrier d'arrosage des 3 premiers étés et la quantité d'eau totale.</li>\n</ol>"
    },
    {
     "id": "v5-l3",
     "titre": "Calculer les besoins en eau et concevoir l'arrosage",
     "duree": "35 min",
     "objectifs": [
      "Comprendre l'évapotranspiration de référence (ET0)",
      "Calculer le besoin en eau d'une surface plantée",
      "Choisir un système d'arrosage économe"
     ],
     "contenu": "\n<p>L'eau est rare à Tlemcen en été : un espace vert doit être conçu pour <b>consommer peu</b>. On calcule ses besoins à partir de l'<b>évapotranspiration de référence</b> (ET0) : la quantité d'eau, en mm par jour, perdue par une pelouse de référence bien arrosée. 1 mm sur 1 m² = 1 litre.</p>\n<h4>Le calcul</h4>\n<p class=\"formule\">Besoin (L/jour) = ET0 (mm/j) × KL × Surface (m²) ÷ Efficience</p>\n<ul>\n  <li><b>KL</b>, coefficient de plantation : environ 0,2 à 0,3 pour des plantes sobres (olivier, romarin, lentisque) ; 0,4 à 0,6 pour des massifs moyens ; 0,7 à 0,8 pour un gazon.</li>\n  <li><b>Efficience</b> du système : goutte-à-goutte ≈ 0,9 ; aspersion ≈ 0,7 (une partie s'évapore ou part avec le vent).</li>\n  <li>On retire la pluie utile quand il pleut (rarement en été).</li>\n</ul>\n<h4>Exemple (juillet, ET0 = 6 mm/j, valeurs du fichier <code>et0_tlemcen.csv</code> du TP)</h4>\n<div class=\"tab-wrap\"><table class=\"tab\"><thead><tr><th>Zone</th><th>Surface</th><th>KL</th><th>Système</th><th>Besoin</th></tr></thead><tbody>\n<tr><td>Gazon</td><td>800 m²</td><td>0,8</td><td>Aspersion (0,7)</td><td>6 × 0,8 × 800 ÷ 0,7 ≈ 5 490 L/j</td></tr>\n<tr><td>Massifs méditerranéens</td><td>800 m²</td><td>0,3</td><td>Goutte-à-goutte (0,9)</td><td>6 × 0,3 × 800 ÷ 0,9 = 1 600 L/j</td></tr>\n</tbody></table></div>\n<p>À surface égale, les massifs sobres au goutte-à-goutte consomment <b>3,4 fois moins</b> que le gazon arrosé par aspersion.</p>\n<h4>Bonnes pratiques</h4>\n<ul>\n  <li><b>Hydrozones</b> : regrouper les plantes selon leurs besoins et les arroser par secteurs séparés.</li>\n  <li>Arroser <b>tôt le matin ou la nuit</b>, moins souvent mais plus longtemps (racines profondes).</li>\n  <li><b>Pailler</b> : réduit fortement l'évaporation.</li>\n  <li>Utiliser des <b>eaux non conventionnelles</b> quand c'est autorisé : eaux de pluie stockées, eaux usées épurées selon la réglementation.</li>\n  <li>Le <b>xéropaysagisme</b> (jardin sec) : plantes adaptées, peu de gazon, paillage minéral ou végétal.</li>\n</ul>",
     "exercice": "<ol>\n  <li>Ouvrez <code>et0_tlemcen.csv</code> et calculez le besoin mensuel en eau (m³) du square de 2 000 m² de votre palette (niveau 2) : précisez les surfaces de chaque zone.</li>\n  <li>Comparez deux variantes : 50 % de gazon ou 10 % de gazon. Quelle économie d'eau sur l'année ?</li>\n  <li>Le classeur <code>calcul_irrigation.xlsx</code> du TP contient le modèle de calcul : vérifiez vos résultats.</li>\n</ol>"
    }
   ],
   "quiz": [
    {
     "question": "À quelle période plante-t-on les arbres en racines nues ?",
     "choix": [
      "Uniquement en avril",
      "Pendant le repos végétatif, de novembre à mars hors gel",
      "En plein été",
      "N'importe quand"
     ],
     "bonne": 1,
     "explication": "Les racines nues ne supportent la plantation que pendant le repos végétatif."
    },
    {
     "question": "Où doit se trouver le collet après la plantation ?",
     "choix": [
      "Enterré de 20 cm",
      "50 cm au-dessus du sol",
      "Dans la couche de gravier",
      "Au niveau du sol fini"
     ],
     "bonne": 3,
     "explication": "Un collet enterré entraîne la pourriture de l'écorce."
    },
    {
     "question": "ET0 = 5 mm/j, KL = 0,3, surface 100 m², goutte-à-goutte (0,9). Besoin journalier ?",
     "choix": [
      "≈ 1 500 L",
      "≈ 150 L",
      "≈ 167 L",
      "≈ 15 L"
     ],
     "bonne": 2,
     "explication": "5 × 0,3 × 100 ÷ 0,9 ≈ 167 litres par jour."
    },
    {
     "question": "Pourquoi regroupe-t-on les plantes en hydrozones ?",
     "choix": [
      "Pour arroser chaque groupe selon ses besoins réels",
      "Pour faire de jolies couleurs",
      "Pour éviter la taille",
      "Pour réduire le nombre d'arbres"
     ],
     "bonne": 0,
     "explication": "Chaque secteur d'arrosage reçoit la dose adaptée à ses plantes."
    },
    {
     "question": "Quel volume de terre vise-t-on souvent pour un grand arbre d'alignement ?",
     "choix": [
      "10 m³ ou plus",
      "1 m³",
      "Aucune terre, du gravier suffit",
      "0,5 m³"
     ],
     "bonne": 0,
     "explication": "Un grand volume de terre permet à l'arbre de développer ses racines et de vivre longtemps."
    }
   ]
  },
  {
   "id": "v6",
   "numero": 6,
   "titre": "Entretien et gestion durable",
   "echelle": "1:200",
   "resume": "Planifier l'entretien sur l'année, appliquer la gestion différenciée, tailler correctement et protéger les végétaux sans pesticides.",
   "lecons": [
    {
     "id": "v6-l1",
     "titre": "Calendrier d'entretien et gestion différenciée",
     "duree": "25 min",
     "objectifs": [
      "Établir le calendrier annuel des travaux d'entretien",
      "Appliquer la gestion différenciée par classes d'entretien",
      "Valoriser les déchets verts"
     ],
     "contenu": "\n<h4>Le calendrier annuel (climat de Tlemcen)</h4>\n<div class=\"tab-wrap\"><table class=\"tab\"><thead><tr><th>Période</th><th>Travaux principaux</th></tr></thead><tbody>\n<tr><td>Novembre à mars</td><td>Plantations, taille des arbres caducs, échenillage des nids de processionnaire, entretien du mobilier, paillage.</td></tr>\n<tr><td>Mars à mai</td><td>Tontes, désherbage manuel, mise en route et contrôle de l'arrosage, fleurissement de printemps. Pas de taille lourde pendant la nidification des oiseaux.</td></tr>\n<tr><td>Juin à septembre</td><td>Arrosage (le poste principal), surveillance des jeunes arbres, ramassage des déchets, prévention des incendies (débroussaillement des zones boisées).</td></tr>\n<tr><td>Octobre</td><td>Bilan de l'été, préparation des plantations, semis de prairies, récolte des feuilles pour le compost.</td></tr>\n</tbody></table></div>\n<h4>La gestion différenciée</h4>\n<p>Tous les espaces n'ont pas besoin du même entretien. La <b>gestion différenciée</b> attribue à chaque espace une <b>classe d'entretien</b> :</p>\n<ul>\n  <li><b>Classe 1, horticole</b> : places et entrées de prestige, massifs fleuris, gazon tondu court. Entretien intensif.</li>\n  <li><b>Classe 2, jardinée</b> : squares et jardins de quartier, entretien régulier.</li>\n  <li><b>Classe 3, rustique</b> : grandes pelouses fauchées moins souvent, arbustes en port libre.</li>\n  <li><b>Classe 4, naturelle</b> : berges, coteaux, prairies fauchées une à deux fois par an, bois morts laissés pour la faune (si sans danger).</li>\n</ul>\n<p>Avantages : moins d'eau, moins d'heures de travail, plus de biodiversité, et des moyens concentrés là où ils sont visibles et utiles. Il faut l'<b>expliquer aux habitants</b> (panneaux) : une prairie non tondue n'est pas un espace abandonné.</p>\n<h4>Les déchets verts</h4>\n<p>Tontes, feuilles et branches broyées deviennent du <b>compost</b> ou du <b>paillage</b> : on ferme le cycle et on réduit les achats d'engrais et de paillis.</p>",
     "exercice": "<ol>\n  <li>Dans QGIS, ouvrez <code>espaces_verts.geojson</code> et ajoutez un champ <code>classe_entretien</code> (1 à 4).</li>\n  <li>Attribuez une classe à chaque espace en justifiant (fréquentation, usage, intérêt écologique).</li>\n  <li>Faites une carte de la gestion différenciée avec une couleur par classe et calculez la surface de chaque classe.</li>\n</ol>"
    },
    {
     "id": "v6-l2",
     "titre": "La taille des arbres",
     "duree": "30 min",
     "objectifs": [
      "Distinguer les types de taille et leurs objectifs",
      "Réaliser une coupe correcte au ras du col de la branche",
      "Refuser l'étêtage et connaître les règles de sécurité"
     ],
     "contenu": "\n<p>Un arbre bien planté, à la bonne place, a <b>peu besoin d'être taillé</b>. La taille répond à un objectif précis ; elle n'est jamais systématique.</p>\n<h4>Les types de taille</h4>\n<ul>\n  <li><b>Taille de formation</b> (jeunes arbres) : garder une flèche unique, supprimer les fourches en V, relever progressivement les branches basses au-dessus des passages.</li>\n  <li><b>Taille d'entretien</b> : supprimer le bois mort, les branches cassées, malades ou qui se croisent.</li>\n  <li><b>Taille de sécurité</b> : supprimer une branche dangereuse au-dessus d'une allée ou d'une aire de jeux.</li>\n  <li><b>Taille architecturée</b> (rideaux, têtes de chat, palmettes) : seulement sur des arbres conduits ainsi depuis leur jeunesse, et à renouveler régulièrement.</li>\n</ul>\n<h4>La bonne coupe</h4>\n<p>On coupe juste à l'extérieur du <b>col de la branche</b> (le renflement à sa base), sans l'abîmer et sans laisser de <b>chicot</b>. Le col contient les tissus qui referment la plaie. Pour une grosse branche, on procède en trois coupes (entaille dessous, coupe dessus plus loin, puis coupe finale) pour éviter l'arrachement de l'écorce.</p>\n<h4>Ce qu'il ne faut pas faire</h4>\n<ul>\n  <li><b>L'étêtage</b> (couper toutes les grosses branches) : l'arbre réagit par des rejets fragiles, pourrit par les grosses plaies et devient dangereux. C'est une mauvaise pratique encore fréquente.</li>\n  <li>Enlever plus d'environ un quart du feuillage en une seule fois.</li>\n  <li>Utiliser des griffes (éperons) pour grimper sur un arbre qu'on ne va pas abattre.</li>\n</ul>\n<h4>Sécurité</h4>\n<p>Le travail en hauteur est réservé à du personnel formé et équipé : casque, lunettes, gants, pantalon anti-coupure pour la tronçonneuse, harnais et cordes ou nacelle. Le chantier est balisé, la circulation protégée.</p>",
     "exercice": "<ol>\n  <li>Sur des photos d'arbres de votre ville, repérez des exemples d'étêtage, de chicots et de coupes correctes.</li>\n  <li>Dessinez les trois coupes nécessaires pour retirer une grosse branche, en indiquant le col.</li>\n  <li>Dans <code>inventaire_arbres.csv</code>, listez les arbres pour lesquels une taille est proposée et précisez le type de taille.</li>\n</ol>"
    },
    {
     "id": "v6-l3",
     "titre": "Protéger les végétaux sans pesticides : la lutte intégrée",
     "duree": "25 min",
     "objectifs": [
      "Reconnaître la processionnaire du pin et ses dangers",
      "Combiner les méthodes de lutte intégrée",
      "Organiser un suivi sanitaire du patrimoine"
     ],
     "contenu": "\n<p>La <b>lutte intégrée</b> combine plusieurs méthodes et n'utilise un produit qu'en dernier recours. Dans les lieux publics, on cherche à se passer des pesticides chimiques, dangereux pour les usagers, les agents et la faune utile.</p>\n<h4>Exemple : la processionnaire du pin</h4>\n<p>La chenille de <i>Thaumetopoea pityocampa</i> vit en colonies dans des <b>nids soyeux blancs</b> au bout des branches de pins et de cèdres. Elle dévore les aiguilles et ses <b>poils urticants</b> provoquent des réactions graves chez l'homme et les animaux (yeux, peau, voies respiratoires). En fin d'hiver, les chenilles descendent en file indienne pour s'enterrer.</p>\n<ul>\n  <li><b>Hiver</b> : échenillage, c'est-à-dire couper et détruire les nids, par des agents équipés (combinaison, masque, lunettes).</li>\n  <li><b>Fin d'hiver</b> : <b>colliers pièges</b> autour des troncs qui capturent les chenilles lors de leur descente.</li>\n  <li><b>Été</b> : <b>pièges à phéromones</b> qui capturent les papillons mâles.</li>\n  <li><b>Automne</b> : traitement biologique au <i>Bacillus thuringiensis</i> sur les jeunes chenilles si l'infestation est forte.</li>\n  <li><b>Toute l'année</b> : nichoirs à mésanges, grandes consommatrices de chenilles ; diversification des essences.</li>\n</ul>\n<h4>Autres méthodes</h4>\n<ul>\n  <li><b>Prévention</b> : bonnes espèces au bon endroit, sol vivant, arrosage adapté : une plante en bonne santé résiste mieux.</li>\n  <li><b>Lutte mécanique</b> : désherbage manuel ou thermique, taille des parties atteintes.</li>\n  <li><b>Lutte biologique</b> : auxiliaires (coccinelles contre les pucerons), nichoirs, haies refuges.</li>\n</ul>\n<h4>Le suivi sanitaire</h4>\n<p>Notez chaque observation (date, lieu, arbre, ravageur, intensité) dans l'inventaire : on repère les foyers, on mesure l'efficacité des actions et on prévoit les campagnes de l'année suivante.</p>",
     "exercice": "<ol>\n  <li>Dans <code>inventaire_arbres.csv</code>, comptez les pins signalés avec des nids de processionnaire (champ <code>defaut</code> = « Nids processionnaire »).</li>\n  <li>Cartographiez-les dans QGIS : sont-ils près des écoles et des aires de jeux ?</li>\n  <li>Rédigez le plan d'action annuel de lutte intégrée pour ces arbres, mois par mois.</li>\n</ol>"
    }
   ],
   "quiz": [
    {
     "question": "Quelle classe de gestion différenciée correspond aux berges et prairies fauchées une à deux fois par an ?",
     "choix": [
      "Classe 1, horticole",
      "Classe 3, rustique",
      "Classe 4, naturelle",
      "Classe 2, jardinée"
     ],
     "bonne": 2,
     "explication": "La classe naturelle réduit les interventions au minimum."
    },
    {
     "question": "Où faut-il couper une branche ?",
     "choix": [
      "Juste à l'extérieur du col, sans chicot",
      "À 30 cm du tronc",
      "Au ras du tronc, en enlevant le col",
      "Au milieu de la branche"
     ],
     "bonne": 0,
     "explication": "Le col contient les tissus qui referment la plaie."
    },
    {
     "question": "Pourquoi l'étêtage est-il une mauvaise pratique ?",
     "choix": [
      "Il est obligatoire chaque année",
      "Il fait trop d'ombre",
      "Il coûte trop peu",
      "Il donne des rejets fragiles et de grosses plaies qui pourrissent"
     ],
     "bonne": 3,
     "explication": "L'arbre étêté devient fragile et dangereux."
    },
    {
     "question": "Quand utilise-t-on les colliers pièges contre la processionnaire ?",
     "choix": [
      "En automne",
      "En fin d'hiver, lors de la descente des chenilles",
      "En été",
      "Jamais"
     ],
     "bonne": 1,
     "explication": "Les colliers capturent les chenilles qui descendent le long du tronc."
    },
    {
     "question": "Dans la lutte intégrée, le produit de traitement est utilisé…",
     "choix": [
      "en premier, de façon préventive",
      "chaque mois",
      "uniquement sur les pelouses",
      "en dernier recours"
     ],
     "bonne": 3,
     "explication": "On combine d'abord prévention, lutte mécanique et biologique."
    }
   ]
  },
  {
   "id": "v7",
   "numero": 7,
   "titre": "Cartographier les espaces verts avec QGIS",
   "echelle": "1:10 000",
   "resume": "Numériser et mesurer les espaces verts, calculer les indicateurs par quartier, analyser l'accessibilité et exploiter l'inventaire des arbres et le NDVI.",
   "lecons": [
    {
     "id": "v7-l1",
     "titre": "Cartographier les espaces verts et calculer les surfaces",
     "duree": "30 min",
     "objectifs": [
      "Ouvrir les couches du TP dans QGIS avec le bon système de coordonnées",
      "Numériser un nouvel espace vert",
      "Calculer les surfaces et le ratio m² par habitant par quartier"
     ],
     "contenu": "\n<p>QGIS est un SIG libre et gratuit (qgis.org, version LTR conseillée). Les couches du TP sont en <b>WGS 84 / UTM zone 30N (EPSG 32630)</b> : les distances et les surfaces sont en mètres.</p>\n<h4>1. Ouvrir les données</h4>\n<ol>\n  <li><i>Projet &gt; Propriétés &gt; SCR</i> : choisir EPSG:32630.</li>\n  <li>Glisser-déposer <code>quartiers.geojson</code> et <code>espaces_verts.geojson</code> dans QGIS.</li>\n  <li>Ajouter un fond OpenStreetMap : panneau <i>Navigateur &gt; XYZ Tiles &gt; OpenStreetMap</i>.</li>\n</ol>\n<h4>2. Numériser un espace vert</h4>\n<p>Sélectionnez la couche <code>espaces_verts</code>, cliquez sur <i>Basculer en mode édition</i> (crayon), puis <i>Ajouter une entité polygone</i>. Cliquez les sommets, clic droit pour terminer, remplissez les attributs (nom, catégorie), enregistrez.</p>\n<h4>3. Calculer les surfaces</h4>\n<p>Ouvrez la <i>Calculatrice de champs</i>, créez un champ décimal <code>surface_m2</code> avec l'expression :</p>\n<pre><code>$area</code></pre>\n<h4>4. Surface d'espaces verts par quartier</h4>\n<p>Outil <i>Traitement &gt; Boîte à outils &gt; Joindre les attributs par localisation (résumé)</i> : couche cible <code>quartiers</code>, couche à joindre <code>espaces_verts</code>, prédicat « intersecte », champ <code>surface_m2</code>, résumé « somme ». (Pour être exact, découpez d'abord les espaces verts par les quartiers avec l'outil <i>Intersection</i>.) Puis, dans la nouvelle couche, calculez le ratio :</p>\n<pre><code>\"surface_m2_sum\" / \"population\"</code></pre>\n<p>Représentez ce champ en <i>Symbologie &gt; Gradué</i> : vous obtenez la carte des quartiers déficitaires (moins de 9 m²/hab).</p>",
     "exercice": "<ol>\n  <li>Réalisez les étapes de la leçon avec les données du TP.</li>\n  <li>Quels quartiers sont sous 9 m²/hab ? Quelle surface faudrait-il créer dans chacun ?</li>\n  <li>Faites une mise en page (titre, légende, échelle, nord, source « données fictives ENIV ») et exportez-la en PDF.</li>\n</ol>"
    },
    {
     "id": "v7-l2",
     "titre": "Analyser l'accessibilité des espaces verts",
     "duree": "30 min",
     "objectifs": [
      "Créer une zone tampon de 300 m autour des espaces verts",
      "Estimer la part de la population à moins de 300 m",
      "Proposer l'emplacement d'un nouvel espace vert"
     ],
     "contenu": "\n<p>Avoir assez d'espaces verts ne suffit pas : il faut qu'ils soient <b>proches</b> des habitants. Selon la règle 3-30-300 (niveau 1), chacun devrait vivre à moins de <b>300 m</b> d'un espace vert.</p>\n<h4>1. Zone tampon</h4>\n<p><i>Vecteur &gt; Outils de géotraitement &gt; Tampon</i> : couche <code>espaces_verts</code>, distance <b>300</b> mètres, cochez <i>Regrouper le résultat</i>. On peut d'abord filtrer les petits espaces (par exemple ne garder que ceux de plus de 5 000 m²) avec l'expression :</p>\n<pre><code>\"surface_m2\" &gt;= 5000</code></pre>\n<h4>2. Population desservie</h4>\n<p>La couche <code>batiments_habitat.geojson</code> du TP contient des points d'habitat avec un nombre d'habitants (champ <code>habitants</code>). Utilisez <i>Sélection par localisation</i> : sélectionner les points qui « intersectent » la zone tampon. La somme des habitants sélectionnés (panneau <i>Statistiques</i>) divisée par la population totale donne la <b>part de la population desservie</b>.</p>\n<h4>3. Zones blanches et proposition</h4>\n<p>Inversez la sélection : les points restants sont les habitants <b>non desservis</b>. Avec une <i>Carte de chaleur</i> (symbologie) sur ces points, repérez la zone où un nouvel espace vert serait le plus utile. Vérifiez ensuite qu'un terrain libre y existe (couche <code>terrains_libres.geojson</code>).</p>\n<div class=\"astuce\"><b>Pour aller plus loin :</b> la distance à vol d'oiseau surestime l'accessibilité. Avec l'outil <i>Zone de desserte</i> (analyse de réseau) et les rues d'OpenStreetMap, on calcule la vraie distance à pied.</div>",
     "exercice": "<ol>\n  <li>Calculez la part de la population à moins de 300 m d'un espace vert de plus de 5 000 m².</li>\n  <li>Cartographiez les habitants non desservis et proposez un terrain pour un nouveau square.</li>\n  <li>Recalculez la part desservie avec ce nouveau square : quel gain ?</li>\n</ol>"
    },
    {
     "id": "v7-l3",
     "titre": "Cartographier l'inventaire des arbres et la végétation (NDVI)",
     "duree": "35 min",
     "objectifs": [
      "Importer l'inventaire des arbres à partir de coordonnées X/Y",
      "Symboliser les arbres par état sanitaire et par espèce",
      "Calculer et interpréter un NDVI à partir d'images Sentinel-2"
     ],
     "contenu": "\n<h4>1. Importer l'inventaire</h4>\n<p><i>Couche &gt; Ajouter une couche &gt; Ajouter une couche de texte délimité</i> : fichier <code>inventaire_arbres.csv</code>, séparateur virgule, géométrie « point », champ X = <code>x</code>, champ Y = <code>y</code>, SCR = EPSG:32630. Exportez ensuite la couche en GeoPackage pour pouvoir la modifier.</p>\n<h4>2. Symbologie et étiquettes</h4>\n<ul>\n  <li><i>Catégorisé</i> sur <code>etat</code> : vert (bon), jaune (moyen), orange (mauvais), rouge (mort).</li>\n  <li>Taille proportionnelle au diamètre de couronne : dans la taille du symbole, utilisez une expression comme :</li>\n</ul>\n<pre><code>\"couronne_m\"</code></pre>\n<p>(Unité : <b>mètres à l'échelle de la carte</b>, pour que le cercle ait la vraie taille de la couronne.)</p>\n<h4>3. Le NDVI</h4>\n<p>Le <b>NDVI</b> (indice de végétation par différence normalisée) mesure la vigueur de la végétation à partir des images satellites : la végétation réfléchit beaucoup le proche infrarouge (PIR) et absorbe le rouge (R).</p>\n<p class=\"formule\">NDVI = (PIR − R) ÷ (PIR + R) &nbsp; ; &nbsp; Sentinel-2 : PIR = bande B8, R = bande B4 (10 m)</p>\n<p>Valeurs : proche de 0 ou négatif pour le bâti, l'eau et le sol nu ; 0,2 à 0,4 pour une végétation clairsemée ou sèche ; au-delà de 0,5 pour une végétation dense et vigoureuse.</p>\n<p>Téléchargez gratuitement les bandes B4 et B8 d'une image Sentinel-2 sur Tlemcen depuis le <b>Copernicus Browser</b> (inscription gratuite), puis <i>Raster &gt; Calculatrice raster</i> :</p>\n<pre><code>(\"B08@1\" - \"B04@1\") / (\"B08@1\" + \"B04@1\")</code></pre>\n<p>Comparez une image de mai et une image d'août : les pelouses non arrosées et les prairies sèchent, les arbres restent verts.</p>",
     "exercice": "<ol>\n  <li>Importez l'inventaire, réalisez la carte de l'état sanitaire avec des cercles à la taille réelle des couronnes.</li>\n  <li>Calculez le taux de canopée de chaque espace vert : somme des surfaces de couronne ÷ surface de l'espace (indication : <i>Joindre les attributs par localisation (résumé)</i>).</li>\n  <li>Avec une image Sentinel-2 réelle, calculez le NDVI de Tlemcen et comparez les quartiers.</li>\n</ol>"
    }
   ],
   "quiz": [
    {
     "question": "Quelle expression QGIS calcule la surface d'un polygone dans le SCR du projet ?",
     "choix": [
      "area_m()",
      "$length",
      "$area",
      "$x"
     ],
     "bonne": 2,
     "explication": "$area renvoie la surface en unités du SCR (m² en UTM)."
    },
    {
     "question": "Pourquoi les données du TP sont-elles en UTM zone 30N ?",
     "choix": [
      "Pour avoir des distances et surfaces en mètres",
      "Parce que QGIS n'accepte que l'UTM",
      "Pour afficher les couleurs",
      "Pour réduire la taille des fichiers"
     ],
     "bonne": 0,
     "explication": "Un système projeté métrique permet de mesurer directement en mètres."
    },
    {
     "question": "Quel outil sert à créer la zone de 300 m autour des espaces verts ?",
     "choix": [
      "Calculatrice raster",
      "Tampon",
      "Union",
      "Géoréférenceur"
     ],
     "bonne": 1,
     "explication": "Le tampon trace une zone à distance fixe autour des entités."
    },
    {
     "question": "Avec Sentinel-2, le NDVI se calcule avec les bandes…",
     "choix": [
      "B11 et B12",
      "B1 et B9",
      "B2 et B3",
      "B8 (PIR) et B4 (rouge)"
     ],
     "bonne": 3,
     "explication": "NDVI = (B8 − B4) ÷ (B8 + B4)."
    },
    {
     "question": "Un NDVI de 0,7 indique…",
     "choix": [
      "une végétation dense et vigoureuse",
      "de l'eau",
      "du bâti",
      "du sol nu"
     ],
     "bonne": 0,
     "explication": "Au-delà de 0,5, la végétation est dense et active."
    }
   ]
  },
  {
   "id": "v8",
   "numero": 8,
   "titre": "Projet, budget et participation",
   "echelle": "1:1",
   "resume": "Chiffrer un projet (métré et devis), rédiger un plan de gestion, associer les habitants et évaluer les résultats.",
   "lecons": [
    {
     "id": "v8-l1",
     "titre": "Métré et devis estimatif",
     "duree": "30 min",
     "objectifs": [
      "Établir le métré (les quantités) d'un projet",
      "Construire un devis estimatif avec des prix unitaires",
      "Estimer le coût d'entretien annuel"
     ],
     "contenu": "\n<p>Le <b>devis estimatif</b> donne le coût prévisionnel du projet. On le construit en deux temps : le <b>métré</b> (les quantités, mesurées sur le plan de masse) puis le <b>chiffrage</b> (quantité × prix unitaire).</p>\n<h4>Structure d'un devis</h4>\n<div class=\"tab-wrap\"><table class=\"tab\"><thead><tr><th>N°</th><th>Désignation</th><th>Unité</th><th>Quantité</th><th>Prix unitaire (DA)</th><th>Montant (DA)</th></tr></thead><tbody>\n<tr><td>1</td><td>Terrassement et apport de terre végétale</td><td>m³</td><td>300</td><td>2 500</td><td>750 000</td></tr>\n<tr><td>2</td><td>Fourniture et plantation d'arbres (circ. 12-14 cm)</td><td>u</td><td>30</td><td>9 000</td><td>270 000</td></tr>\n<tr><td>3</td><td>Fourniture et plantation d'arbustes</td><td>u</td><td>400</td><td>600</td><td>240 000</td></tr>\n<tr><td>4</td><td>Réseau goutte-à-goutte</td><td>ml</td><td>900</td><td>350</td><td>315 000</td></tr>\n<tr><td>5</td><td>Bancs</td><td>u</td><td>20</td><td>35 000</td><td>700 000</td></tr>\n<tr><td colspan=\"5\"><b>Total hors taxes</b></td><td><b>2 275 000</b></td></tr>\n</tbody></table></div>\n<p><b>Attention :</b> ces prix sont <b>fictifs</b>, pour l'exercice. En situation réelle, on utilise les prix des marchés récents de la commune ou des consultations d'entreprises. On ajoute ensuite la TVA et une marge pour imprévus (souvent 5 à 10 %).</p>\n<h4>Le coût de gestion</h4>\n<p>Un espace vert coûte surtout <b>après</b> sa création : eau, main-d'œuvre, remplacements, réparations. On l'estime en m² par classe d'entretien (niveau 6) et on le présente avec le devis, pour que le maître d'ouvrage sache s'il pourra l'entretenir.</p>\n<div class=\"astuce\"><b>Tableur :</b> le classeur <code>devis_estimatif.xlsx</code> du TP contient les formules (Montant = Quantité × PU, sous-totaux, TVA, imprévus). Modifiez les quantités, tout se recalcule.</div>",
     "exercice": "<ol>\n  <li>À partir de votre plan de masse (niveau 4) et de votre liste de mobilier, établissez le métré.</li>\n  <li>Complétez <code>devis_estimatif.xlsx</code> avec vos quantités. Quel est le coût total TTC avec 10 % d'imprévus ?</li>\n  <li>Estimez le coût d'eau annuel du projet avec vos calculs du niveau 5 (prix de l'eau fictif : 40 DA/m³).</li>\n</ol>"
    },
    {
     "id": "v8-l2",
     "titre": "Le plan de gestion d'un espace vert",
     "duree": "25 min",
     "objectifs": [
      "Connaître le contenu d'un plan de gestion",
      "Rédiger des fiches de gestion par espace",
      "Choisir des indicateurs de suivi"
     ],
     "contenu": "\n<p>Le <b>plan de gestion</b> organise l'entretien d'un espace vert (ou de tous ceux d'une commune) sur plusieurs années. Il sert de feuille de route aux équipes et de base aux cahiers des charges des entreprises.</p>\n<h4>Contenu type</h4>\n<ol>\n  <li><b>Diagnostic</b> : inventaire, état sanitaire, usages, problèmes (niveaux 1 à 3).</li>\n  <li><b>Objectifs</b> : par exemple « augmenter la canopée de 20 % à 25 % en 10 ans », « réduire la consommation d'eau de 30 % », « zéro pesticide ».</li>\n  <li><b>Classes d'entretien</b> et carte de gestion différenciée (niveau 6).</li>\n  <li><b>Fiches de gestion</b> : pour chaque espace, les opérations, leur fréquence, la période et les moyens (agents, matériel).</li>\n  <li><b>Programme pluriannuel</b> : plantations, remplacements, rénovations, avec un budget par année.</li>\n  <li><b>Indicateurs de suivi</b> : nombre d'arbres plantés et morts, taux de canopée, m³ d'eau consommés, m²/hab, satisfaction des usagers.</li>\n</ol>\n<h4>Exemple de fiche de gestion</h4>\n<div class=\"tab-wrap\"><table class=\"tab\"><thead><tr><th>Opération</th><th>Fréquence</th><th>Période</th></tr></thead><tbody>\n<tr><td>Tonte de la pelouse centrale</td><td>2 fois par mois</td><td>Mars à juin, octobre</td></tr>\n<tr><td>Fauche de la prairie</td><td>2 fois par an</td><td>Juin et octobre</td></tr>\n<tr><td>Contrôle de l'arrosage</td><td>Chaque semaine</td><td>Mai à septembre</td></tr>\n<tr><td>Visite sanitaire des arbres</td><td>1 fois par an</td><td>Hiver</td></tr>\n<tr><td>Contrôle de l'aire de jeux</td><td>Visuel chaque semaine, approfondi chaque année</td><td>Toute l'année</td></tr>\n</tbody></table></div>",
     "exercice": "<ol>\n  <li>Rédigez le plan de gestion (4 pages maximum) du square de votre projet avec la structure de la leçon.</li>\n  <li>Remplissez une fiche de gestion pour chacune des zones (pelouse, massifs, arbres, jeux).</li>\n  <li>Choisissez 5 indicateurs et leur valeur cible à 5 ans.</li>\n</ol>"
    },
    {
     "id": "v8-l3",
     "titre": "Associer les habitants et évaluer le projet",
     "duree": "25 min",
     "objectifs": [
      "Organiser la participation des habitants",
      "Préparer et analyser une enquête auprès des usagers",
      "Présenter un projet de façon claire"
     ],
     "contenu": "\n<p>Un espace vert conçu <b>avec</b> les habitants est mieux respecté et mieux utilisé. La participation peut intervenir à chaque étape.</p>\n<h4>Formes de participation</h4>\n<ul>\n  <li><b>Avant le projet</b> : questionnaire, réunion de quartier, balade diagnostic avec les habitants, ateliers avec les enfants de l'école voisine.</li>\n  <li><b>Pendant</b> : présentation des esquisses, choix entre deux variantes, journée de plantation collective.</li>\n  <li><b>Après</b> : jardins partagés, parrainage d'arbres par des familles ou des classes, comités d'usagers, signalement des problèmes.</li>\n</ul>\n<h4>L'enquête auprès des usagers</h4>\n<p>Questions courtes, fermées si possible : fréquence de visite, temps d'accès, activités, satisfaction (de 1 à 5) sur l'ombre, la propreté, la sécurité, les jeux, et une question ouverte « que faudrait-il améliorer ? ». Le fichier <code>enquete_usagers.csv</code> du TP contient 120 réponses fictives à analyser.</p>\n<h4>Présenter le projet</h4>\n<p>Pour un jury ou un conseil communal : une affiche ou un diaporama avec le diagnostic (cartes), le plan de masse, deux ou trois vues d'ambiance, la palette végétale, le devis et le plan de gestion. Un message clair : « ce que le projet apporte au quartier ».</p>\n<div class=\"astuce\"><b>À retenir :</b> l'évaluation boucle le projet. Les indicateurs (canopée, m²/hab, eau, satisfaction) mesurés avant et après montrent si les objectifs sont atteints et nourrissent le projet suivant.</div>",
     "exercice": "<ol>\n  <li>Analysez <code>enquete_usagers.csv</code> dans un tableur : note moyenne de chaque critère, part des usagers venant à pied, trois améliorations les plus demandées.</li>\n  <li>Proposez trois actions de participation pour votre projet de square.</li>\n  <li>Projet final : présentez votre square (diagnostic, plan de masse, palette, irrigation, devis, plan de gestion) en 10 diapositives.</li>\n</ol>"
    }
   ],
   "quiz": [
    {
     "question": "Que contient le métré d'un projet ?",
     "choix": [
      "Les quantités mesurées sur le plan",
      "La liste des usagers",
      "Les prix unitaires",
      "Le planning d'entretien"
     ],
     "bonne": 0,
     "explication": "Le métré mesure les quantités ; le chiffrage les multiplie par les prix unitaires."
    },
    {
     "question": "30 arbres à 9 000 DA l'unité coûtent…",
     "choix": [
      "2 700 000 DA",
      "39 000 DA",
      "27 000 DA",
      "270 000 DA"
     ],
     "bonne": 3,
     "explication": "30 × 9 000 = 270 000 DA."
    },
    {
     "question": "Pourquoi présenter le coût d'entretien avec le devis de création ?",
     "choix": [
      "Parce que la loi interdit l'entretien",
      "Parce que l'espace vert coûte surtout après sa création",
      "Pour gonfler le budget",
      "Ce n'est pas utile"
     ],
     "bonne": 1,
     "explication": "Eau, main-d'œuvre et remplacements pèsent chaque année."
    },
    {
     "question": "Lequel est un indicateur de suivi d'un plan de gestion ?",
     "choix": [
      "Le taux de canopée",
      "Le nom de l'architecte",
      "La marque des tondeuses",
      "La couleur des bancs"
     ],
     "bonne": 0,
     "explication": "Le taux de canopée mesure l'évolution du couvert arboré."
    },
    {
     "question": "Quel est un intérêt principal de la participation des habitants ?",
     "choix": [
      "Éviter de faire un diagnostic",
      "Réduire le nombre d'arbres",
      "Supprimer l'entretien",
      "Un espace mieux utilisé et mieux respecté"
     ],
     "bonne": 3,
     "explication": "Les habitants qui ont participé s'approprient l'espace."
    }
   ]
  }
 ]
};

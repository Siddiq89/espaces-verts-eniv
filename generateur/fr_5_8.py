from outils import C, lecon, q

N5 = dict(id="v5", numero=5, titre="Sol, plantation et irrigation", echelle="1:20",
  resume="Préparer le sol, planter un arbre dans les règles, calculer les besoins en eau et concevoir un arrosage économe.",
  lecons=[
  lecon("v5-l1", "Le sol et la fosse de plantation", "25 min",
    ["Décrire les qualités d'une bonne terre végétale",
     "Dimensionner une fosse de plantation en ville",
     "Prévenir le tassement du sol"],
    """
<p>Les racines vivent dans le sol : un arbre dans un mauvais sol restera chétif toute sa vie, quels que soient les soins. En ville, le sol est souvent fait de <b>remblais</b>, de gravats, compacté par les engins et les voitures.</p>
<h4>Une bonne terre végétale</h4>
<ul>
  <li><b>Texture</b> équilibrée (sable, limon, argile) : ni trop collante, ni trop filtrante. Test simple : une poignée de terre humide forme une boule qui se casse sous une légère pression.</li>
  <li><b>Matière organique</b> : 2 à 5 % ; on améliore avec du compost mûr.</li>
  <li><b>Structure</b> aérée : l'air et l'eau doivent circuler. Un sol tassé asphyxie les racines.</li>
  <li><b>pH</b> : les sols de la région de Tlemcen sont souvent calcaires (pH 7,5 à 8,5) ; choisir des espèces qui le tolèrent.</li>
</ul>
<h4>La fosse de plantation</h4>
<ul>
  <li>Volume : <b>le plus grand possible</b>. Pour un grand arbre d'alignement, on vise souvent 10 m³ de terre ou plus ; une petite fosse de 1 m³ condamne l'arbre à rester petit et à mourir jeune.</li>
  <li>Quand le trottoir est étroit, on relie les fosses entre elles (<b>tranchée continue</b>) ou on utilise des <b>mélanges terre-pierre</b> porteurs qui laissent passer les racines sous les trottoirs.</li>
  <li>Décompacter le fond et les parois, ne pas mettre de couche de gravier au fond.</li>
</ul>
<h4>Protéger le sol</h4>
<p>Pendant les chantiers, on clôture la zone sous la couronne des arbres existants (aucun engin, aucun stockage). Dans les espaces verts, on évite que les voitures se garent sur les pelouses et au pied des arbres. Le <b>paillage</b> (copeaux de bois, broyat) protège le sol du soleil, garde l'humidité et nourrit la vie du sol.</p>""",
    """<ol>
  <li>Prélevez un peu de terre dans deux endroits (pelouse, pied d'arbre de rue) : faites le test de la boule et observez la couleur, les cailloux, les racines.</li>
  <li>Une rue fictive de 300 m doit recevoir des micocouliers tous les 8 m d'un seul côté. Combien d'arbres ? Quel volume total de terre pour 10 m³ par arbre ?</li>
  <li>Proposez une solution si le trottoir ne fait que 2 m de large.</li>
</ol>"""),
  lecon("v5-l2", "Planter un arbre dans les règles", "25 min",
    ["Choisir la période et le plant",
     "Réaliser une plantation étape par étape",
     "Assurer l'arrosage et le suivi des premières années"],
    """
<h4>La période</h4>
<p>On plante pendant le <b>repos végétatif</b>, de novembre à mars, hors périodes de gel ou de sol détrempé. Les plants en <b>racines nues</b> doivent absolument être plantés à cette période ; les plants en <b>conteneur</b> ou en <b>motte</b> tolèrent une période un peu plus longue, mais jamais en plein été à Tlemcen.</p>
<h4>Choisir le plant</h4>
<p>Tronc droit, flèche (pousse terminale) intacte, racines non enroulées en spirale dans le pot, pas de blessure. Un jeune plant (circonférence 10-14 cm) reprend souvent mieux qu'un gros sujet.</p>
<h4>Étapes</h4>
<ol>
  <li>Ouvrir la fosse et ameublir le fond.</li>
  <li>Placer le ou les <b>tuteurs</b> avant l'arbre (côté vent dominant), sans blesser les racines.</li>
  <li>Démêler les racines qui tournent, couper les racines abîmées.</li>
  <li>Placer l'arbre : le <b>collet</b> (jonction tronc-racines) au niveau du sol fini, jamais enterré.</li>
  <li>Reboucher avec la terre végétale (amendée de compost), tasser légèrement au pied.</li>
  <li>Former une <b>cuvette d'arrosage</b> et arroser abondamment (au moins 50 litres) même s'il pleut.</li>
  <li>Attacher l'arbre au tuteur avec un lien souple qui ne blesse pas l'écorce ; pailler la cuvette.</li>
</ol>
<h4>Le suivi</h4>
<p>Pendant les <b>2 à 3 premiers étés</b>, arroser régulièrement (par exemple 50 litres une fois par semaine, à adapter à la météo et au sol). Desserrer les liens chaque année, retirer les tuteurs après 2 à 3 ans. Remplacer les sujets morts dès l'hiver suivant.</p>
<div class="astuce"><b>Erreur fréquente :</b> enterrer le collet. L'écorce du tronc pourrit, l'arbre dépérit lentement. Le collet doit rester visible.</div>""",
    """<ol>
  <li>Rédigez une fiche de chantier illustrée (schéma de la fosse, tuteur, cuvette) pour la plantation d'un frêne.</li>
  <li>Si possible, participez à la plantation d'un arbre dans l'établissement et photographiez chaque étape.</li>
  <li>Prévoyez le calendrier d'arrosage des 3 premiers étés et la quantité d'eau totale.</li>
</ol>"""),
  lecon("v5-l3", "Calculer les besoins en eau et concevoir l'arrosage", "35 min",
    ["Comprendre l'évapotranspiration de référence (ET0)",
     "Calculer le besoin en eau d'une surface plantée",
     "Choisir un système d'arrosage économe"],
    """
<p>L'eau est rare à Tlemcen en été : un espace vert doit être conçu pour <b>consommer peu</b>. On calcule ses besoins à partir de l'<b>évapotranspiration de référence</b> (ET0) : la quantité d'eau, en mm par jour, perdue par une pelouse de référence bien arrosée. 1 mm sur 1 m² = 1 litre.</p>
<h4>Le calcul</h4>
<p class="formule">Besoin (L/jour) = ET0 (mm/j) × KL × Surface (m²) ÷ Efficience</p>
<ul>
  <li><b>KL</b>, coefficient de plantation : environ 0,2 à 0,3 pour des plantes sobres (olivier, romarin, lentisque) ; 0,4 à 0,6 pour des massifs moyens ; 0,7 à 0,8 pour un gazon.</li>
  <li><b>Efficience</b> du système : goutte-à-goutte ≈ 0,9 ; aspersion ≈ 0,7 (une partie s'évapore ou part avec le vent).</li>
  <li>On retire la pluie utile quand il pleut (rarement en été).</li>
</ul>
<h4>Exemple (juillet, ET0 = 6 mm/j, valeurs du fichier <code>et0_tlemcen.csv</code> du TP)</h4>
<div class="tab-wrap"><table class="tab"><thead><tr><th>Zone</th><th>Surface</th><th>KL</th><th>Système</th><th>Besoin</th></tr></thead><tbody>
<tr><td>Gazon</td><td>800 m²</td><td>0,8</td><td>Aspersion (0,7)</td><td>6 × 0,8 × 800 ÷ 0,7 ≈ 5 490 L/j</td></tr>
<tr><td>Massifs méditerranéens</td><td>800 m²</td><td>0,3</td><td>Goutte-à-goutte (0,9)</td><td>6 × 0,3 × 800 ÷ 0,9 = 1 600 L/j</td></tr>
</tbody></table></div>
<p>À surface égale, les massifs sobres au goutte-à-goutte consomment <b>3,4 fois moins</b> que le gazon arrosé par aspersion.</p>
<h4>Bonnes pratiques</h4>
<ul>
  <li><b>Hydrozones</b> : regrouper les plantes selon leurs besoins et les arroser par secteurs séparés.</li>
  <li>Arroser <b>tôt le matin ou la nuit</b>, moins souvent mais plus longtemps (racines profondes).</li>
  <li><b>Pailler</b> : réduit fortement l'évaporation.</li>
  <li>Utiliser des <b>eaux non conventionnelles</b> quand c'est autorisé : eaux de pluie stockées, eaux usées épurées selon la réglementation.</li>
  <li>Le <b>xéropaysagisme</b> (jardin sec) : plantes adaptées, peu de gazon, paillage minéral ou végétal.</li>
</ul>""",
    """<ol>
  <li>Ouvrez <code>et0_tlemcen.csv</code> et calculez le besoin mensuel en eau (m³) du square de 2 000 m² de votre palette (niveau 2) : précisez les surfaces de chaque zone.</li>
  <li>Comparez deux variantes : 50 % de gazon ou 10 % de gazon. Quelle économie d'eau sur l'année ?</li>
  <li>Le classeur <code>calcul_irrigation.xlsx</code> du TP contient le modèle de calcul : vérifiez vos résultats.</li>
</ol>"""),
  ],
  quiz=[
    q("À quelle période plante-t-on les arbres en racines nues ?", ["En plein été", "Pendant le repos végétatif, de novembre à mars hors gel", "Uniquement en avril", "N'importe quand"], 1, "Les racines nues ne supportent la plantation que pendant le repos végétatif."),
    q("Où doit se trouver le collet après la plantation ?", ["Enterré de 20 cm", "Au niveau du sol fini", "50 cm au-dessus du sol", "Dans la couche de gravier"], 1, "Un collet enterré entraîne la pourriture de l'écorce."),
    q("ET0 = 5 mm/j, KL = 0,3, surface 100 m², goutte-à-goutte (0,9). Besoin journalier ?", ["≈ 167 L", "≈ 150 L", "≈ 1 500 L", "≈ 15 L"], 0, "5 × 0,3 × 100 ÷ 0,9 ≈ 167 litres par jour."),
    q("Pourquoi regroupe-t-on les plantes en hydrozones ?", ["Pour arroser chaque groupe selon ses besoins réels", "Pour faire de jolies couleurs", "Pour éviter la taille", "Pour réduire le nombre d'arbres"], 0, "Chaque secteur d'arrosage reçoit la dose adaptée à ses plantes."),
    q("Quel volume de terre vise-t-on souvent pour un grand arbre d'alignement ?", ["0,5 m³", "1 m³", "10 m³ ou plus", "Aucune terre, du gravier suffit"], 2, "Un grand volume de terre permet à l'arbre de développer ses racines et de vivre longtemps."),
  ])

N6 = dict(id="v6", numero=6, titre="Entretien et gestion durable", echelle="1:200",
  resume="Planifier l'entretien sur l'année, appliquer la gestion différenciée, tailler correctement et protéger les végétaux sans pesticides.",
  lecons=[
  lecon("v6-l1", "Calendrier d'entretien et gestion différenciée", "25 min",
    ["Établir le calendrier annuel des travaux d'entretien",
     "Appliquer la gestion différenciée par classes d'entretien",
     "Valoriser les déchets verts"],
    """
<h4>Le calendrier annuel (climat de Tlemcen)</h4>
<div class="tab-wrap"><table class="tab"><thead><tr><th>Période</th><th>Travaux principaux</th></tr></thead><tbody>
<tr><td>Novembre à mars</td><td>Plantations, taille des arbres caducs, échenillage des nids de processionnaire, entretien du mobilier, paillage.</td></tr>
<tr><td>Mars à mai</td><td>Tontes, désherbage manuel, mise en route et contrôle de l'arrosage, fleurissement de printemps. Pas de taille lourde pendant la nidification des oiseaux.</td></tr>
<tr><td>Juin à septembre</td><td>Arrosage (le poste principal), surveillance des jeunes arbres, ramassage des déchets, prévention des incendies (débroussaillement des zones boisées).</td></tr>
<tr><td>Octobre</td><td>Bilan de l'été, préparation des plantations, semis de prairies, récolte des feuilles pour le compost.</td></tr>
</tbody></table></div>
<h4>La gestion différenciée</h4>
<p>Tous les espaces n'ont pas besoin du même entretien. La <b>gestion différenciée</b> attribue à chaque espace une <b>classe d'entretien</b> :</p>
<ul>
  <li><b>Classe 1, horticole</b> : places et entrées de prestige, massifs fleuris, gazon tondu court. Entretien intensif.</li>
  <li><b>Classe 2, jardinée</b> : squares et jardins de quartier, entretien régulier.</li>
  <li><b>Classe 3, rustique</b> : grandes pelouses fauchées moins souvent, arbustes en port libre.</li>
  <li><b>Classe 4, naturelle</b> : berges, coteaux, prairies fauchées une à deux fois par an, bois morts laissés pour la faune (si sans danger).</li>
</ul>
<p>Avantages : moins d'eau, moins d'heures de travail, plus de biodiversité, et des moyens concentrés là où ils sont visibles et utiles. Il faut l'<b>expliquer aux habitants</b> (panneaux) : une prairie non tondue n'est pas un espace abandonné.</p>
<h4>Les déchets verts</h4>
<p>Tontes, feuilles et branches broyées deviennent du <b>compost</b> ou du <b>paillage</b> : on ferme le cycle et on réduit les achats d'engrais et de paillis.</p>""",
    """<ol>
  <li>Dans QGIS, ouvrez <code>espaces_verts.geojson</code> et ajoutez un champ <code>classe_entretien</code> (1 à 4).</li>
  <li>Attribuez une classe à chaque espace en justifiant (fréquentation, usage, intérêt écologique).</li>
  <li>Faites une carte de la gestion différenciée avec une couleur par classe et calculez la surface de chaque classe.</li>
</ol>"""),
  lecon("v6-l2", "La taille des arbres", "30 min",
    ["Distinguer les types de taille et leurs objectifs",
     "Réaliser une coupe correcte au ras du col de la branche",
     "Refuser l'étêtage et connaître les règles de sécurité"],
    """
<p>Un arbre bien planté, à la bonne place, a <b>peu besoin d'être taillé</b>. La taille répond à un objectif précis ; elle n'est jamais systématique.</p>
<h4>Les types de taille</h4>
<ul>
  <li><b>Taille de formation</b> (jeunes arbres) : garder une flèche unique, supprimer les fourches en V, relever progressivement les branches basses au-dessus des passages.</li>
  <li><b>Taille d'entretien</b> : supprimer le bois mort, les branches cassées, malades ou qui se croisent.</li>
  <li><b>Taille de sécurité</b> : supprimer une branche dangereuse au-dessus d'une allée ou d'une aire de jeux.</li>
  <li><b>Taille architecturée</b> (rideaux, têtes de chat, palmettes) : seulement sur des arbres conduits ainsi depuis leur jeunesse, et à renouveler régulièrement.</li>
</ul>
<h4>La bonne coupe</h4>
<p>On coupe juste à l'extérieur du <b>col de la branche</b> (le renflement à sa base), sans l'abîmer et sans laisser de <b>chicot</b>. Le col contient les tissus qui referment la plaie. Pour une grosse branche, on procède en trois coupes (entaille dessous, coupe dessus plus loin, puis coupe finale) pour éviter l'arrachement de l'écorce.</p>
<h4>Ce qu'il ne faut pas faire</h4>
<ul>
  <li><b>L'étêtage</b> (couper toutes les grosses branches) : l'arbre réagit par des rejets fragiles, pourrit par les grosses plaies et devient dangereux. C'est une mauvaise pratique encore fréquente.</li>
  <li>Enlever plus d'environ un quart du feuillage en une seule fois.</li>
  <li>Utiliser des griffes (éperons) pour grimper sur un arbre qu'on ne va pas abattre.</li>
</ul>
<h4>Sécurité</h4>
<p>Le travail en hauteur est réservé à du personnel formé et équipé : casque, lunettes, gants, pantalon anti-coupure pour la tronçonneuse, harnais et cordes ou nacelle. Le chantier est balisé, la circulation protégée.</p>""",
    """<ol>
  <li>Sur des photos d'arbres de votre ville, repérez des exemples d'étêtage, de chicots et de coupes correctes.</li>
  <li>Dessinez les trois coupes nécessaires pour retirer une grosse branche, en indiquant le col.</li>
  <li>Dans <code>inventaire_arbres.csv</code>, listez les arbres pour lesquels une taille est proposée et précisez le type de taille.</li>
</ol>"""),
  lecon("v6-l3", "Protéger les végétaux sans pesticides : la lutte intégrée", "25 min",
    ["Reconnaître la processionnaire du pin et ses dangers",
     "Combiner les méthodes de lutte intégrée",
     "Organiser un suivi sanitaire du patrimoine"],
    """
<p>La <b>lutte intégrée</b> combine plusieurs méthodes et n'utilise un produit qu'en dernier recours. Dans les lieux publics, on cherche à se passer des pesticides chimiques, dangereux pour les usagers, les agents et la faune utile.</p>
<h4>Exemple : la processionnaire du pin</h4>
<p>La chenille de <i>Thaumetopoea pityocampa</i> vit en colonies dans des <b>nids soyeux blancs</b> au bout des branches de pins et de cèdres. Elle dévore les aiguilles et ses <b>poils urticants</b> provoquent des réactions graves chez l'homme et les animaux (yeux, peau, voies respiratoires). En fin d'hiver, les chenilles descendent en file indienne pour s'enterrer.</p>
<ul>
  <li><b>Hiver</b> : échenillage, c'est-à-dire couper et détruire les nids, par des agents équipés (combinaison, masque, lunettes).</li>
  <li><b>Fin d'hiver</b> : <b>colliers pièges</b> autour des troncs qui capturent les chenilles lors de leur descente.</li>
  <li><b>Été</b> : <b>pièges à phéromones</b> qui capturent les papillons mâles.</li>
  <li><b>Automne</b> : traitement biologique au <i>Bacillus thuringiensis</i> sur les jeunes chenilles si l'infestation est forte.</li>
  <li><b>Toute l'année</b> : nichoirs à mésanges, grandes consommatrices de chenilles ; diversification des essences.</li>
</ul>
<h4>Autres méthodes</h4>
<ul>
  <li><b>Prévention</b> : bonnes espèces au bon endroit, sol vivant, arrosage adapté : une plante en bonne santé résiste mieux.</li>
  <li><b>Lutte mécanique</b> : désherbage manuel ou thermique, taille des parties atteintes.</li>
  <li><b>Lutte biologique</b> : auxiliaires (coccinelles contre les pucerons), nichoirs, haies refuges.</li>
</ul>
<h4>Le suivi sanitaire</h4>
<p>Notez chaque observation (date, lieu, arbre, ravageur, intensité) dans l'inventaire : on repère les foyers, on mesure l'efficacité des actions et on prévoit les campagnes de l'année suivante.</p>""",
    """<ol>
  <li>Dans <code>inventaire_arbres.csv</code>, comptez les pins signalés avec des nids de processionnaire (champ <code>defaut</code> = « Nids processionnaire »).</li>
  <li>Cartographiez-les dans QGIS : sont-ils près des écoles et des aires de jeux ?</li>
  <li>Rédigez le plan d'action annuel de lutte intégrée pour ces arbres, mois par mois.</li>
</ol>"""),
  ],
  quiz=[
    q("Quelle classe de gestion différenciée correspond aux berges et prairies fauchées une à deux fois par an ?", ["Classe 1, horticole", "Classe 2, jardinée", "Classe 3, rustique", "Classe 4, naturelle"], 3, "La classe naturelle réduit les interventions au minimum."),
    q("Où faut-il couper une branche ?", ["Au ras du tronc, en enlevant le col", "Juste à l'extérieur du col, sans chicot", "À 30 cm du tronc", "Au milieu de la branche"], 1, "Le col contient les tissus qui referment la plaie."),
    q("Pourquoi l'étêtage est-il une mauvaise pratique ?", ["Il donne des rejets fragiles et de grosses plaies qui pourrissent", "Il fait trop d'ombre", "Il coûte trop peu", "Il est obligatoire chaque année"], 0, "L'arbre étêté devient fragile et dangereux."),
    q("Quand utilise-t-on les colliers pièges contre la processionnaire ?", ["En été", "En fin d'hiver, lors de la descente des chenilles", "En automne", "Jamais"], 1, "Les colliers capturent les chenilles qui descendent le long du tronc."),
    q("Dans la lutte intégrée, le produit de traitement est utilisé…", ["en premier, de façon préventive", "en dernier recours", "chaque mois", "uniquement sur les pelouses"], 1, "On combine d'abord prévention, lutte mécanique et biologique."),
  ])

N7 = dict(id="v7", numero=7, titre="Cartographier les espaces verts avec QGIS", echelle="1:10 000",
  resume="Numériser et mesurer les espaces verts, calculer les indicateurs par quartier, analyser l'accessibilité et exploiter l'inventaire des arbres et le NDVI.",
  lecons=[
  lecon("v7-l1", "Cartographier les espaces verts et calculer les surfaces", "30 min",
    ["Ouvrir les couches du TP dans QGIS avec le bon système de coordonnées",
     "Numériser un nouvel espace vert",
     "Calculer les surfaces et le ratio m² par habitant par quartier"],
    """
<p>QGIS est un SIG libre et gratuit (qgis.org, version LTR conseillée). Les couches du TP sont en <b>WGS 84 / UTM zone 30N (EPSG 32630)</b> : les distances et les surfaces sont en mètres.</p>
<h4>1. Ouvrir les données</h4>
<ol>
  <li><i>Projet &gt; Propriétés &gt; SCR</i> : choisir EPSG:32630.</li>
  <li>Glisser-déposer <code>quartiers.geojson</code> et <code>espaces_verts.geojson</code> dans QGIS.</li>
  <li>Ajouter un fond OpenStreetMap : panneau <i>Navigateur &gt; XYZ Tiles &gt; OpenStreetMap</i>.</li>
</ol>
<h4>2. Numériser un espace vert</h4>
<p>Sélectionnez la couche <code>espaces_verts</code>, cliquez sur <i>Basculer en mode édition</i> (crayon), puis <i>Ajouter une entité polygone</i>. Cliquez les sommets, clic droit pour terminer, remplissez les attributs (nom, catégorie), enregistrez.</p>
<h4>3. Calculer les surfaces</h4>
<p>Ouvrez la <i>Calculatrice de champs</i>, créez un champ décimal <code>surface_m2</code> avec l'expression :</p>
""" + C('$area') + """
<h4>4. Surface d'espaces verts par quartier</h4>
<p>Outil <i>Traitement &gt; Boîte à outils &gt; Joindre les attributs par localisation (résumé)</i> : couche cible <code>quartiers</code>, couche à joindre <code>espaces_verts</code>, prédicat « intersecte », champ <code>surface_m2</code>, résumé « somme ». (Pour être exact, découpez d'abord les espaces verts par les quartiers avec l'outil <i>Intersection</i>.) Puis, dans la nouvelle couche, calculez le ratio :</p>
""" + C('"surface_m2_sum" / "population"') + """
<p>Représentez ce champ en <i>Symbologie &gt; Gradué</i> : vous obtenez la carte des quartiers déficitaires (moins de 9 m²/hab).</p>""",
    """<ol>
  <li>Réalisez les étapes de la leçon avec les données du TP.</li>
  <li>Quels quartiers sont sous 9 m²/hab ? Quelle surface faudrait-il créer dans chacun ?</li>
  <li>Faites une mise en page (titre, légende, échelle, nord, source « données fictives ENIV ») et exportez-la en PDF.</li>
</ol>"""),
  lecon("v7-l2", "Analyser l'accessibilité des espaces verts", "30 min",
    ["Créer une zone tampon de 300 m autour des espaces verts",
     "Estimer la part de la population à moins de 300 m",
     "Proposer l'emplacement d'un nouvel espace vert"],
    """
<p>Avoir assez d'espaces verts ne suffit pas : il faut qu'ils soient <b>proches</b> des habitants. Selon la règle 3-30-300 (niveau 1), chacun devrait vivre à moins de <b>300 m</b> d'un espace vert.</p>
<h4>1. Zone tampon</h4>
<p><i>Vecteur &gt; Outils de géotraitement &gt; Tampon</i> : couche <code>espaces_verts</code>, distance <b>300</b> mètres, cochez <i>Regrouper le résultat</i>. On peut d'abord filtrer les petits espaces (par exemple ne garder que ceux de plus de 5 000 m²) avec l'expression :</p>
""" + C('"surface_m2" >= 5000') + """
<h4>2. Population desservie</h4>
<p>La couche <code>batiments_habitat.geojson</code> du TP contient des points d'habitat avec un nombre d'habitants (champ <code>habitants</code>). Utilisez <i>Sélection par localisation</i> : sélectionner les points qui « intersectent » la zone tampon. La somme des habitants sélectionnés (panneau <i>Statistiques</i>) divisée par la population totale donne la <b>part de la population desservie</b>.</p>
<h4>3. Zones blanches et proposition</h4>
<p>Inversez la sélection : les points restants sont les habitants <b>non desservis</b>. Avec une <i>Carte de chaleur</i> (symbologie) sur ces points, repérez la zone où un nouvel espace vert serait le plus utile. Vérifiez ensuite qu'un terrain libre y existe (couche <code>terrains_libres.geojson</code>).</p>
<div class="astuce"><b>Pour aller plus loin :</b> la distance à vol d'oiseau surestime l'accessibilité. Avec l'outil <i>Zone de desserte</i> (analyse de réseau) et les rues d'OpenStreetMap, on calcule la vraie distance à pied.</div>""",
    """<ol>
  <li>Calculez la part de la population à moins de 300 m d'un espace vert de plus de 5 000 m².</li>
  <li>Cartographiez les habitants non desservis et proposez un terrain pour un nouveau square.</li>
  <li>Recalculez la part desservie avec ce nouveau square : quel gain ?</li>
</ol>"""),
  lecon("v7-l3", "Cartographier l'inventaire des arbres et la végétation (NDVI)", "35 min",
    ["Importer l'inventaire des arbres à partir de coordonnées X/Y",
     "Symboliser les arbres par état sanitaire et par espèce",
     "Calculer et interpréter un NDVI à partir d'images Sentinel-2"],
    """
<h4>1. Importer l'inventaire</h4>
<p><i>Couche &gt; Ajouter une couche &gt; Ajouter une couche de texte délimité</i> : fichier <code>inventaire_arbres.csv</code>, séparateur virgule, géométrie « point », champ X = <code>x</code>, champ Y = <code>y</code>, SCR = EPSG:32630. Exportez ensuite la couche en GeoPackage pour pouvoir la modifier.</p>
<h4>2. Symbologie et étiquettes</h4>
<ul>
  <li><i>Catégorisé</i> sur <code>etat</code> : vert (bon), jaune (moyen), orange (mauvais), rouge (mort).</li>
  <li>Taille proportionnelle au diamètre de couronne : dans la taille du symbole, utilisez une expression comme :</li>
</ul>
""" + C('"couronne_m"') + """
<p>(Unité : <b>mètres à l'échelle de la carte</b>, pour que le cercle ait la vraie taille de la couronne.)</p>
<h4>3. Le NDVI</h4>
<p>Le <b>NDVI</b> (indice de végétation par différence normalisée) mesure la vigueur de la végétation à partir des images satellites : la végétation réfléchit beaucoup le proche infrarouge (PIR) et absorbe le rouge (R).</p>
<p class="formule">NDVI = (PIR − R) ÷ (PIR + R) &nbsp; ; &nbsp; Sentinel-2 : PIR = bande B8, R = bande B4 (10 m)</p>
<p>Valeurs : proche de 0 ou négatif pour le bâti, l'eau et le sol nu ; 0,2 à 0,4 pour une végétation clairsemée ou sèche ; au-delà de 0,5 pour une végétation dense et vigoureuse.</p>
<p>Téléchargez gratuitement les bandes B4 et B8 d'une image Sentinel-2 sur Tlemcen depuis le <b>Copernicus Browser</b> (inscription gratuite), puis <i>Raster &gt; Calculatrice raster</i> :</p>
""" + C('("B08@1" - "B04@1") / ("B08@1" + "B04@1")') + """
<p>Comparez une image de mai et une image d'août : les pelouses non arrosées et les prairies sèchent, les arbres restent verts.</p>""",
    """<ol>
  <li>Importez l'inventaire, réalisez la carte de l'état sanitaire avec des cercles à la taille réelle des couronnes.</li>
  <li>Calculez le taux de canopée de chaque espace vert : somme des surfaces de couronne ÷ surface de l'espace (indication : <i>Joindre les attributs par localisation (résumé)</i>).</li>
  <li>Avec une image Sentinel-2 réelle, calculez le NDVI de Tlemcen et comparez les quartiers.</li>
</ol>"""),
  ],
  quiz=[
    q("Quelle expression QGIS calcule la surface d'un polygone dans le SCR du projet ?", ["$length", "$area", "$x", "area_m()"], 1, "$area renvoie la surface en unités du SCR (m² en UTM)."),
    q("Pourquoi les données du TP sont-elles en UTM zone 30N ?", ["Pour avoir des distances et surfaces en mètres", "Parce que QGIS n'accepte que l'UTM", "Pour afficher les couleurs", "Pour réduire la taille des fichiers"], 0, "Un système projeté métrique permet de mesurer directement en mètres."),
    q("Quel outil sert à créer la zone de 300 m autour des espaces verts ?", ["Tampon", "Union", "Calculatrice raster", "Géoréférenceur"], 0, "Le tampon trace une zone à distance fixe autour des entités."),
    q("Avec Sentinel-2, le NDVI se calcule avec les bandes…", ["B2 et B3", "B8 (PIR) et B4 (rouge)", "B11 et B12", "B1 et B9"], 1, "NDVI = (B8 − B4) ÷ (B8 + B4)."),
    q("Un NDVI de 0,7 indique…", ["de l'eau", "du bâti", "une végétation dense et vigoureuse", "du sol nu"], 2, "Au-delà de 0,5, la végétation est dense et active."),
  ])

N8 = dict(id="v8", numero=8, titre="Projet, budget et participation", echelle="1:1",
  resume="Chiffrer un projet (métré et devis), rédiger un plan de gestion, associer les habitants et évaluer les résultats.",
  lecons=[
  lecon("v8-l1", "Métré et devis estimatif", "30 min",
    ["Établir le métré (les quantités) d'un projet",
     "Construire un devis estimatif avec des prix unitaires",
     "Estimer le coût d'entretien annuel"],
    """
<p>Le <b>devis estimatif</b> donne le coût prévisionnel du projet. On le construit en deux temps : le <b>métré</b> (les quantités, mesurées sur le plan de masse) puis le <b>chiffrage</b> (quantité × prix unitaire).</p>
<h4>Structure d'un devis</h4>
<div class="tab-wrap"><table class="tab"><thead><tr><th>N°</th><th>Désignation</th><th>Unité</th><th>Quantité</th><th>Prix unitaire (DA)</th><th>Montant (DA)</th></tr></thead><tbody>
<tr><td>1</td><td>Terrassement et apport de terre végétale</td><td>m³</td><td>300</td><td>2 500</td><td>750 000</td></tr>
<tr><td>2</td><td>Fourniture et plantation d'arbres (circ. 12-14 cm)</td><td>u</td><td>30</td><td>9 000</td><td>270 000</td></tr>
<tr><td>3</td><td>Fourniture et plantation d'arbustes</td><td>u</td><td>400</td><td>600</td><td>240 000</td></tr>
<tr><td>4</td><td>Réseau goutte-à-goutte</td><td>ml</td><td>900</td><td>350</td><td>315 000</td></tr>
<tr><td>5</td><td>Bancs</td><td>u</td><td>20</td><td>35 000</td><td>700 000</td></tr>
<tr><td colspan="5"><b>Total hors taxes</b></td><td><b>2 275 000</b></td></tr>
</tbody></table></div>
<p><b>Attention :</b> ces prix sont <b>fictifs</b>, pour l'exercice. En situation réelle, on utilise les prix des marchés récents de la commune ou des consultations d'entreprises. On ajoute ensuite la TVA et une marge pour imprévus (souvent 5 à 10 %).</p>
<h4>Le coût de gestion</h4>
<p>Un espace vert coûte surtout <b>après</b> sa création : eau, main-d'œuvre, remplacements, réparations. On l'estime en m² par classe d'entretien (niveau 6) et on le présente avec le devis, pour que le maître d'ouvrage sache s'il pourra l'entretenir.</p>
<div class="astuce"><b>Tableur :</b> le classeur <code>devis_estimatif.xlsx</code> du TP contient les formules (Montant = Quantité × PU, sous-totaux, TVA, imprévus). Modifiez les quantités, tout se recalcule.</div>""",
    """<ol>
  <li>À partir de votre plan de masse (niveau 4) et de votre liste de mobilier, établissez le métré.</li>
  <li>Complétez <code>devis_estimatif.xlsx</code> avec vos quantités. Quel est le coût total TTC avec 10 % d'imprévus ?</li>
  <li>Estimez le coût d'eau annuel du projet avec vos calculs du niveau 5 (prix de l'eau fictif : 40 DA/m³).</li>
</ol>"""),
  lecon("v8-l2", "Le plan de gestion d'un espace vert", "25 min",
    ["Connaître le contenu d'un plan de gestion",
     "Rédiger des fiches de gestion par espace",
     "Choisir des indicateurs de suivi"],
    """
<p>Le <b>plan de gestion</b> organise l'entretien d'un espace vert (ou de tous ceux d'une commune) sur plusieurs années. Il sert de feuille de route aux équipes et de base aux cahiers des charges des entreprises.</p>
<h4>Contenu type</h4>
<ol>
  <li><b>Diagnostic</b> : inventaire, état sanitaire, usages, problèmes (niveaux 1 à 3).</li>
  <li><b>Objectifs</b> : par exemple « augmenter la canopée de 20 % à 25 % en 10 ans », « réduire la consommation d'eau de 30 % », « zéro pesticide ».</li>
  <li><b>Classes d'entretien</b> et carte de gestion différenciée (niveau 6).</li>
  <li><b>Fiches de gestion</b> : pour chaque espace, les opérations, leur fréquence, la période et les moyens (agents, matériel).</li>
  <li><b>Programme pluriannuel</b> : plantations, remplacements, rénovations, avec un budget par année.</li>
  <li><b>Indicateurs de suivi</b> : nombre d'arbres plantés et morts, taux de canopée, m³ d'eau consommés, m²/hab, satisfaction des usagers.</li>
</ol>
<h4>Exemple de fiche de gestion</h4>
<div class="tab-wrap"><table class="tab"><thead><tr><th>Opération</th><th>Fréquence</th><th>Période</th></tr></thead><tbody>
<tr><td>Tonte de la pelouse centrale</td><td>2 fois par mois</td><td>Mars à juin, octobre</td></tr>
<tr><td>Fauche de la prairie</td><td>2 fois par an</td><td>Juin et octobre</td></tr>
<tr><td>Contrôle de l'arrosage</td><td>Chaque semaine</td><td>Mai à septembre</td></tr>
<tr><td>Visite sanitaire des arbres</td><td>1 fois par an</td><td>Hiver</td></tr>
<tr><td>Contrôle de l'aire de jeux</td><td>Visuel chaque semaine, approfondi chaque année</td><td>Toute l'année</td></tr>
</tbody></table></div>""",
    """<ol>
  <li>Rédigez le plan de gestion (4 pages maximum) du square de votre projet avec la structure de la leçon.</li>
  <li>Remplissez une fiche de gestion pour chacune des zones (pelouse, massifs, arbres, jeux).</li>
  <li>Choisissez 5 indicateurs et leur valeur cible à 5 ans.</li>
</ol>"""),
  lecon("v8-l3", "Associer les habitants et évaluer le projet", "25 min",
    ["Organiser la participation des habitants",
     "Préparer et analyser une enquête auprès des usagers",
     "Présenter un projet de façon claire"],
    """
<p>Un espace vert conçu <b>avec</b> les habitants est mieux respecté et mieux utilisé. La participation peut intervenir à chaque étape.</p>
<h4>Formes de participation</h4>
<ul>
  <li><b>Avant le projet</b> : questionnaire, réunion de quartier, balade diagnostic avec les habitants, ateliers avec les enfants de l'école voisine.</li>
  <li><b>Pendant</b> : présentation des esquisses, choix entre deux variantes, journée de plantation collective.</li>
  <li><b>Après</b> : jardins partagés, parrainage d'arbres par des familles ou des classes, comités d'usagers, signalement des problèmes.</li>
</ul>
<h4>L'enquête auprès des usagers</h4>
<p>Questions courtes, fermées si possible : fréquence de visite, temps d'accès, activités, satisfaction (de 1 à 5) sur l'ombre, la propreté, la sécurité, les jeux, et une question ouverte « que faudrait-il améliorer ? ». Le fichier <code>enquete_usagers.csv</code> du TP contient 120 réponses fictives à analyser.</p>
<h4>Présenter le projet</h4>
<p>Pour un jury ou un conseil communal : une affiche ou un diaporama avec le diagnostic (cartes), le plan de masse, deux ou trois vues d'ambiance, la palette végétale, le devis et le plan de gestion. Un message clair : « ce que le projet apporte au quartier ».</p>
<div class="astuce"><b>À retenir :</b> l'évaluation boucle le projet. Les indicateurs (canopée, m²/hab, eau, satisfaction) mesurés avant et après montrent si les objectifs sont atteints et nourrissent le projet suivant.</div>""",
    """<ol>
  <li>Analysez <code>enquete_usagers.csv</code> dans un tableur : note moyenne de chaque critère, part des usagers venant à pied, trois améliorations les plus demandées.</li>
  <li>Proposez trois actions de participation pour votre projet de square.</li>
  <li>Projet final : présentez votre square (diagnostic, plan de masse, palette, irrigation, devis, plan de gestion) en 10 diapositives.</li>
</ol>"""),
  ],
  quiz=[
    q("Que contient le métré d'un projet ?", ["Les prix unitaires", "Les quantités mesurées sur le plan", "Le planning d'entretien", "La liste des usagers"], 1, "Le métré mesure les quantités ; le chiffrage les multiplie par les prix unitaires."),
    q("30 arbres à 9 000 DA l'unité coûtent…", ["27 000 DA", "270 000 DA", "2 700 000 DA", "39 000 DA"], 1, "30 × 9 000 = 270 000 DA."),
    q("Pourquoi présenter le coût d'entretien avec le devis de création ?", ["Parce que l'espace vert coûte surtout après sa création", "Ce n'est pas utile", "Pour gonfler le budget", "Parce que la loi interdit l'entretien"], 0, "Eau, main-d'œuvre et remplacements pèsent chaque année."),
    q("Lequel est un indicateur de suivi d'un plan de gestion ?", ["La couleur des bancs", "Le taux de canopée", "Le nom de l'architecte", "La marque des tondeuses"], 1, "Le taux de canopée mesure l'évolution du couvert arboré."),
    q("Quel est un intérêt principal de la participation des habitants ?", ["Un espace mieux utilisé et mieux respecté", "Supprimer l'entretien", "Éviter de faire un diagnostic", "Réduire le nombre d'arbres"], 0, "Les habitants qui ont participé s'approprient l'espace."),
  ])

import json, sys
V = [
("v1","","Comment les villes algériennes développent leurs espaces verts : de la pépinière à l'aménagement (en arabe)","abd-loYpIjs",""),
("v1","v1-l2","Rafraîchir la ville par le végétal sans arrosage","fZuLAWpyk08",""),
("v1","v1-l2","Un îlot de fraîcheur en ville","LFYSX0U4nJA",""),
("v1","v1-l2","L'importance des espaces verts au cœur des villes (en arabe)","lnyi8FhQrDg",""),
("v1","v1-l3","Comment préserver les espaces verts (en arabe)","2ljST3bu-2k",""),
("v2","v2-l2","10 arbustes pour un jardin méditerranéen en plein soleil et sans soif","opiR0i0pdA8",""),
("v2","v2-l2","Les plantes méditerranéennes","0TJQk3vMezU",""),
("v2","v2-l3","Nommer une plante grâce à l'application Pl@ntNet","aEas5HiKf4o",""),
("v2","v2-l3","Identifier une plante avec Pl@ntNet sur le web","KlgxPDwkpXE",""),
("v3","v3-l1","Participer à un inventaire diagnostic des arbres","PZ448q42yvo","Avec une technicienne de l'arbre de Silvavenir."),
("v3","v3-l3","Reconnaître un arbre mort","qNAXnHKXeVA",""),
("v4","v4-l2","Aménager son jardin en 8 étapes","AxEp6UBA6dk",""),
("v4","v4-l2","Créer un plan de son jardin en 3 points","5mWEvhKjgDM",""),
("v5","v5-l2","Comment planter et tuteurer un arbre","cMy2OkL5jEE",""),
("v5","v5-l2","Planter un arbre : les bons gestes","zaxx6ivwN4s",""),
("v5","v5-l2","Plantation et tuteurage d'un arbre en racines nues","KmDnEPBOAOk",""),
("v5","v5-l2","La bonne méthode pour planter n'importe quel arbre (en arabe)","pflHShN_Z-4",""),
("v5","v5-l3","Installer un arrosage goutte-à-goutte","VyyCLfpSOec",""),
("v5","v5-l3","Avantages et inconvénients du goutte-à-goutte","FPqf5OXrJOg",""),
("v6","v6-l1","C'est quoi la gestion différenciée des espaces verts ?","apO9885OV2k",""),
("v6","v6-l1","Gestion différenciée des espaces verts","F4SI_0-uwYM",""),
("v6","v6-l2","Comment bien couper une branche ?","Nx63yelhBqg",""),
("v6","v6-l2","Les bases de la taille correcte des arbres (en arabe)","BgY5LHRSk4Y",""),
("v6","v6-l3","L'écopiège contre la processionnaire : quand le poser et comment l'entretenir","zqlRrumEOrM","Chaîne YouTube : Polleniz."),
("v6","v6-l3","Monter et poser un écopiège contre la chenille processionnaire du pin","vuO8r_mAZ34",""),
("v7","v7-l2","La Minute QGIS : comment créer une zone tampon ?","pSKH5sEb95c",""),
("v7","v7-l2","QGIS : créer une zone tampon (buffer)","vdIcjcnf39g",""),
("v7","v7-l3","QGIS : importer un fichier CSV","AsNhCy2ztUg",""),
("v7","v7-l3","Charger des images Sentinel-2 dans QGIS et calculer le NDVI","-T2oPZi07zw",""),
("v7","v7-l3","Calculer l'indice de végétation NDVI (exercice pratique)","e6buBRkL_60",""),
]
out=[dict(niveau=n,lecon=l,titre=t,url="https://www.youtube.com/watch?v="+i,duree="",description=d) for n,l,t,i,d in V]
h="""/*
 * VIDÉOS TUTORIELLES — parcours Espaces verts
 * Vidéos YouTube en français ou en arabe uniquement (trouvées par recherche le 22/11/2026, à visionner avant le cours).
 * Ajoutez des vidéos depuis la page « Administration » du site, puis remplacez ce fichier
 * par le videos.js téléchargé, ou copiez un bloc { ... } à la main.
 * Champs : niveau ("v1"…"v8"), lecon (ex. "v3-l2" ou "" pour tout le niveau), titre,
 *          url (YouTube ou videos/fichier.mp4), duree, description ("Chaîne YouTube : Nom." alimente la page Remerciements).
 */
window.VIDEOS = """
open(sys.argv[1],"w",encoding="utf-8").write(h+json.dumps(out,ensure_ascii=False,indent=2)+";\n")
print(len(out))

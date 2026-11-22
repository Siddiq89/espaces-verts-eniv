import json, os, sys
SITE=sys.argv[1]
def t(p):
    s=os.path.getsize(os.path.join(SITE,p)); return f"{s/1024:.0f} Ko".replace(".",",") if s<1024*1024 else f"{s/1048576:.1f} Mo".replace(".",",")
F=[("","","fichiers/TP_EV_ENIV.zip","Toutes les données du TP (dossier TP_EV)","Décompressez dans C:\\ENIV\\ : couches SIG (GeoJSON et shapefile) et tableaux (CSV, Excel)."),
("","","fichiers/shapefiles_ev.zip","Toutes les couches au format shapefile","Pour ArcGIS ou les anciens logiciels (UTM 30N, encodage UTF-8)."),
("v1","v1-l1","fichiers/espaces_verts.geojson","Espaces verts de la ville fictive","14 espaces verts avec leur catégorie (loi n° 07-06) et leur surface."),
("v1","v1-l2","fichiers/quartiers_population.csv","Population et espaces verts par quartier","Pour calculer les m² d'espaces verts par habitant."),
("v2","v2-l2","fichiers/palette_vegetale.csv","Palette végétale pour Tlemcen","19 espèces : strate, noms français et arabe, besoin en eau, rusticité, remarques."),
("v3","v3-l1","fichiers/inventaire_arbres.csv","Inventaire des arbres (297 arbres)","Espèce, coordonnées X/Y (UTM 30N), circonférence, hauteur, couronne, état, défaut, action."),
("v3","v3-l1","fichiers/fiche_inventaire_arbre.csv","Fiche d'inventaire vide","Modèle pour inventorier les arbres de votre établissement."),
("v4","v4-l1","fichiers/site_projet.zip","Site de projet (1,2 ha), courbes de niveau et réseaux","Pour l'analyse du site et le plan de masse."),
("v5","v5-l3","fichiers/et0_tlemcen.csv","Évapotranspiration et pluie mensuelles","Valeurs indicatives pour le calcul des besoins en eau."),
("v5","v5-l3","fichiers/calcul_irrigation.xlsx","Modèle de calcul des besoins en eau","Zones, KL, efficience : les besoins mensuels se recalculent."),
("v7","v7-l1","fichiers/quartiers.geojson","Quartiers de la ville fictive","8 quartiers avec leur population."),
("v7","v7-l2","fichiers/accessibilite.zip","Couches pour l'analyse d'accessibilité","Habitat (habitants), terrains libres, espaces verts, quartiers."),
("v8","v8-l1","fichiers/devis_estimatif.xlsx","Modèle de devis estimatif","Prix fictifs, formules de montants, imprévus et TVA."),
("v8","v8-l3","fichiers/enquete_usagers.csv","Enquête auprès des usagers (120 réponses)","Fréquentation, mode d'accès, notes de satisfaction, améliorations demandées.")]
out=[dict(niveau=a,lecon=b,fichier=c,titre=d,taille=t(c),description=e) for a,b,c,d,e in F]
h="""/*
 * FICHIERS D'EXEMPLE À TÉLÉCHARGER — parcours Espaces verts
 * Pour ajouter un fichier : copiez-le dans fichiers/ puis ajoutez un bloc { ... } ci-dessous.
 * Champs : niveau ("v1"…"v8" ou "" pour un fichier général), lecon (ex. "v3-l2" ou ""),
 *          fichier (chemin depuis le dossier du site), titre, taille, description.
 */
window.FICHIERS = """
open(os.path.join(SITE,"donnees/fichiers.js"),"w",encoding="utf-8").write(h+json.dumps(out,ensure_ascii=False,indent=2)+";\n")

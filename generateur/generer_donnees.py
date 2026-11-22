"""Génère les données FICTIVES du TP Espaces verts ENIV (ville fictive près de Tlemcen, UTM 30N EPSG:32630).
Usage : python generer_donnees.py DOSSIER_SORTIE   (nécessite pyshp et openpyxl)"""
import json, math, os, random, sys, csv, zipfile
import shapefile
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill
R = random.Random(2026)
OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
X0, Y0 = 652000, 3858000
PRJ = 'PROJCS["WGS_1984_UTM_Zone_30N",GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",500000.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",-3.0],PARAMETER["Scale_Factor",0.9996],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]]'

def aire(p):
    return abs(sum(p[i][0]*p[i+1][1]-p[i+1][0]*p[i][1] for i in range(len(p)-1)))/2
def rect(x, y, w, h, ang=0, jit=0):
    c = [(-w/2,-h/2),(w/2,-h/2),(w/2,h/2),(-w/2,h/2)]
    a = math.radians(ang); pts=[]
    for dx, dy in c:
        dx += R.uniform(-jit, jit); dy += R.uniform(-jit, jit)
        pts.append((round(x+dx*math.cos(a)-dy*math.sin(a),1), round(y+dx*math.sin(a)+dy*math.cos(a),1)))
    return pts+[pts[0]]
def dedans(pt, poly):
    x, y = pt; ins = False
    for i in range(len(poly)-1):
        (x1,y1),(x2,y2) = poly[i], poly[i+1]
        if (y1>y)!=(y2>y) and x < (x2-x1)*(y-y1)/(y2-y1)+x1: ins = not ins
    return ins
def ecrire_geojson(nom, feats, geom):
    fc = {"type":"FeatureCollection","name":nom,"crs":{"type":"name","properties":{"name":"urn:ogc:def:crs:EPSG::32630"}},"features":[]}
    for props, g in feats:
        if geom=="Polygon": gg={"type":"Polygon","coordinates":[[list(p) for p in g]]}
        elif geom=="LineString": gg={"type":"LineString","coordinates":[list(p) for p in g]}
        else: gg={"type":"Point","coordinates":list(g)}
        fc["features"].append({"type":"Feature","properties":props,"geometry":gg})
    json.dump(fc, open(os.path.join(OUT,"donnees",nom+".geojson"),"w",encoding="utf-8"), ensure_ascii=False)
    # shapefile équivalent
    shp = os.path.join(OUT,"donnees","shapefiles",nom)
    w = shapefile.Writer(shp, shapeType={"Polygon":shapefile.POLYGON,"LineString":shapefile.POLYLINE,"Point":shapefile.POINT}[geom], encoding="utf-8")
    keys = list(feats[0][0].keys())
    for k in keys:
        v = feats[0][0][k]
        if isinstance(v, float): w.field(k[:10],"N",18,2)
        elif isinstance(v, int): w.field(k[:10],"N",12,0)
        else: w.field(k[:10],"C",120)
    for props, g in feats:
        if geom=="Polygon": w.poly([list(reversed(g))] if aire_signee(g)>0 else [g])
        elif geom=="LineString": w.line([g])
        else: w.point(*g)
        w.record(*[props[k] for k in keys])
    w.close(); open(shp+".prj","w").write(PRJ); open(shp+".cpg","w").write("UTF-8")
def aire_signee(p): return sum(p[i][0]*p[i+1][1]-p[i+1][0]*p[i][1] for i in range(len(p)-1))/2

os.makedirs(os.path.join(OUT,"donnees","shapefiles"), exist_ok=True)
os.makedirs(os.path.join(OUT,"tables"), exist_ok=True)

# ---------------- Quartiers (grille 4 x 2 de 1 x 2 km) ----------------
NOMS_Q = ["Hay Ezzitoun","Cité des Pins","Hay El Ward","Hay Ennour","Les Jardins","Hay Essalam","Cité Universitaire","Hay El Feth"]
quartiers=[]
for i,nom in enumerate(NOMS_Q):
    c, r = i%4, i//4
    x, y = X0+c*1000, Y0+r*2000
    poly=[(x,y),(x+1000,y),(x+1000,y+2000),(x,y+2000),(x,y)]
    quartiers.append(dict(code=f"Q{i+1}", nom=nom, poly=poly))

# ---------------- Espaces verts ----------------
# (quartier, nom, catégorie, cx, cy (relatifs), largeur, hauteur, angle)
EV_DEF = [
 (0,"Parc des Oliviers","Parc urbain",500,1300,260,200,8),
 (0,"Square Ezzitoun","Jardin public",300,500,90,70,0),
 (1,"Jardin de la Cité des Pins","Jardin collectif ou résidentiel",500,900,110,80,12),
 (1,"Square des Écoles","Jardin public",700,1600,60,50,0),
 (2,"Jardin botanique municipal","Jardin spécialisé",500,1000,180,150,-5),
 (2,"Boulevard des Micocouliers","Alignement boisé",500,400,700,10,0),
 (3,"Bois de l'Oued","Forêt urbaine",600,1100,300,420,20),
 (4,"Square des Roses","Jardin public",400,1500,80,60,0),
 (4,"Jardin des Jardins","Jardin collectif ou résidentiel",650,600,70,60,5),
 (5,"Placette Essalam","Jardin public",500,1000,50,45,0),
 (6,"Parc universitaire","Parc urbain",500,1000,220,180,-10),
 (6,"Allée des Frênes","Alignement boisé",500,300,10,800,0),
 (7,"Square El Feth","Jardin public",300,1400,70,55,0),
 (7,"Coteau d'El Feth","Forêt urbaine",650,500,200,250,15),
]
ev=[]
for k,(qi,nom,cat,cx,cy,w,h,a) in enumerate(EV_DEF):
    q=quartiers[qi]; x0,y0=q["poly"][0]
    poly=rect(x0+cx,y0+cy,w,h,a,jit=min(w,h)*0.06)
    ev.append(dict(id=f"EV{k+1:02d}", nom=nom, categorie=cat, quartier=q["nom"], poly=poly, surface=round(aire(poly))))
ecrire_geojson("espaces_verts",[({"id":e["id"],"nom":e["nom"],"categorie":e["categorie"],"quartier":e["quartier"],"surface_m2":float(e["surface"])},e["poly"]) for e in ev],"Polygon")

# ---------------- Habitat (points) ----------------
DENS = [70,110,90,40,120,130,60,85]  # nb de points par quartier
hab=[]; pop={q["nom"]:0 for q in quartiers}
for qi,q in enumerate(quartiers):
    x0,y0=q["poly"][0]; n=0
    while n<DENS[qi]:
        p=(round(x0+R.uniform(30,970),1), round(y0+R.uniform(30,1970),1))
        if any(dedans(p,e["poly"]) for e in ev): continue
        hb=R.randint(20,80); hab.append(({"id":f"H{len(hab)+1:04d}","quartier":q["nom"],"habitants":hb},p)); pop[q["nom"]]+=hb; n+=1
ecrire_geojson("batiments_habitat",hab,"Point")
for q in quartiers:
    q["population"]=pop[q["nom"]]; q["surface_ev"]=sum(e["surface"] for e in ev if e["quartier"]==q["nom"])
ecrire_geojson("quartiers",[({"code":q["code"],"nom":q["nom"],"population":q["population"],"surface_ha":200.0},q["poly"]) for q in quartiers],"Polygon")
with open(os.path.join(OUT,"tables","quartiers_population.csv"),"w",newline="",encoding="utf-8") as f:
    wr=csv.writer(f); wr.writerow(["code","quartier","population","surface_quartier_ha","surface_ev_m2"])
    for q in quartiers: wr.writerow([q["code"],q["nom"],q["population"],200,q["surface_ev"]])

# ---------------- Terrains libres ----------------
TL=[(3,300,1600,120,90),(5,250,400,100,80),(5,750,1600,90,90),(1,250,300,80,70)]
ecrire_geojson("terrains_libres",[({"id":f"TL{i+1}","quartier":quartiers[qi]["nom"],"surface_m2":float(round(aire(rect(quartiers[qi]["poly"][0][0]+cx,quartiers[qi]["poly"][0][1]+cy,w,h))))},rect(quartiers[qi]["poly"][0][0]+cx,quartiers[qi]["poly"][0][1]+cy,w,h)) for i,(qi,cx,cy,w,h) in enumerate(TL)],"Polygon")

# ---------------- Site de projet (1,2 ha), courbes, réseaux ----------------
sx,sy=X0+1000+250,Y0+2000+1400   # dans Hay Essalam ? (quartier 6 = Hay Essalam col1,row1)
site=[(sx,sy),(sx+120,sy),(sx+120,sy+100),(sx,sy+100),(sx,sy)]
ecrire_geojson("site_projet",[({"nom":"Site de projet - square Essalam","surface_m2":float(aire(site))},site)],"Polygon")
courbes=[]
for k,alt in enumerate(range(812,818)):
    yy=sy-5+k*22
    courbes.append(({"altitude":alt},[(sx-20+j*20, round(yy+6*math.sin(j/2),1)) for j in range(9)]))
ecrire_geojson("courbes_site",courbes,"LineString")
ecrire_geojson("reseaux",[({"type":"Conduite d'eau potable","profondeur_m":1.2},[(sx-20,sy+30),(sx+140,sy+30)]),
  ({"type":"Ligne électrique aérienne","profondeur_m":0.0},[(sx+90,sy-20),(sx+90,sy+120)]),
  ({"type":"Assainissement","profondeur_m":2.0},[(sx-20,sy+95),(sx+140,sy+95)])],"LineString")

# ---------------- Inventaire des arbres ----------------
ESP = [("Celtis australis","Micocoulier",22),("Pinus halepensis","Pin d'Alep",17),("Fraxinus angustifolia","Frêne oxyphylle",11),
 ("Olea europaea","Olivier",10),("Quercus ilex","Chêne vert",7),("Ceratonia siliqua","Caroubier",6),("Platanus x hispanica","Platane",6),
 ("Melia azedarach","Mélia",5),("Cupressus sempervirens","Cyprès de Provence",5),("Washingtonia robusta","Palmier de Californie",4),
 ("Jacaranda mimosifolia","Jacaranda",3),("Ailanthus altissima","Ailante",4)]
def tirer():
    t=R.uniform(0,sum(e[2] for e in ESP))
    for e in ESP:
        t-=e[2]
        if t<=0: return e
    return ESP[-1]
arbres=[]; n=0
CIBLE={"Parc urbain":"Forte","Jardin public":"Forte","Jardin collectif ou résidentiel":"Moyenne","Jardin spécialisé":"Moyenne","Alignement boisé":"Forte","Forêt urbaine":"Faible"}
NB={"Parc urbain":30,"Jardin public":9,"Jardin collectif ou résidentiel":10,"Jardin spécialisé":20,"Alignement boisé":0,"Forêt urbaine":14}
for e in ev:
    pts=[]
    if e["categorie"]=="Alignement boisé":
        (ax,ay),(bx,by)=e["poly"][0],e["poly"][2]
        long_=max(abs(bx-ax),abs(by-ay)); m=int(long_//12)
        for j in range(m):
            t=(j+0.5)/m; pts.append((round(ax+(bx-ax)*t,1),round(ay+(by-ay)*t,1)))
    else:
        xs=[p[0] for p in e["poly"]]; ys=[p[1] for p in e["poly"]]
        while len(pts)<NB[e["categorie"]]:
            p=(round(R.uniform(min(xs),max(xs)),1),round(R.uniform(min(ys),max(ys)),1))
            if dedans(p,e["poly"]): pts.append(p)
    for p in pts:
        if e["nom"]=="Boulevard des Micocouliers": sp=ESP[0]
        elif e["nom"]=="Allée des Frênes": sp=ESP[2]
        elif e["categorie"]=="Forêt urbaine": sp=R.choice([ESP[1],ESP[1],ESP[4],ESP[5],ESP[1]])
        else: sp=tirer()
        n+=1
        stade=R.choices(["Jeune","Adulte","Mature","Sénescent"],[25,45,22,8])[0]
        base={"Jeune":(25,60),"Adulte":(70,160),"Mature":(160,260),"Sénescent":(180,320)}[stade]
        circ=R.randint(*base); d=circ/math.pi/100
        haut=round(min(25, 1.5+ d*22*R.uniform(0.8,1.2)),1)
        if sp[0].startswith("Washingtonia"): haut=round(R.uniform(6,18),1)
        cour=round(max(1.0, d*14*R.uniform(0.8,1.2)),1)
        defauts=["Aucun"]*10+["Branche morte"]*4+["Cavité"]*2+["Fourche écorce incluse"]*2+["Blessure au collet"]*2+["Champignon au pied"]+["Inclinaison"]
        df=R.choice(defauts)
        if sp[0]=="Pinus halepensis" and R.random()<0.35: df="Nids processionnaire"
        if stade=="Sénescent" and R.random()<0.5: df=R.choice(["Cavité","Champignon au pied","Branche morte"])
        etat={"Aucun":"Bon","Branche morte":"Moyen","Nids processionnaire":"Moyen","Blessure au collet":"Moyen","Inclinaison":"Moyen",
              "Fourche écorce incluse":R.choice(["Moyen","Mauvais"]),"Cavité":R.choice(["Moyen","Mauvais"]),"Champignon au pied":"Mauvais"}[df]
        if stade=="Sénescent" and R.random()<0.25: etat="Mort"; df="Arbre mort"
        action={"Bon":"Surveillance","Moyen":"Taille d'entretien","Mauvais":"Expertise et mise en sécurité","Mort":"Abattage et replantation"}[etat]
        if df=="Nids processionnaire": action="Échenillage"
        if df=="Fourche écorce incluse" and etat=="Moyen": action="Taille de formation ou haubanage"
        if sp[0]=="Ailanthus altissima": action="Élimination (espèce envahissante)"
        cible=CIBLE[e["categorie"]]
        arbres.append([f"ARB-{n:04d}",sp[0],sp[1],p[0],p[1],circ,haut,cour,stade,etat,df,cible,action,e["id"],e["nom"],e["quartier"]])
CH=["id","espece","nom_commun","x","y","circonference_cm","hauteur_m","couronne_m","stade","etat","defaut","cible","action","id_espace","espace","quartier"]
with open(os.path.join(OUT,"tables","inventaire_arbres.csv"),"w",newline="",encoding="utf-8") as f:
    wr=csv.writer(f); wr.writerow(CH); wr.writerows(arbres)
with open(os.path.join(OUT,"tables","fiche_inventaire_arbre.csv"),"w",newline="",encoding="utf-8") as f:
    wr=csv.writer(f); wr.writerow(CH)

# ---------------- Palette végétale ----------------
PAL=[("Arbre","Pinus halepensis","Pin d'Alep","الصنوبر الحلبي","Persistant",15,"Faible","Très bonne","Local ; surveiller la processionnaire"),
("Arbre","Celtis australis","Micocoulier","الميس","Caduc",15,"Faible à moyen","Très bonne","Arbre d'alignement, ombre dense"),
("Arbre","Fraxinus angustifolia","Frêne oxyphylle","الدردار","Caduc",18,"Moyen","Très bonne","Local ; sols frais, berges"),
("Arbre","Olea europaea","Olivier","الزيتون","Persistant",8,"Très faible","Bonne","Très sobre ; pollen allergisant"),
("Arbre","Quercus ilex","Chêne vert","البلوط الأخضر","Persistant",12,"Faible","Très bonne","Local, longévif"),
("Arbre","Ceratonia siliqua","Caroubier","الخروب","Persistant",10,"Très faible","Moyenne","Sensible aux fortes gelées"),
("Arbre","Cupressus sempervirens","Cyprès de Provence","السرو","Persistant",20,"Faible","Très bonne","Brise-vent ; pollen allergisant"),
("Arbre","Melia azedarach","Mélia","الزنزلخت","Caduc",10,"Faible","Bonne","Fruits toxiques, éviter près des jeux"),
("Arbre","Jacaranda mimosifolia","Jacaranda","الجاكرندا","Semi-persistant",10,"Moyen","Faible","Gélif : éviter les zones froides"),
("Arbuste","Pistacia lentiscus","Lentisque","الضرو","Persistant",3,"Très faible","Bonne","Local, haies libres"),
("Arbuste","Myrtus communis","Myrte","الريحان","Persistant",2.5,"Faible","Moyenne","Local, parfumé"),
("Arbuste","Nerium oleander","Laurier-rose","الدفلى","Persistant",3,"Faible","Moyenne","Toxique : jamais près des aires de jeux"),
("Arbuste","Rhamnus alaternus","Alaterne","السفير","Persistant",4,"Très faible","Bonne","Local, haies brise-vent"),
("Arbuste","Lavandula dentata","Lavande dentée","الخزامى","Persistant",0.8,"Très faible","Moyenne","Mellifère"),
("Couvre-sol","Rosmarinus officinalis 'Prostratus'","Romarin rampant","إكليل الجبل الزاحف","Persistant",0.3,"Très faible","Bonne","Mellifère, talus"),
("Couvre-sol","Lantana montevidensis","Lantana rampant","لانتانا زاحفة","Persistant",0.4,"Faible","Faible","Gélif en hiver froid"),
("Grimpante","Bougainvillea glabra","Bougainvillier","الجهنمية","Persistant",6,"Faible","Faible","Mur abrité au sud"),
("Gazon","Cynodon dactylon","Chiendent pied-de-poule (gazon)","النجيل","Caduc l'hiver",0.05,"Moyen","Bonne","Gazon résistant au piétinement"),
("À éviter","Ailanthus altissima","Ailante","شجرة السماء","Caduc",20,"Faible","Très bonne","ENVAHISSANTE : ne pas planter")]
with open(os.path.join(OUT,"tables","palette_vegetale.csv"),"w",newline="",encoding="utf-8") as f:
    wr=csv.writer(f); wr.writerow(["strate","espece","nom_fr","nom_ar","feuillage","hauteur_adulte_m","besoin_eau","rusticite_froid","remarques"]); wr.writerows(PAL)

# ---------------- ET0 mensuelle (indicative, fictive) ----------------
ET0=[("janvier",1.5,70),("février",2.0,65),("mars",3.0,60),("avril",3.8,50),("mai",4.8,30),("juin",5.8,8),("juillet",6.2,2),("août",5.8,4),("septembre",4.5,20),("octobre",3.2,45),("novembre",2.0,65),("décembre",1.4,70)]
JOURS=[31,28,31,30,31,30,31,31,30,31,30,31]
with open(os.path.join(OUT,"tables","et0_tlemcen.csv"),"w",newline="",encoding="utf-8") as f:
    wr=csv.writer(f); wr.writerow(["mois","jours","et0_mm_jour","pluie_mm_mois"])
    for (m,e,p),j in zip(ET0,JOURS): wr.writerow([m,j,e,p])

# ---------------- Classeur irrigation ----------------
B=Font(bold=True); F=PatternFill("solid",fgColor="DCEFE2")
wb=Workbook(); ws=wb.active; ws.title="Zones"
ws.append(["Calcul des besoins en eau d'un espace vert (données fictives ENIV, cellules vertes à modifier)"]); ws["A1"].font=B
ws.append([]); ws.append(["Zone","Surface (m²)","KL","Efficience"]); 
for c in "ABCD": ws[c+"3"].font=B
for z in [("Gazon",800,0.8,0.7),("Massifs méditerranéens",800,0.3,0.9),("Arbres (cuvettes)",400,0.4,0.9)]:
    ws.append(list(z))
for r in range(4,7):
    for c in "BCD": ws[f"{c}{r}"].fill=F
ws2=wb.create_sheet("Besoins mensuels")
ws2.append(["Mois","Jours","ET0 (mm/j)","Pluie (mm/mois)","Pluie utile (mm/mois) = 0,7 × pluie"]+[f"Besoin {z} (m³/mois)" for z in ["zone 1","zone 2","zone 3"]]+["Total (m³/mois)"])
for c in "ABCDEFGHI": ws2[c+"1"].font=B
for i,((m,e,p),j) in enumerate(zip(ET0,JOURS)):
    r=i+2
    row=[m,j,e,p,f"=0.7*D{r}"]
    for k,zr in enumerate([4,5,6]):
        row.append(f"=MAX(0,(C{r}*B{r}*Zones!C{zr}-E{r})*Zones!B{zr}/Zones!D{zr}/1000)")
    row.append(f"=F{r}+G{r}+H{r}")
    ws2.append(row)
ws2.append(["Total annuel","","","","",'=SUM(F2:F13)','=SUM(G2:G13)','=SUM(H2:H13)','=SUM(I2:I13)'])
for c in "ABCDEFGHI": ws2[c+"14"].font=B
for c,wd in zip("ABCDEFGHI",[12,8,10,14,22,20,20,20,16]): ws2.column_dimensions[c].width=wd
ws.column_dimensions["A"].width=28
wb.save(os.path.join(OUT,"tables","calcul_irrigation.xlsx"))

# ---------------- Devis estimatif ----------------
wb=Workbook(); ws=wb.active; ws.title="Devis"
ws.append(["Devis estimatif - square de quartier (PRIX FICTIFS pour l'exercice, en DA)"]); ws["A1"].font=B
ws.append([]); ws.append(["N°","Désignation","Unité","Quantité","Prix unitaire (DA)","Montant (DA)"])
for c in "ABCDEF": ws[c+"3"].font=B
L=[("Terrassement et apport de terre végétale","m³",300,2500),("Fourniture et plantation d'arbres (circ. 12-14 cm)","u",30,9000),
("Fourniture et plantation d'arbustes","u",400,600),("Couvre-sols et vivaces","u",600,250),("Engazonnement","m²",500,450),
("Paillage (broyat de bois)","m²",900,300),("Réseau goutte-à-goutte","ml",900,350),("Allées en stabilisé","m²",1400,1800),
("Bancs","u",20,35000),("Corbeilles","u",10,12000),("Aire de jeux 2-12 ans (équipements + sol amortissant)","forfait",1,2500000),
("Point d'eau potable","u",1,150000),("Éclairage des allées","u",12,90000)]
for i,(d,u,qte,pu) in enumerate(L):
    r=i+4; ws.append([i+1,d,u,qte,pu,f"=D{r}*E{r}"]); ws[f"D{r}"].fill=F; ws[f"E{r}"].fill=F
r=4+len(L)
ws.append(["","Total hors taxes","","","",f"=SUM(F4:F{r-1})"])
ws.append(["","Imprévus (taux en E)","","",0.10,f"=F{r}*E{r+1}"])
ws.append(["","TVA (taux en E)","","",0.19,f"=(F{r}+F{r+1})*E{r+2}"])
ws.append(["","Total TTC","","","",f"=F{r}+F{r+1}+F{r+2}"])
for k in range(4): ws[f"B{r+k}"].font=B; ws[f"F{r+k}"].font=B
ws[f"E{r+1}"].fill=F; ws[f"E{r+2}"].fill=F
for c,wd in zip("ABCDEF",[5,55,9,10,18,18]): ws.column_dimensions[c].width=wd
wb.save(os.path.join(OUT,"tables","devis_estimatif.xlsx"))

# ---------------- Enquête usagers ----------------
AMEL=["Plus d'ombre","Plus de bancs","Toilettes","Propreté","Jeux pour les grands","Éclairage le soir","Point d'eau potable","Moins de bruit"]
with open(os.path.join(OUT,"tables","enquete_usagers.csv"),"w",newline="",encoding="utf-8") as f:
    wr=csv.writer(f); wr.writerow(["id","age","sexe","frequence","mode_acces","temps_acces_min","note_ombre","note_proprete","note_securite","note_jeux","note_globale","amelioration"])
    for i in range(120):
        acc=R.choices(["À pied","Voiture","Bus","Vélo"],[70,18,10,2])[0]
        wr.writerow([i+1,R.choice(["moins de 18","18-30","31-50","51-65","plus de 65"]),R.choice(["F","M"]),R.choices(["Tous les jours","Chaque semaine","Chaque mois","Rarement"],[25,40,20,15])[0],
          acc,R.randint(2,12) if acc=="À pied" else R.randint(5,30),R.choices([1,2,3,4,5],[25,30,25,15,5])[0],R.choices([1,2,3,4,5],[10,20,35,25,10])[0],
          R.choices([1,2,3,4,5],[5,15,35,30,15])[0],R.choices([1,2,3,4,5],[15,25,30,20,10])[0],R.choices([1,2,3,4,5],[5,20,40,28,7])[0],
          R.choices(AMEL,[30,18,12,14,8,10,6,2])[0]])

print("quartiers", [(q["nom"],q["population"],q["surface_ev"],round(q["surface_ev"]/q["population"],1)) for q in quartiers])
print("arbres", len(arbres), "habitat", len(hab))

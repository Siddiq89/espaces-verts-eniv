import json, re, sys
sys.path.insert(0,'.')
from fr_1_4 import N1,N2,N3,N4
from fr_5_8 import N5,N6,N7,N8
from en_ev import EN
from ar_ev import AR
from ber_ev import BER
NIV=[N1,N2,N3,N4,N5,N6,N7,N8]
from melange import melanger_trad
melanger_trad(EN,NIV); melanger_trad(AR,NIV)
OUT=sys.argv[1]; err=0
for lang,D in (("en",EN),("ar",AR)):
    for n in NIV:
        t=D.get(n['id'])
        if not t: print(lang,"niveau manquant",n['id']); err+=1; continue
        if len(t['quiz'])!=len(n['quiz']): print(lang,n['id'],"quiz count"); err+=1
        for tq,fq in zip(t['quiz'],n['quiz']):
            if len(tq['choix'])!=len(fq['choix']): print(lang,n['id'],"choix",tq['question']); err+=1
        for l in n['lecons']:
            tl=D.get(l['id'])
            if not tl: print(lang,"leçon manquante",l['id']); err+=1; continue
            nb=len(re.findall(r'<pre>',l['contenu']))
            used=sorted(int(x) for x in re.findall(r'<!--code:(\d+)-->',tl['contenu']))
            if used!=list(range(nb)): print(lang,l['id'],"codes",used,"attendu",nb); err+=1
            if len(tl['objectifs'])!=len(l['objectifs']): print(lang,l['id'],"objectifs"); err+=1
    head=f"/* Traduction {lang} du parcours Espaces verts (générée par generateur/gen_trad.py). Les blocs de code restent ceux de la version française (<!--code:N-->). */\n"
    open(f"{OUT}/{lang}.js","w",encoding="utf-8").write(head+"window.TRAD = window.TRAD || {};\nwindow.TRAD.%s = Object.assign(window.TRAD.%s || {}, %s);\n" % (lang,lang,json.dumps(D,ensure_ascii=False,indent=1)))
open(f"{OUT}/ber.js","w",encoding="utf-8").write("/* Tamaziɣt (asekkil alatin) : nom du parcours et titres des niveaux. Les leçons restent en français. Traduction à faire relire par un locuteur. */\nwindow.TRAD = window.TRAD || {};\nwindow.TRAD.ber = Object.assign(window.TRAD.ber || {}, %s);\n" % json.dumps(BER,ensure_ascii=False,indent=1))
print("erreurs:",err)

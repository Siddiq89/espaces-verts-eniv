import json, sys
sys.path.insert(0, '.')
from fr_1_4 import N1, N2, N3, N4
from fr_5_8 import N5, N6, N7, N8
NIV = [N1, N2, N3, N4, N5, N6, N7, N8]
from melange import melanger_fr
melanger_fr(NIV)
cours = dict(cle="ev", nom="Espaces verts", court="le TP", logiciel="Espaces verts", recherche="espaces verts",
  titre="Espaces verts urbains : concevoir, planter, gérer",
  accroche="Les espaces verts, de l'arbre au projet urbain",
  lead="Un parcours progressif pour comprendre, concevoir et gérer les espaces verts de la ville : typologie et services rendus, palette végétale adaptée au climat de Tlemcen, inventaire et diagnostic des arbres, conception d'un square, plantation et irrigation économe, entretien et gestion différenciée, cartographie avec QGIS, devis et plan de gestion. Chaque leçon propose un exercice pratique, des vidéos et un quiz de fin de niveau.",
  niveaux=NIV)
entete = """/*
 * CONTENU PÉDAGOGIQUE : parcours Espaces verts — Espaces verts ENIV, enseignant : BOUHAFSI SIDDIQ
 * ------------------------------------------------------------------
 * Niveaux, leçons, exercices et quiz. Texte en HTML simple.
 * Dans un quiz, "bonne" est le numéro de la bonne réponse en comptant à partir de 0.
 * Pour les VIDÉOS, utilisez donnees/videos.js (ou la page Administration du site).
 * Fichier généré par generateur/gen_cours.py : modifiez de préférence les fichiers fr_*.py,
 * ou modifiez directement ce fichier si vous n'utilisez pas Python.
 */
"""
open(sys.argv[1], 'w', encoding='utf-8').write(entete + "window.COURS = " + json.dumps(cours, ensure_ascii=False, indent=1) + ";\n")
print(sum(len(n['lecons']) for n in NIV), "leçons", sum(len(n['quiz']) for n in NIV), "questions")

# scripts/rename_files.py
import os

dossier = input("Entrez le chemin du dossier : ")
for i, fichier in enumerate(os.listdir(dossier), 1):
    ancien = os.path.join(dossier, fichier)
    nouveau = os.path.join(dossier, f"fichier_{i}{os.path.splitext(fichier)[1]}")
    os.rename(ancien, nouveau)
print("Renommage terminé !")
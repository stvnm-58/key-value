#!/usr/bin/python3

import redis

print("--- Connexion à Redis ---")
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

print("\n--- Écriture des 6 utilisateurs ---")
# On enregistre tes 5 valeurs avec des clés structurées
r.set("user:1", "Antho")
r.set("user:2", "Ryan")
r.set("user:3", "Anil")
r.set("user:4", "Marie")
r.set("user:5", "Steven")
r.set("user:6", "Maxence")
print("[OK] Les 6 prénoms ont été stockés dans Redis.")

print("\n--- Lecture et Affichage ---")
# On fait une boucle de 1 à 5 pour aller chercher les données
for i in range(1, 6):
    prenom = r.get(f"user:{i}")
    print(f"ID {i} dans Redis -> {prenom}")

print("\n--- Fin du script ---")
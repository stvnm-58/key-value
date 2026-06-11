#!/usr/bin/python3

import redis

# Connexion
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

# Récupération directe de l'ID 1
prenom_1 = r.get("user:1")
prenom_2 = r.get("user:2")
prenom_3 = r.get("user:3")
prenom_4 = r.get("user:4")
prenom_5 = r.get("user:5")

print(prenom_1, prenom_2, prenom_3, prenom_4, prenom_5)

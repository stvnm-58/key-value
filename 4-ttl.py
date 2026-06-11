#!/usr/bin/python3

import redis

# Connexion
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

# Création du user:6 avec une expiration (ex) de 60 secondes
r.set("user:6", "Maxence", ex=60)

print("Le user:6 a été créé avec un TTL de 30 secondes.")

# On vérifie immédiatement le temps restant
temps_restant = r.ttl("user:6")
print(f"Temps restant pour user:6 : {temps_restant} secondes.")
#!/usr/bin/python3

import redis

# Connexion
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

prenom_6 = r.get("user:6")
temps_restant = r.ttl("user:6")

print(prenom_6)
print(f"Temps restant pour user:6 : {temps_restant} secondes.")
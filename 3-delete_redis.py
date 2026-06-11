#!/usr/bin/python3

import redis

# Connexion
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

# Suppression directe des deux clés
r.delete("user:2")
r.delete("user:4")

print("ID 2 et ID 4 ont été supprimés.")
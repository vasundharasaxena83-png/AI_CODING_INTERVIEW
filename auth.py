import json
import os

FILE = "users.json"

def load():
    if not os.path.exists(FILE):
        return {}
    return json.load(open(FILE))

def save(data):
    json.dump(data, open(FILE, "w"))

def signup(u, p):
    users = load()
    if u in users:
        return False, "User exists"
    users[u] = p
    save(users)
    return True, "Created"

def login(u, p):
    users = load()
    if u not in users:
        return False, "Account not found"
    if users[u] != p:
        return False, "Wrong password"
    return True, "Success"
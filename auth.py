users = {
    "admin": {"password": "admin123", "role": "ADMIN"},
    "pharmacist": {"password": "pharma123", "role": "PHARMACIST"}
}

def login(username, password):
    if username in users and users[username]["password"] == password:
        return users[username]["role"]
    else:
        return None

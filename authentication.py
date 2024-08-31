
from flask import request, jsonify

def auth(user,password):
    user_name = "Genaro"
    user_password = "Genaro123"
    return user == user_name and password == user_password

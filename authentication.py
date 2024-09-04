
from flask import request, jsonify
from wsgi import app

def authentication(user,password):
    user_name = "Genaro"
    user_password = "Genaro123"
    return user == user_name and password == user_password

@app.route('/input/{my_target_field}', methods = ['POST'])
def input_data(my_target_field):
    auth = request.authorization # Extrae la auth desde la solicitud

    if not auth or not authentication(auth.user, auth.password):
        return jsonify({
            'Message': 'Authentication required'
        }), 401 # not authorized
    
    if not request.json or my_target_field not in request.json:
        return jsonify({
            'Error' : 'Invalid input'
        }), 400 # mas apropiado para una bad req 
    
    value = request.json[my_target_field]
    return jsonify({
        'Message' : "received <my_target_field> : {value}"
    }), 200
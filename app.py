
# * Info importante resaltada
# ! Peligro
# ? Cuestionamiento, utilizar o no?
# TODO : Cosas para hacer eventualmente.

# * Importaciones
from flask import Flask
from authentication import input_data

# TODO from markupsafe import escape

app = Flask(__name__)
@app.route("/")
def mainApp():
    return "<p>Ejercicio BackEND RD</p>"

if __name__ == '__main__':
    app.run(debug=True)

# Detalles a tener en cuenta de la preparacion.

# * Info importante resaltada
# ! Peligro
# ? Cuestionamiento, utilizar o no?
# TODO : Cosas para hacer eventualmente.

from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# Detalles a tener en cuenta de la preparacion.

# * Info importante resaltada
# ! Peligro
# ? Cuestionamiento, utilizar o no?
# TODO : Cosas para hacer eventualmente.

# * Importaciones
from flask import Flask
from authentication import input_data

# TODO from markupsafe import escape

# * App
app = Flask(__name__)
@app.route("/")
def mainApp():
    return f"<p>Ejercicio BackEND RD</p>"
if __name__ == '__main__':
    app.run(debug = True)


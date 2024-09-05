from flask import Flask

app = Flask(__name__)
@app.route("/")
def mainApp():
    return "<p>Ejercicio BackEND RD</p>"

if __name__ == '__main__':
    app.run(debug=True)
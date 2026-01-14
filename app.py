from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/curso")
def curso():
    return render_template("curso.html")

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

@app.route("/terminos")
def terminos():
    return render_template("terminos.html")

@app.route("/privacidad")
def privacidad():
    return render_template("privacidad.html")

@app.route("/reembolsos")
def reembolsos():
    return render_template("reembolsos.html")

if __name__ == "__main__":
    app.run(debug=True)

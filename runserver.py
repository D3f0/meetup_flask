# encoding: utf-8


from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    context = {
        'title': u"Mi primer página",
        'content': u'Soy otra cosa',
    }
    return render_template("base.html", **context)

@app.route("/saludar/<nombre>/")
def saludar(nombre):
    return "Hola {0}".format(nombre)

app.run(debug=True)
from flask import Flask
from db import ManipulaBanco
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


def retornalhtml(jason):
    html = ''
    try:
        for k in jason:
            for y in jason[k]:
                for c in y:
                    html = html +  str(c) + ' : ' + str(y[c]) + '  '
                html = html + '<br>'
        return html
    except ValueError:
        return "Vazio"

@app.route('/getcities')
def getcities():

    mani = ManipulaBanco()
    jason = mani.getcities()
    obj = json.loads(jason)
    try:
        return retornalhtml(obj)
    except ValueError:
        return "erro"


@app.route('/createtable')
def createtable():
    mani = ManipulaBanco()
    try:
        mani.createbase()
        return "Tabelas criadas"
    except ValueError:
        return "erro"

@app.route('/filltable')
def filltable():

    mani = ManipulaBanco()
    try:
        jason = mani.insertcities()
        return "Preenchido"
    except ValueError:
        return "Erro no preenchimento"

@app.route('/insertcity/<city>')
def insertcity(city):
    mani = ManipulaBanco()
    try:
        mani.insertcity(city)
        return "Dado inserido"
    except ValueError:
        return "erro"

@app.route('/getcity/<id>')
def getcity(id):
    mani = ManipulaBanco()
    try:
        jason = mani.getcity(id)
        obj = json.loads(jason)
        return retornalhtml(obj)
    except ValueError:
        return "erro"

if __name__ == '__main__':
    app.run()


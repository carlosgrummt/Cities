from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import json
import os

basedir = os.path.abspath(os.path.dirname(__file__))
nomebanco = 'banco.db'
Base = declarative_base()

class Cities(Base):
    __tablename__ = 'cities'
    id              = Column(Integer, primary_key = True)
    cityname        = Column(String(80))

db = create_engine('sqlite:///' + os.path.join(basedir, nomebanco))
db.echo = False
db.connect()

Session = sessionmaker(bind=db)
session = Session()

class ManipulaBanco():
    def createbase(self):
        Base.metadata.create_all(db)

    #def clearbase(self):

    def insertcities(self):
        city = Cities()
        city.cityname = "Curitiba"
        session.add(city)

        city = Cities()
        city.cityname = "Itaguai"
        session.add(city)

        city = Cities()
        city.cityname = "Rio de Janeiro"
        session.add(city)

        city = Cities()
        city.cityname = "São Paulo"
        session.add(city)

        session.commit()


    def getcities(self):
        upd = session.query(Cities).filter_by().all()
        listadicionarios = {}
        lista = []
        for i in upd:
            listadicionarios = {}
            for ii in i.__dict__:
                if ii[0] != '_':
                    listadicionarios[ii] = i.__dict__[ii]
            lista.append(listadicionarios)

        resultado = {"Cities": lista}
        return json.dumps(resultado, indent=4)

    def getcity(self, id):
        upd = session.query(Cities).filter_by(id=id).first()
        listadicionarios = {}
        lista = []
        listadicionarios = {}
        for ii in upd.__dict__:
            if ii[0] != '_':
                listadicionarios[ii] = upd.__dict__[ii]
        lista.append(listadicionarios)

        resultado = {"Cities": lista}
        return json.dumps(resultado, indent=4)

    def insertcity(self,name):
        city = Cities()
        city.cityname = name
        session.add(city)
        session.commit()

#mani = ManipulaBanco()
#mani.insertcity('Ribeirão Preto')
#print(mani.getcities())
#mani.insertcities()
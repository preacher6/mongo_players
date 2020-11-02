from pymongo import MongoClient

class Jugadores():
    """Clase para crear jugadores"""
    def __init__(self, nombre, apellidos, edad, demarcacion, internacional):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.demarcacion = demarcacion
        self.internacional = internacional

    def to_mongo_collection(self):
        """Convertir a formato JSON"""
        return {"nombre": self.nombre,
                "apellidos": self.apellidos,
                "edad": self.edad,
                "demarcación": self.demarcacion,
                "internacional": self.internacional}

    
futbolistas = [
    Jugadores('Iker', 'Casillas', 33, ['Portero'], True),
    Jugadores('Carles','Puyol',36,['Central', 'Lateral'],True),
    Jugadores('Sergio','Ramos',28,['Lateral','Central'],True),
    Jugadores('Andrés','Iniesta',30,['Centrocampista','Delantero'],True),
    Jugadores('Fernando','Torres',30,['Delantero'],True),
    Jugadores('Leo','Baptistao',22,['Delantero'],False)
]
    
client = MongoClient('localhost')
database = client.Futbol
colleccion = database.Futbolistas

"""for futbolista in futbolistas:
    colleccion.insert(futbolista.to_mongo_collection())"""


for collect in colleccion.find({"demarcación":{"$in": ['Delantero']}, "edad":30}):
    print(collect["apellidos"])

#colleccion.update({"edad":{"$gt":30}}, {"$inc":{"edad": 50}}, upsert=False, multi=True)

colleccion.remove({"internacional":False})


for collect in colleccion.find():
    print('el jugador %s tiene %s años'%(collect['nombre'], collect['edad']))

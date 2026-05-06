from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modelo import Jugador
from config import enlace

engine = create_engine(enlace)

Session = sessionmaker(bind=engine)
session = Session()

# se crea un objetos
#
jugadores = [
    {
        "nombre": "Kylian Mbappé", "seleccion": "Francia", "posicion": "Delantero",
        "edad": 27, "goles": 5, "titular": True},
    {
        "nombre": "Vinicius Jr", "seleccion": "Brasil", "posicion": "Extremo",
        "edad": 25, "goles": 3, "titular": True },
    {
        "nombre": "Moisés Caicedo", "seleccion": "Ecuador", "posicion": "Mediocampista",
        "edad": 24, "goles": 1, "titular": True
    },
    {
        "nombre": "Jude Bellingham", "seleccion": "Inglaterra", "posicion": "Mediocampista",
        "edad": 23, "goles": 2, "titular": True
    },
    {
        "nombre": "Lautaro Martínez", "seleccion": "Argentina", "posicion": "Delantero",
        "edad": 28, "goles": 4, "titular": False
    }
]

for d in jugadores:
    j = Jugador(nombre = d["nombre"], seleccion = d['seleccion'], posicion = d["posicion"],
        edad = d["edad"], goles = d["goles"], titular = d["titular"])
    session.add(j)

# se confirma las transacciones
session.commit()

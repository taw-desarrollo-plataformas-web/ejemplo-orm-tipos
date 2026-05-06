"""
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from modelo import Jugador
from config import enlace

engine = create_engine(enlace)

Session = sessionmaker(bind=engine)
session = Session()

registros = session.query(Jugador).all()

for s in registros:
    print(s)

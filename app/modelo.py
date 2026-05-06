from sqlalchemy import create_engine
from config import enlace
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean

engine = create_engine(enlace)

Base = declarative_base()

class Jugador(Base):
    __tablename__ = "jugadores"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    seleccion = Column(String(50), nullable=False)
    posicion = Column(String(30), nullable=False)
    edad = Column(Integer, nullable=False)
    goles = Column(Integer, default=0)
    titular = Column(Boolean, default=True)

    def __repr__(self):
        return f"Jugador: {self.nombre}. Seleccción: {self.seleccion}. Posición: {self.posicion}"

Base.metadata.create_all(engine)

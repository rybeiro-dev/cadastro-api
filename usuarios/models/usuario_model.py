from sqlalchemy import Column, Integer, String

from databases.connection import Base


class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100))
    email = Column(String(255))

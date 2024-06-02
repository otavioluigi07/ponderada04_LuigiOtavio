from sqlalchemy import Column, Integer, String

from database import Base

class User(Base):
    __tablename__ = "Usuarios"

    id: int = Column(Integer, primary_key=True, index=True)
    nome: str = Column(String(100), nullable=False)
    idade: int = Column(Integer, nullable=False)
    sexo: str = Column(String(255), nullable=False)

from sqlalchemy import Column, Integer, String

from database import Base

class Historia(Base):
    __tablename__ = "historias"

    id: int = Column(Integer, primary_key=True, index=True)
    titulo: str = Column(String(100), nullable=False)
    descricao: str = Column(String(255), nullable=False)
    categoria: str = Column(String(255), nullable=False)

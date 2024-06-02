import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../../")

from models.historiaModel import Historia
from repositories.historiasRepositories import HistoriaRepositoy
from database import Base

# Configuração do banco de dados de teste
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Criação das tabelas no banco de dados de teste
Base.metadata.create_all(bind=engine)

# Fixture para a sessão do banco de dados
@pytest.fixture
def db():
    session = TestingSessionLocal()
    Base.metadata.create_all(bind=engine)  # Certifique-se de que as tabelas estão criadas
    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(bind=engine)  # Limpe o banco de dados após os testes

# Testes unitários para o repositório
def test_create_historia(db):
    historia_data = {"titulo": "Teste", "descricao": "Descrição de teste", "categoria": "Categoria de teste"}
    historia = Historia(**historia_data)
    saved_historia = HistoriaRepositoy.save(db, historia)
    
    assert saved_historia.id is not None
    assert saved_historia.titulo == "Teste"
    assert saved_historia.descricao == "Descrição de teste"
    assert saved_historia.categoria == "Categoria de teste"

def test_find_all(db):
    historia_data = {"titulo": "Teste", "descricao": "Descrição de teste", "categoria": "Categoria de teste"}
    historia = Historia(**historia_data)
    HistoriaRepositoy.save(db, historia)
    
    historias = HistoriaRepositoy.find_all(db)
    assert len(historias) > 0

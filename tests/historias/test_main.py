import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../../")

from main import app  # Certifique-se de importar seu aplicativo FastAPI
from database import Base, get_db

# Configuração do banco de dados de teste
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Criação das tabelas no banco de dados de teste
Base.metadata.create_all(bind=engine)

# Dependência de substituição
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

# Testes integrados para a API
def test_create_historia():
    response = client.post(
        "/api/historias",
        json={"titulo": "Teste", "descricao": "Descrição de teste", "categoria": "Categoria de teste"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["id"] is not None
    assert data["titulo"] == "Teste"
    assert data["descricao"] == "Descrição de teste"
    assert data["categoria"] == "Categoria de teste"

def test_find_all_historias():
    response = client.get("/api/historias")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

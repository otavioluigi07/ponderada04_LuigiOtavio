# tests/usuarios/test_user_integration.py
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base
from models.userModel import User
from repositories.userRepositories import UserRepository
import pytest

# Definição da engine de banco de dados
engine = create_engine('sqlite:///test.db')

@pytest.fixture(scope="module")
def session():
    Base.metadata.create_all(bind=engine)  # Aqui também é necessário usar a engine definida acima
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

def setup_module(module):
    Base.metadata.create_all(bind=engine)

def teardown_module(module):
    Base.metadata.drop_all(bind=engine)

class TestUserRepositoryIntegration:
    def test_create_user(self, session: Session):
        user = User(nome="Alice", idade=25, sexo="M")
        UserRepository.save(session, user)
        assert user.id is not None

    def test_get_user_by_name(self, session: Session):
        user = User(nome="Alice", idade=25, sexo="M")
        UserRepository.save(session, user)
        retrieved_user = UserRepository.find_by_name(session, "Alice")
        assert retrieved_user == user

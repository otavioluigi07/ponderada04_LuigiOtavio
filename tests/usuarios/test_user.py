# tests/usuarios/test_user.py
from models.userModel import User
from pydantic import ValidationError

class TestUser:
    def test_user_repr(self):
        user = User(nome="Alice", idade=25, sexo="M")
        assert repr(user) == "User(nome='Alice', idade=25, sexo='M')"

    def test_user_equality(self):
        user1 = User(nome="Alice", idade=25, sexo="M")
        user2 = User(nome="Alice", idade=25, sexo="M")
        assert user1 == user2

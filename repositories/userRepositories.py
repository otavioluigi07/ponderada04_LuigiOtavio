from sqlalchemy.orm import Session
from models.userModel import User

class UserRepository:
    @staticmethod
    def find_all(db: Session) -> list[User]:
        return db.query(User).all()

    @staticmethod
    def save(db: Session, user: User) -> User:  
        if user.id:  
            db.merge(user)
        else:
            db.add(user)
        db.commit()
        return user

    @staticmethod
    def find_by_id(db: Session, id: int) -> User:
        return db.query(User).filter(User.id == id).first()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(User).filter(User.id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        user = db.query(User).filter(User.id == id).first()  # Renomeando a variável User para user
        if user is not None:
            db.delete(user)
            db.commit()

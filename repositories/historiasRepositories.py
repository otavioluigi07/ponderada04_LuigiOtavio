from sqlalchemy.orm import Session

from models.historiaModel import Historia

class HistoriaRepositoy:
    @staticmethod
    def find_all(db: Session) -> list[Historia]:
        return db.query(Historia).all()

    @staticmethod
    def save(db: Session, historia: Historia) -> Historia:
        # historia.descricao = enhance_description(historia.descricao)
        if historia.id:
            db.merge(historia)
        else:
            db.add(historia)
        db.commit()
        return historia

    @staticmethod
    def find_by_id(db: Session, id: int) -> Historia:
        return db.query(Historia).filter(Historia.id == id).first()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(Historia).filter(Historia.id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        historia = db.query(Historia).filter(Historia.id == id).first()
        if historia is not None:
            db.delete(historia)
            db.commit()
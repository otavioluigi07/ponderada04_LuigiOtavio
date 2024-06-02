from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from models.historiaModel import Historia
from models.userModel import User
from database import engine, Base, get_db
from repositories.historiasRepositories import HistoriaRepositoy
from repositories.userRepositories import UserRepository
from schemas.historiaSchema import HistoriaRequest, HistoriaResponse
from schemas.userSchema import UserRequest, UserResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()

#Rotas das histórias
@app.post("/api/historias", response_model=HistoriaResponse, status_code=status.HTTP_201_CREATED)
def create(request: HistoriaRequest, db: Session = Depends(get_db)):
    historia = HistoriaRepositoy.save(db, Historia(**request.dict()))
    return HistoriaResponse.from_orm(historia)

@app.get("/api/historias", response_model=list[HistoriaResponse])
def find_all(db: Session = Depends(get_db)):
    historias = HistoriaRepositoy.find_all(db)
    return [HistoriaResponse.from_orm(historia) for historia in historias]

@app.get("/api/historias/{id}", response_model=HistoriaResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    historia = HistoriaRepositoy.find_by_id(db, id)
    if not historia:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Historia não encontrado"
        )
    return HistoriaResponse.from_orm(historia)

@app.delete("/api/historia/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    if not HistoriaRepositoy.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="História não encontrado"
        )
    HistoriaRepositoy.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/api/historias/{id}", response_model=HistoriaResponse)
def update(id: int, request: HistoriaRequest, db: Session = Depends(get_db)):
    if not HistoriaRepositoy.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="História não encontrado"
        )
    historia = HistoriaRepositoy.save(db, Historia(id=id, **request.dict()))
    return HistoriaResponse.from_orm(historia)

#Rotas dos usuários
@app.post("/api/usuarios", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create(request: UserRequest, db: Session = Depends(get_db)):
    user = UserRepository.save(db, Historia(**request.dict()))
    return UserResponse.from_orm(user)

@app.get("/api/usuarios", response_model=list[UserResponse])
def find_all(db: Session = Depends(get_db)):
    users = UserRepository.find_all(db)
    return [UserResponse.from_orm(user) for user in users]

@app.get("/api/usuario/{id}", response_model=UserResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    user = UserRepository.find_by_id(db, id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Usuario não encontrado"
        )
    return UserResponse.from_orm(user)

@app.delete("/api/usuario/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    if not UserRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Usuario não encontrado"
        )
    UserRepository.delete_by_id(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/api/usuario/{id}", response_model=UserResponse)
def update(id: int, request: UserRequest, db: Session = Depends(get_db)):
    if not UserRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Usuario não encontrado"
        )
    user = UserRepository.save(db, User(id=id, **request.dict()))
    return UserResponse.from_orm(user)

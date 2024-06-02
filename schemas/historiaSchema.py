from pydantic import BaseModel

class HistoriaBase(BaseModel):
    titulo: str
    descricao: str
    categoria: str

class HistoriaRequest(HistoriaBase):
    ...

class HistoriaResponse(HistoriaBase):
    id: int

    class Config:
        orm_mode = True
        from_attributes = True  

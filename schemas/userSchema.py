from pydantic import BaseModel

class UserBase(BaseModel):
    titulo: str
    descricao: str
    categoria: str

class UserRequest(UserBase):
    ...

class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True
        from_attributes = True  

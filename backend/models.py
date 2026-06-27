from pydantic import BaseModel

class Maquina(BaseModel):
    nome: str
    fabricante: str
    modelo: str
    localizacao: str

class Falha(BaseModel):
    maquina: str
    descricao: str
    prioridade: str
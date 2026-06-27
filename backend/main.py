from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="AutoTech AI",
    version="0.1.0"
)

class Maquina(BaseModel):
    nome: str
    fabricante: str
    modelo: str
    localizacao: str

class Falha(BaseModel):
    maquina: str
    descricao: str
    prioridade: str

maquinas = []
falhas = []

@app.get("/")
def inicio():
    return {"mensagem": "Bem-vindo à AutoTech AI!"}

@app.get("/status")
def status():
    return {
        "sistema": "AutoTech AI",
        "status": "Online",
        "versao": "0.1.0"
    }

@app.post("/maquinas")
def cadastrar_maquina(maquina: Maquina):
    maquinas.append(maquina)
    return {
        "mensagem": "Máquina cadastrada com sucesso!",
        "dados": maquina
    }

@app.get("/maquinas")
def listar_maquinas():
    return maquinas

@app.post("/falhas")
def cadastrar_falha(falha: Falha):
    falhas.append(falha)
    return {
        "mensagem": "Falha registrada com sucesso!",
        "dados": falha
    }

@app.get("/falhas")
def listar_falhas():
    return falhas

@app.get("/diagnostico/{problema}")
def diagnostico(problema: str):

    problema = problema.lower()

    if "motor" in problema:
        return {
            "problema": problema,
            "possiveis_causas": [
                "Falta de alimentação",
                "Disjuntor desligado",
                "Contator com defeito",
                "Relé térmico desarmado"
            ]
        }

    elif "sensor" in problema:
        return {
            "problema": problema,
            "possiveis_causas": [
                "Sensor desalinhado",
                "Sensor queimado",
                "Cabo rompido",
                "Fonte 24V desligada"
            ]
        }

    else:
        return {
            "problema": problema,
            "mensagem": "Ainda não conheço esse problema. Em breve aprenderei!"
        }
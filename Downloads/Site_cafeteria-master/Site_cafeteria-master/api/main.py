from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

db = {}
counter = {'id': 1}


class Produto(BaseModel):
    nome: str
    preco: float
    descricao: Optional[str] = ''


@app.get('/health')
def health():
    return {'status': 'ok'}


@app.get('/produtos')
def listar_produtos():
    return [{'id': pid, **dados} for pid, dados in db.items()]


@app.post('/produtos', status_code=201)
def criar_produto(produto: Produto):
    pid = counter['id']
    db[pid] = produto.dict()
    counter['id'] += 1
    return {'id': pid, **db[pid]}


@app.get('/produtos/{pid}')
def ler_produto(pid: int):
    if pid not in db:
        raise HTTPException(status_code=404, detail='Produto nao encontrado')
    return {'id': pid, **db[pid]}


@app.put('/produtos/{pid}')
def atualizar_produto(pid: int, produto: Produto):
    if pid not in db:
        raise HTTPException(status_code=404, detail='Produto nao encontrado')
    db[pid] = produto.dict()
    return {'id': pid, **db[pid]}


@app.delete('/produtos/{pid}')
def deletar_produto(pid: int):
    if pid not in db:
        raise HTTPException(status_code=404, detail='Produto nao encontrado')
    del db[pid]
    return {'mensagem': 'Produto removido'}
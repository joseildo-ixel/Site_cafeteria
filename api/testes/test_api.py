import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_health():
    r = client.get('/health')
    assert r.status_code == 200
    assert r.json()['status'] == 'ok'


def test_criar_produto():
    r = client.post('/produtos', json={'nome': 'Cafe Expresso', 'preco': 5.0})
    assert r.status_code == 201
    assert r.json()['nome'] == 'Cafe Expresso'


def test_ler_produto_existente():
    r = client.post('/produtos', json={'nome': 'Bolo de Chocolate', 'preco': 8.0})
    pid = r.json()['id']
    r2 = client.get(f'/produtos/{pid}')
    assert r2.status_code == 200


def test_ler_produto_inexistente():
    r = client.get('/produtos/9999')
    assert r.status_code == 404


def test_deletar_produto():
    r = client.post('/produtos', json={'nome': 'Suco de Laranja', 'preco': 6.0})
    pid = r.json()['id']
    r2 = client.delete(f'/produtos/{pid}')
    assert r2.status_code == 200

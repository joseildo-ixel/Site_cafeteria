# Aroma & Grao - Cafeteria API

Projeto integrador da disciplina **Gerenciamento de Configuração de Software** do curso de Analise e Desenvolvimento de Sistemas (ADS) - IFPE.

## Equipe

| Nome |
|------|
| Joseildo dos Santos|
| Eliabe Rafael|
| Eduardo Artur|
| Erik Jerônimo|
| Luis Felipe |
| Romero Galindo |
| Algusto |

---

## Descrição do Projeto

Este projeto implementa uma **API REST** para gerenciamento de produtos de uma cafeteria ficticia chamada **Aroma & Grao**, com um pipeline CI/CD completo utilizando **GitHub Actions** e **Docker**.

---

## Tecnologias Utilizadas

- Python 3.10
- FastAPI
- Pytest (com pytest-html)
- Docker
- GitHub Actions
- Docker Hub

---

## Fluxo do Pipeline CI/CD

```mermaid
flowchart LR
    A[Push / Pull Request] --> B[CI - Testes]
    B --> C[Build - Verificar Imagem Docker]
    C --> D[CD - Publicar no Docker Hub]
```

### Descrição dos Jobs

| Job | Gatilho | O que faz |
|-----|---------|-----------|
| CI - Testes | Todo push e pull request | Instala dependencias, executa os testes automatizados e gera relatório de resultados em HTML |
| Build | Apos CI passar | Constroi a imagem Docker localmente para validar o Dockerfile |
| CD | Push na branch master | Publica a imagem no Docker Hub com tags de versão e latest |

---

## Como executar localmente com Docker

### Pre-requisitos

- Docker instalado

### Passos

```bash
# Clone o repositorio
git clone [https://github.com/joseildo-ixel/Site_cafeteria.git](https://github.com/joseildo-ixel/Site_cafeteria.git)
cd Site_cafeteria

# Construa a imagem e suba a aplicacao localmente
docker compose up --build
```

A API ficara disponivel em: `http://localhost:8000`

Documentacao interativa: `http://localhost:8000/docs`

---

## Como executar os testes

```bash
# Instale as dependencias
pip install -r api/requirements.txt
pip install pytest pytest-html

# Execute os testes
python -m pytest api/testes/ -v
```

---

## Endpoints da API

| Metodo | Rota | Descricao |
|--------|------|-----------|
| GET | `/health` | Verificacao de saude da API |
| GET | `/produtos` | Listar todos os produtos |
| POST | `/produtos` | Criar um produto |
| GET | `/produtos/{id}` | Buscar um produto por ID |
| PUT | `/produtos/{id}` | Atualizar um produto |
| DELETE | `/produtos/{id}` | Remover um produto |

---

## Imagem Docker

A imagem e publicada automaticamente no Docker Hub a cada push na branch `master` (ou `main`):

```bash
docker pull joseildosystem/cafeteria-api:latest
```

---

## Evidencias de Execucao

![Pipeline CI/CD](docs/pipeline.png)

*(Nota: Certifique-se de atualizar o arquivo docs/pipeline.png com um print da nova pipeline passando verde no GitHub Actions!)*

---

## Estrategia de Branches (GitFlow)

| Branch | Finalidade |
|--------|-----------|
| `master` | Versao estavel e final |
| `develop` | Integracao das funcionalidades |
| `feature/*` | Novas funcionalidades |
| `release/*` | Preparacao para lancamento |

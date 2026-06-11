# -- Estágio 1: Build (Instalação de dependências) --
FROM python:3.10-slim AS builder

WORKDIR /app
# Cria um ambiente virtual para isolar as dependências
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY api/requirements.txt .
# Instala as dependências dentro do ambiente virtual
RUN pip install --no-cache-dir -r requirements.txt

# -- Estágio 2: Produção (Imagem final enxuta) --
FROM python:3.10-slim

WORKDIR /app

# Copia apenas o ambiente virtual pronto do Estágio 1
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Cria o usuário não-root por segurança
RUN adduser --disabled-password --gecos "" appuser

# Copia o código da aplicação
COPY api/ .

# Define o usuário criado
USER appuser

EXPOSE 8000

# Verifica a saúde da aplicação
HEALTHCHECK --interval=30s --timeout=5s \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1

# Inicia a API com Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
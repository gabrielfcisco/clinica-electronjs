# Use a imagem oficial do Python como base
FROM python:latest

# Variável de ambiente que impede o reload
ENV PYTHONUNBUFFERED=1

# Defina o diretório de trabalho como /app
WORKDIR /app

# Copie o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências do projeto
RUN pip install -r requirements.txt

# Copie o conteúdo do diretório atual para o diretório de trabalho no container
COPY . .


# Exponha a porta 8000
EXPOSE 8000

# Comando padrão para executar quando o contêiner for iniciado
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
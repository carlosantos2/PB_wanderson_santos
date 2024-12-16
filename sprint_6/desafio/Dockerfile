# Usar uma imagem base do Python
FROM python:3.9-slim

# Definir o diretório de trabalho
WORKDIR /app

# Copiar apenas o arquivo de requisitos primeiro para aproveitar o cache do Docker
COPY requeriments.txt .

# Instalar as dependências
RUN pip install --no-cache-dir -r requeriments.txt

# Instalar o AWS CLI
RUN apt-get update && apt-get install -y awscli && apt-get clean

# Copiar a pasta .aws para o diretório home do root no container
COPY .aws /root/.aws

# Copiar todos os arquivos restantes para o diretório de trabalho
COPY . .

# Comando para executar o script
CMD ["python", "ingestao.py"]
    

    #cd ingestao
    #docker build -t data-lake-ingestao1 .
    #docker run --rm -v ${PWD}/dados:/app/dados data-lake-ingestao1


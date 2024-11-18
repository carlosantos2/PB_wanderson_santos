# Use a imagem base do Python
FROM python:3.9-slim

# Defina o diretório de trabalho
WORKDIR /app

# Copie o arquivo hash_generator.py para o diretório de trabalho
COPY mascarar.py .

# Comando para executar o script
CMD ["python", "mascarar.py"]

#docker build -t mascarar-dados .
#docker run -it --name mascarar-dados mascarar-dados

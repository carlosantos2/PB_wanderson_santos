# Use a imagem base do Python
FROM python:3.9-slim

#diretório de trabalho
WORKDIR /app

# Copia o arquivo carguru.py para o diretório de trabalho
COPY carguru.py .

# executa o script
CMD ["python", "carguru.py"]


#docker build -t carguru-image .
#docker run --name carguru-container carguru-image

#5. Etapa 2: Reutilização de Containers
#Sim, é possível reutilizar containers parados. Para reiniciar um container que foi parado, podemos usar o seguinte comando:
#docker start carguru-container
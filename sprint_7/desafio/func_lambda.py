import boto3
import requests
from datetime import datetime
import json

# Configurações fixas
TMDB_API_KEY = "xxxxxxxxxxxxxxx"  # chave da API do TMDB
BUCKET_NAME = "data-lake-desafio-final-parte-2"  #  nome do bucket S3
YEAR = 2022  # Ano para análise
GENRES = {
    "comedy": 35,
    "animation": 16,
}  # Gêneros a serem coletados

# Função para buscar dados da API do TMDB
def fetch_tmdb_data(api_key, endpoint, params):
    url = f"https://api.themoviedb.org/3/{endpoint}"
    params["api_key"] = api_key
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Falha ao buscar dados da API TMDB: {response.status_code}")
        return None

# Função para buscar filmes de um gênero específico
def fetch_movies_by_genre(api_key, genre_id, year, page=1):
    params = {
        "language": "pt-BR",
        "with_genres": genre_id,
        "primary_release_year": year,
        "page": page,
    }
    endpoint = "discover/movie"
    return fetch_tmdb_data(api_key, endpoint, params)

# Função para enviar dados para o S3
def upload_to_s3(data, bucket, prefix):
    s3_key = f"{prefix}.json"
    print(f"Caminho S3: {s3_key}")

    s3 = boto3.client("s3")
    s3.put_object(Body=json.dumps(data), Bucket=bucket, Key=s3_key)
    print(f"Dados carregados para o S3: s3://{bucket}/{s3_key}")

# Função principal do Lambda
def lambda_handler(event, context):
    # Data atual para organizar os arquivos no S3
    current_date = datetime.now().strftime("%Y/%m/%d")

    for genre_name, genre_id in GENRES.items():
        print(f"Coletando dados para o gênero: {genre_name}")
        all_movies = []
        total_pages = float("inf")
        current_page = 1

        # Requisição de dados da API por páginas
        while current_page <= total_pages:
            tmdb_response = fetch_movies_by_genre(TMDB_API_KEY, genre_id, YEAR, current_page)
            if tmdb_response:
                all_movies.extend(tmdb_response["results"])
                total_pages = tmdb_response["total_pages"]
                current_page += 1
            else:
                print(f"Erro ao buscar página {current_page} para o gênero {genre_name}.")
                break

        # Agrupando em lotes de 100 para envio ao S3
        grouped_data = [all_movies[i : i + 100] for i in range(0, len(all_movies), 100)]
        for index, group in enumerate(grouped_data, start=1):
            prefix = f"Raw/TMDB/JSON/{current_date}/{genre_name}_part_{index}"
            upload_to_s3(group, BUCKET_NAME, prefix)

    print("Execução finalizada com sucesso.")

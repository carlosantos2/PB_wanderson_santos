import boto3
import pandas as pd
from datetime import datetime

# Sessão com perfil AWS configurado
session = boto3.Session(profile_name='225989360512_AdministratorAccess')
s3 = session.client('s3')

# Nome do bucket
nome_bucket = 'data-lake-desafio-final-parte-1'

# Criar o bucket (ignora erro se já existir)
try:
    s3.create_bucket(Bucket=nome_bucket)
    print(f"Bucket {nome_bucket} criado com sucesso!")
except s3.exceptions.BucketAlreadyExists:
    print(f"Bucket {nome_bucket} já existe!")
except s3.exceptions.BucketAlreadyOwnedByYou:
    print(f"Bucket {nome_bucket} já pertence a você!")

# Função para fazer upload dos arquivos CSV para o S3
def upload_para_s3(arquivo_local, caminho_no_bucket):
    try:
        s3.upload_file(arquivo_local, nome_bucket, caminho_no_bucket)
        print(f"Arquivo {arquivo_local} enviado para {caminho_no_bucket} com sucesso!")
    except Exception as e:
        print(f"Erro ao fazer upload do arquivo {arquivo_local}: {e}")

# Função principal
def main():
    # Caminhos dos arquivos CSV locais
    arquivo_movies = '/app/dados/movies.csv'
    arquivo_series = '/app/dados/series.csv'

    # Data atual para organização no bucket
    data_atual = datetime.now().strftime('%Y/%m/%d')

    # Verifica se os arquivos existem antes de enviar
    try:
        movies_df = pd.read_csv(arquivo_movies, sep='|')
        print("Movies CSV carregado com sucesso!")
    except Exception as e:
        print(f"Erro ao carregar o arquivo movies.csv: {e}")
        return

    try:
        series_df = pd.read_csv(arquivo_series, sep='|')
        print("Series CSV carregado com sucesso!")
    except Exception as e:
        print(f"Erro ao carregar o arquivo series.csv: {e}")
        return

    # Caminhos para upload no S3
    caminho_movies = f'Raw/Local/CSV/Movies/{data_atual}/movies.csv'
    caminho_series = f'Raw/Local/CSV/Series/{data_atual}/series.csv'

    # Upload dos arquivos
    upload_para_s3(arquivo_movies, caminho_movies)
    upload_para_s3(arquivo_series, caminho_series)

if __name__ == "__main__":
    main()

import pandas as pd
import boto3

session = boto3.Session(profile_name='225989360512_AdministratorAccess') 
s3 = session.client('s3')


# Configuração do S3
nome_do_meu_bucket = "bucket-aws-desafio-estagio-conect"
meu_arquivo_csv =r'C:\Users\wande\Desktop\PB_WANDERSON_SANTOS\sprint_5\desafio\relacao-de-vagas-de-estagio-e-emprego.csv'



# Baixar o arquivo do S3 para análise
s3.download_file(nome_do_meu_bucket, meu_arquivo_csv, meu_arquivo_csv)

# Carregar o arquivo como um DataFrame do Pandas
df = pd.read_csv(meu_arquivo_csv)

# 4.1. Filtro com dois operadores lógicos
# Filtrar vagas com salário inicial > 1000 e carga horária < 30
filtro = df[(df['no_salario_inicio'] > 1000) & (df['carga_horaria'] < 30)]

# 4.2. Funções de agregação
# Agregação 1: Média salarial por tipo de vaga
media_salarial = df.groupby('tipo_vaga')['no_salario_inicio'].mean()

# Agregação 2: Soma do número de candidatos por cidade
candidatos_por_cidade = df.groupby('cidade')['qt_candidatos'].sum()

# 4.3. Função condicional
# Adicionar coluna indicando se o salário inicial é "Alto" ou "Baixo"
media_geral_salario = df['no_salario_inicio'].mean()
df['status_salario'] = df['no_salario_inicio'].apply(
    lambda x: 'Alto' if x > media_geral_salario else 'Baixo'
)

# 4.4. Função de conversão
# Converter salário de R$ para USD (taxa fictícia de 1 USD = 4 BRL)
df['salario_usd'] = df['no_salario_inicio'] / 4.0

# 4.5. Função de data
# Extrair o ano da data de vigência inicial
df['ano_vigencia'] = pd.to_datetime(df['dt_vigencia_inicio'], dayfirst=True).dt.year
# 4.6. Função de string
# Padronizar os nomes das cidades para letras maiúsculas
df['cidade'] = df['cidade'].str.upper()

# Salvar o DataFrame manipulado em um novo arquivo CSV
output_file = "resultado_final.csv"
df.to_csv(output_file, index=False)

# Upload do arquivo manipulado para o mesmo bucket no S3
s3.upload_file(output_file, nome_do_meu_bucket, output_file)

print("Arquivo transformado salvo e enviado para o S3 com sucesso!")


#python arquivo_final.py
import pandas as pd
import boto3

# Configuração do S3 e sessão
session = boto3.Session(profile_name='225989360512_AdministratorAccess')
s3 = session.client('s3')

# Nome do bucket e arquivo CSV
nome_do_meu_bucket = "bucket-aws-desafio-estagio-conect"
meu_arquivo_csv = 'relacao-de-vagas-de-estagio-e-emprego.csv'

# Baixar o arquivo do S3
s3.download_file(nome_do_meu_bucket, meu_arquivo_csv, meu_arquivo_csv)
print("Arquivo baixado com sucesso.")

# Carregar o arquivo como DataFrame do Pandas
df = pd.read_csv(meu_arquivo_csv)

# Verificação inicial
print("Estrutura do DataFrame carregado:")
print(df.info())


# 4.1. Cláusula que filtra dados com dois operadores lógicos
filtro = df[(df['no_salario_inicio'] > 1000) & (df['carga_horaria'] < 30)]

# 4.2. Duas funções de agregação
# 1. Média salarial por tipo de vaga
media_salarial = df.groupby('tipo_vaga')['no_salario_inicio'].mean().round(2)
print("\nMédia salarial por tipo de vaga:")
print(media_salarial)

# 2. Contagem de vagas por cidade
vagas_por_cidade = df['cidade'].value_counts()
print("\nContagem de vagas por cidade:")
print(vagas_por_cidade)

# 4.3. Função condicional
# Adicionar coluna indicando se o salário inicial é "Alto" ou "Baixo"
media_geral_salario = df['no_salario_inicio'].mean()
df['status_salario'] = df['no_salario_inicio'].apply(
    lambda x: 'Alto' if x > media_geral_salario else 'Baixo'
)

# 4.4. Função de conversão
# Converter salário inicial de R$ para USD com taxa fictícia de 1 USD = 5 BRL
df['salario_usd'] = (df['no_salario_inicio'] / 5.0).round(2)

# 4.5. Função de data
# Extrair o ano da data de vigência inicial
df['ano_vigencia'] = pd.to_datetime(df['dt_vigencia_inicio'], dayfirst=True).dt.year

# 4.6. Função de string
# Padronizar a coluna de tipo de vaga para letras maiúsculas
df['tipo_vaga'] = df['tipo_vaga'].str.upper()

# Salvar DataFrame manipulado em um novo arquivo CSV
output_file = "resultado_final.csv"
df.to_csv(output_file, index=False)

# Upload do arquivo manipulado para o S3
print("\nEnviando arquivo transformado para o S3...")
s3.upload_file(output_file, nome_do_meu_bucket, output_file)
print("Arquivo enviado para o S3 com sucesso!")

#python C:\Users\wande\Desktop\PB_WANDERSON_SANTOS\sprint_5\desafio\arquivo_final.py
import boto3
import pandas as pd

# Iniciando a sessão com o perfil especificado
session = boto3.Session(profile_name='225989360512_AdministratorAccess') 
s3 = session.client('s3')

# Nome do bucket e arquivo
nome_do_bucket = 'bucket-aws-desafio-estagio-conect'
nome_do_arquivo = 'relacao-de-vagas-de-estagio-e-emprego.csv'

# Baixando o arquivo do S3
s3.download_file(nome_do_bucket, nome_do_arquivo, nome_do_arquivo)

# Carregando o arquivo CSV em um DataFrame
df = pd.read_csv(nome_do_arquivo)

# 4.1. Filtrando dados usando ao menos dois operadores lógicos
filtro = df[(df['tipo_vaga'] == 'ESTÁGIO REMUNERADO') & (df['no_salario_inicio'] > 1000)]

# Verificando se o filtro retornou dados
if filtro.empty:
    print("Nenhum dado encontrado com os critérios de filtro.")
else:
    # 4.2. Duas funções de agregação
    agregacao = filtro['no_salario_inicio'].mean()  # Média de Salário Inicial
    total_vagas = filtro['no_qtd_vagas'].sum()  

    # 4.3. Função condicional
    filtro['status'] = filtro['qt_candidatos'].apply(lambda x: 'Muitos Candidatos' if x > 10 else 'Poucos Candidatos')

    # 4.4. Função de conversão
    filtro['no_salario_inicio'] = filtro['no_salario_inicio'].astype(float)

    # 4.5. Função de data
    filtro['dt_vigencia_inicio'] = pd.to_datetime(filtro['dt_vigencia_inicio'], dayfirst=True)

    # 4.6. Função de string
    filtro['status'] = filtro['status'].str.upper()

    # Salvando o DataFrame filtrado como CSV
    output_file = 'resultado_vagas.csv'
    filtro.to_csv(output_file, index=False)

    # Enviando o arquivo resultante de volta para o S3
    s3.upload_file(output_file, nome_do_bucket, output_file)
    print(f'\nArquivo {output_file} enviado para o bucket {nome_do_bucket}.')
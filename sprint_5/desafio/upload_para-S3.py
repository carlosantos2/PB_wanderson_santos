import boto3

session = boto3.Session(profile_name='225989360512_AdministratorAccess') 
s3 = session.client('s3')

# Nome do bucket
nome_bucket = 'bucket-aws-desafio-estagio-conect'

# Criar o bucket
s3.create_bucket(Bucket=nome_bucket)

print(f"Bucket {nome_bucket} criado com sucesso!")

# Nome do arquivo local e no bucket
#arquivo = 'relacao-de-vagas-de-estagio-e-emprego.csv'
arquivo =r'C:\Users\wande\Desktop\PB_WANDERSON_SANTOS\sprint_5\desafio\relacao-de-vagas-de-estagio-e-emprego.csv'

# Upload do arquivo
s3.upload_file(arquivo, nome_bucket, arquivo)

print(f"Arquivo {arquivo} enviado para o bucket {nome_bucket} com sucesso!")

#aws configure
#python -m venv venv
#venv\Scripts\activate
#pip install boto3
#python upload_para-S3.py
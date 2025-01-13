import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import functions as F
import datetime

# Inicializar o contexto do Glue
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# 1. Ler o arquivo CSV
input_path = "s3://data-lake-desafio-final-part-01/Raw/Local/CSV/Movies/2024/12/16/movies.csv"
df_movies = spark.read.option("header", "true").option("delimiter", "|").csv(input_path)

# 2. Remover colunas nulas e padronizar os dados
df_cleaned = df_movies.dropna(subset=["genero", "anoLancamento"])

# 3. Filtrar os dados conforme necessário
df_filtered = df_cleaned.filter(
    (F.col("genero").contains("Comedy") | F.col("genero").contains("Animation")) &
    (F.col("anoLancamento") == "2017")
)

# 4. Definir o caminho de saída
data_processing_date = datetime.datetime.now()
year = data_processing_date.strftime("%Y")
month = data_processing_date.strftime("%m")
day = data_processing_date.strftime("%d")

output_path = f"s3://data-lake-desafio-final-part-01/Trusted/CSV/Parquet/{year}/{month}/{day}/"

# 5. Salvar o resultado em formato PARQUET
df_filtered.write.mode("overwrite").parquet(output_path)

# Finalizar o trabalho
job.commit()

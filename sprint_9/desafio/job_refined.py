import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, round

# Obter as opções resolvidas para o job, como o nome do job
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

# Inicializar o SparkContext
sc = SparkContext()

# Inicializar o GlueContext com o SparkContext existente
glueContext = GlueContext(sc)

# Obter a sessão Spark a partir do GlueContext
spark = glueContext.spark_session

# Inicializar o job AWS Glue
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Caminho para leitura dos dados na camada Trusted
trusted_path = "s3://data-lake-desafio-final-part-01/Trusted/TMDB/PARQUET/2025/01/20/"

# Lendo dados da camada Trusted
df_trusted = spark.read.parquet(trusted_path)

# Criar DataFrames dimensionais
dataframes = {
    "dim_tempo": df_trusted.select(col("anoLancamento").alias("idTempo")).distinct(),
    "dim_idioma": df_trusted.select(col("idioma_original").alias("idIdioma")).distinct(),
    "dim_filmes": df_trusted.select(
        col("id").alias("idFilme"),
        col("tituloPrincipal"),
        col("tituloOriginal"),
        col("genero")
    ).distinct(),
    "fact_filmes": df_trusted.select(
        col("id").alias("idFilme"),
        col("anoLancamento").alias("idTempo"),
        col("idioma_original").alias("idIdioma"),
        col("orcamento"),
        col("receita"),
        col("numeroVotos"),
        round(col("notaMedia"), 1).alias("notaMedia"),
        col("popularidade")
    )
}

# Caminho S3 para gravação da camada Refined
refined_path = "s3://data-lake-desafio-final-part-01/Refined/"

# Gravar DataFrames no S3 em formato Parquet com modo "overwrite"
for name, df in dataframes.items():
    df.write.mode("overwrite").parquet(f"{refined_path}{name}.parquet")

# Finalizar o job
job.commit()

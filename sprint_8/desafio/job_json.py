from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType, ArrayType, MapType
from datetime import datetime

# Inicializar o contexto Spark
sc = SparkContext()
spark = SparkSession(sc)

# Configuração para ignorar arquivos corrompidos
spark.conf.set("spark.sql.files.ignoreCorruptFiles", "true")

# Caminho de entrada e saída no S3
input_path = "s3://data-lake-desafio-final-part-01/Raw/TMDB/JSON/2025/01/08/"
data_processamento = datetime.now()
ano, mes, dia = data_processamento.strftime('%Y'), data_processamento.strftime('%m'), data_processamento.strftime('%d')
output_path = f"s3://data-lake-desafio-final-part-01/Trusted/TMDB/PARQUET/{ano}/{mes}/{dia}/"

# Esquema explícito para o JSON
schema = StructType([
    StructField("id", StringType(), True),
    StructField("tituloPincipal", StringType(), True),
    StructField("tituloOriginal", StringType(), True),
    StructField("anoLancamento", StringType(), True),
    StructField("tempoMinutos", StringType(), True),
    StructField("genero", StringType(), True),
    StructField("notaMedia", FloatType(), True),
    StructField("numeroVotos", IntegerType(), True),
    StructField("generoArtista", StringType(), True),
    StructField("personagem", StringType(), True),
    StructField("nomeArtista", ArrayType(StringType()), True),
    StructField("anoNascimento", StringType(), True),
    StructField("anoFalecimento", StringType(), True),
    StructField("profissao", StringType(), True),
    StructField("titulosMaisConhecidos", StringType(), True),
    StructField("orcamento", IntegerType(), True),
    StructField("receita", IntegerType(), True),
    StructField("resumo", StringType(), True),
    StructField("idioma_original", StringType(), True),
    StructField("popularidade", FloatType(), True),
    StructField("produtoras", ArrayType(StringType()), True),
    StructField("paises_de_producao", ArrayType(StringType()), True),
    StructField("generos_tmbd", ArrayType(StringType()), True),
    StructField("avaliacoes", ArrayType(MapType(StringType(), StringType())), True)
])

# Carregar o arquivo JSON
try:
    df = spark.read.schema(schema).option("multiline", "true").json(input_path)
    print(f"Linhas carregadas: {df.count()}")
    df.show(truncate=False)
    df.printSchema()
except Exception as e:
    print(f"Erro ao carregar o arquivo JSON: {e}")
    raise

# Gravar o DataFrame em formato Parquet no S3
try:
    df.write.format("parquet") \
        .mode("overwrite") \
        .partitionBy() \
        .save(output_path)
    print(f"Arquivo salvo com sucesso no caminho: {output_path}")
except Exception as e:
    print(f"Erro ao salvar o arquivo Parquet: {e}")
    raise

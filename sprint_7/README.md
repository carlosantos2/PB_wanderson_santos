# Sprint 7 (AWS - DESAFIO FINAL) - Trilha de Data Engineering

### Introdução

Nesta sétima sprint da trilha de Data Engineering, avançamos no desafio final com foco em ingestão e análise de dados. Exploramos a ingestão de dados utilizando a API TMDB, realizamos atividades práticas com o Apache Spark e experimentamos o AWS Glue para integração e manipulação de dados. Além disso, concluímos o curso de Spark para reforçar nossos conhecimentos.

## Aprendizados

### **Ingestão de Dados com API TMDB**
- **API TMDB**: Aprendemos a realizar chamadas à API do TMDB, capturando dados complementares de filmes e séries. 
- Integração com AWS Lambda para automatizar a ingestão.
- Persistência dos dados no S3, organizando-os em arquivos JSON seguindo boas práticas de estruturação.

### **Apache Spark**
- **Contador de Palavras com Spark**: Criamos um script para realizar contagem de palavras utilizando as capacidades de processamento distribuído do Apache Spark.
- Compreendemos conceitos como RDDs (Resilient Distributed Datasets), DataFrames e ações/transformações no Spark.

### **AWS Glue**
- **AWS Glue Data Catalog**: Exploramos como criar e gerenciar catálogos de dados com o AWS Glue.
- Entendemos como o Glue interage com dados armazenados no S3 e como configurá-lo para integração com outras ferramentas como o Athena.

### **Curso de Spark**
- Curso concluído sobre fundamentos e aplicações do Apache Spark, consolidando habilidades para trabalhar com grandes volumes de dados.

## Desafios

### **Desafio Final**
Dando continuidade ao desafio iniciado na Sprint 6, nesta etapa, focamos na ingestão de dados externos e complementares aos dados de filmes e séries:
- **Ingestão pela API TMDB**:
  - Consumimos dados utilizando AWS Lambda.
  - Persistimos os resultados no S3 em arquivos JSON organizados por dia de processamento.
  - Agrupamos os registros de forma otimizada, com no máximo 100 por arquivo.
- **Análise de Dados**:
  - Identificação de relações entre custo e receita para os 5 melhores e 5 piores filmes dos gêneros comédia e animação.
  - Preparação para futuras análises mais aprofundadas no Data Lake.

- [📁Desafio](../sprint_7/desafio)

## Exercícios

- **Exercício 1: Ingestão pela API TMDB**:
  
- **Exercício 2: Contador de Palavras com Spark**:
  - Desenvolver um script que utiliza o Apache Spark para realizar contagem de palavras.
  - Implementação e execução localmente.

- **Exercício 3: AWS Glue Data Catalog**:
  - Configurar e criar um Data Catalog utilizando o AWS Glue.
  - Exploração das tabelas no catálogo para integração com outras ferramentas.

### Confira os três exercícios abaixo:

[📁Exercicio-1_API_TMBD](../sprint_7/exercicios/README_api_tmdb.md)

[📁Exercicio-2_Spark_Word_Count](../sprint_7/exercicios/exercicio_spark/)

[📁Exercicio-3_AWS_Glue](../sprint_7/exercicios/README_exec_lab-glue.md)

## Conclusão

A Sprint 7 consolidou conhecimentos fundamentais para o desafio final, como ingestão de dados via API, uso de AWS Lambda, Spark e Glue. Essas práticas reforçaram nossa capacidade de lidar com dados em larga escala e de automatizar processos essenciais para um Data Lake. Seguimos bem preparados para as próximas etapas.



# Sprint 8 (AWS - DESAFIO FINAL) - Trilha de Data Engineering

### Introdução

Nesta oitava sprint da trilha de Data Engineering, avançamos no desafio final com foco no processamento de dados e na prática de manipulação de dados em larga escala. Realizamos exercícios que consolidaram conhecimentos de manipulação de listas, geração de datasets em Python e uso do Apache Spark para análises avançadas. Essas práticas complementaram o desafio principal, que envolveu a transformação de dados na camada Trusted do Data Lake usando AWS Glue e Spark.

## Aprendizados

### **Manipulação de Dados em Python**
- **Listas e Arquivos**:
  - Criamos uma lista com 250 inteiros aleatórios, invertendo sua ordem.
  - Organizamos nomes de animais em ordem alfabética e os salvamos em um arquivo CSV.
  - Geramos um dataset de nomes aleatórios utilizando a biblioteca `names`, salvando-o em um arquivo de texto.

### **Análise de Dados com Apache Spark**
- Criamos um DataFrame a partir de um arquivo contendo aproximadamente 10 milhões de nomes.
- Realizamos operações de transformação e filtragem, como:
  - Adicionar colunas de atributos gerados aleatoriamente, como "Escolaridade", "País" e "Ano de Nascimento".
  - Filtrar dados para identificar pessoas de gerações específicas.
  - Executar análises SQL para agrupar e ordenar informações por país e geração.

### **Processamento de Dados na Trusted Zone**
- Desenvolvemos dois jobs no AWS Glue para transformar e organizar os dados provenientes da camada Raw:
  - Processamento de arquivos CSV e JSON com persistência no formato PARQUET.
  - Organização e particionamento dos dados JSON por ano, mês e dia.

### **Documentação e Evidências**
- Documentamos cada etapa do desafio, com logs, prints e explicações claras.
- Consolidamos práticas de organização para facilitar futuras reproduçes do processo.

## Desafios

### **Entrega 3: Processamento Camada Trusted**
- **Job 1: Processamento de arquivos CSV**:
  - Transformação e persistência no S3 no formato PARQUET, sem particionamento.
- **Job 2: Processamento de arquivos JSON**:
  - Aplicação de particionamento por data no S3, seguindo boas práticas de organização.

### Configuração dos Jobs:
- **Worker type:** G 1x.
- **Requested number of workers:** 2.
- **Job timeout:** 60 minutos ou menos.

confira aqui o desafio da sprint 8:

- [📁Desafio](../sprint_8/desafio)


## Exercícios

- **Exercício 1: Manipulação de Dados em Python**:
  - Criação de listas, ordenação de nomes e geração de datasets.
  - Persistência de dados em arquivos CSV e TXT.
  

  ### Etapas:
  1. **Etapa 1**: Em Python, declare e inicialize uma lista contendo 250 inteiros obtidos de forma aleatória. Após, aplicar o método reverse sobre o conteúdo da lista e imprimir o resultado.

    - [📁Código Etapa 1](../sprint_8/exercicios/exec_1/etapa_1.py)

  2. **Etapa 2**: Em Python, declare e inicialize uma lista contendo o nome de 20 animais. Ordene-os em ordem crescente e itere sobre os itens, imprimindo um a um. Armazene o conteúdo da lista em um arquivo de texto, um item em cada linha, no formato CSV.
    - [📁Código Etapa 2](../sprint_8/exercicios/exec_1/etapa_2.py)

    - [📁 arquivo animais.csv gerado](../sprint_8/exercicios/exec_1/animais.csv)

  3. **Etapa 3**: Elaborar um código Python para gerar um dataset de nomes de pessoas.

  OBS: o arquivo nomes_aleatorios.txt gerado está com incluido no .gitignore, para evitar sobrecarga no repositório, devido ao tamanho do arquivo.

    - [📁Código Etapa 3](../sprint_8/exercicios/exec_1/etapa_3.py)

- # **Exercício 2: Análise de Dados com Apache Spark**:
  - Criação e transformação de DataFrames.
  - Uso de comandos SQL para realizar análises avançadas.

  - [📁Exercicio-2_Spark_DataFrames](../sprint_8/exercicios/exec_2)

  - [📁Código Exercício 2](../sprint_8/exercicios/exec_2/exercicio_2.ipynb)




## Certificados 
Nesta sprint não houveram cursos complementares, logo, não foi necessária a comprovação por meio de certificados.



## Conclusão

A Sprint 8 foi essencial para consolidar habilidades práticas em manipulação de dados, processamento com Apache Spark e uso do AWS Glue. Essas atividades complementaram o desafio principal, fortalecendo a compreensão das etapas necessárias para integrar e transformar dados em um ambiente de Data Lake. Seguimos bem preparados para novos desafios e aplicações do que aprendemos.

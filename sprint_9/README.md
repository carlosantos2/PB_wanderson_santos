# Sprint 9 (AWS - DESAFIO FINAL) - Trilha de Data Engineering

### Introdução

Nesta nona sprint da trilha de Data Engineering, avançamos para a etapa 4 do desafio, com foco na criação e modelagem da camada Refined do Data Lake. Este trabalho envolveu a transformação dos dados da camada Trusted em um formato pronto para análise e visualização no Amazon QuickSight. As práticas realizadas consolidaram conhecimentos de modelagem multidimensional, processamento com Apache Spark e uso de AWS Glue, além de aprofundar o domínio sobre particionamento e persistência de dados.

## Aprendizados

### **Modelagem Multidimensional**
- Projetamos um modelo de dados na camada Refined, com base em princípios de modelagem dimensional.
- Criamos tabelas fato e dimensão para organizar os dados de forma eficiente para consultas analíticas.

### **Processamento de Dados com AWS Glue e Spark**
- Desenvolvemos scripts no AWS Glue para transformar os dados da camada Trusted e armazená-los na Refined Zone.
- Garantimos a persistência dos dados no formato PARQUET, otimizando o uso no Amazon Athena e QuickSight.

### **Documentação e Evidências**
- Documentamos todas as etapas do desafio, incluindo:
  - Logs e prints das execuções no Glue.
  - Evidências de dados transformados e armazenados no S3.
  - Desenho do modelo dimensional da camada Refined.

## Desafios

### **Entrega 4: Modelagem e Processamento da Camada Refined**
- **Modelagem de Dados:**
  - Estruturamos os dados em tabelas fato e dimensão.
  - Criamos um modelo que suporta consultas analíticas multidimensionais no Amazon QuickSight.
- **Processamento de Dados:**
  - Implementamos dois jobs no AWS Glue:
    - Job 1: Transformação de dados CSV e armazenamento no formato PARQUET.
    - Job 2: Transformação de dados JSON e particionamento por ano, mês e dia.
- **Configuração dos Jobs:**
  - **Worker type:** G 1x.
  - **Requested number of workers:** 2.
  - **Job timeout:** 60 minutos ou menos.

Confira aqui o desafio da Sprint 9:

- [📁Desafio](../sprint_9/desafio)

## Exercícios

- Nesta sprint, não houve exercícios propostos além do desafio principal.

## Certificados

- Nesta sprint, não foram realizados cursos complementares, portanto, não foi necessária a comprovação por meio de certificados.

## Conclusão

A Sprint 9 foi referente a entreag 4 do desafio de Data Engineering com a criação da camada Refined, consolidando práticas de modelagem de dados, transformação com Spark e organização no AWS Glue. Esse trabalho destacou a importância de planejar cuidadosamente o pipeline de dados, desde a modelagem até a análise final. Estamos prontos para aplicar os conhecimentos adquiridos em projetos reais e desafios futuros.

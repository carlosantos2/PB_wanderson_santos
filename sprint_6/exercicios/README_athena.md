
# Exercicio 2- Athena 

### Instruções para Configuração e Consulta de Banco de Dados

## Passo 1: Na guia *Settings* (Configurações), escolha *Manage* (Gerenciar).
![Imagem do passo 1](../exercicios/configuracao.png)

---

## Etapa 2: Criar um banco de dados
![Imagem da criação do banco de dados](../exercicios/meu_banco.png)

---

## Etapa 3: Criar uma tabela
![Imagem da criação da tabela](../exercicios/tabela_meu_banco.png)

---

## Etapa 4: Teste os dados com a seguinte consulta
Substitua o nome dos campos, banco de dados e tabela pelos nomes que você criou anteriormente:
sql
SELECT nome 
FROM nomedobanco.nomedatabela 
WHERE ano = 1999 
ORDER BY total 
LIMIT 15;

![teste de dados](../exercicios/teste_meu_banco.png)

## Crie uma consulta que lista os 3 nomes mais usados em cada década desde o 1950 até hoje.

![tabela de dados](../exercicios/1950.png)

## resultado

![tabela de dados](../exercicios/resultado_meu_banco.png)
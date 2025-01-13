# Etapa 3: Geração de nomes aleatórios
import names
import os
import time
import random

# Definir semente
random.seed(40)
qtd_nomes_unicos = 3000
qtd_nomes_aleatorios = 10000000

# Gerar nomes únicos
aux = []
for i in range(qtd_nomes_unicos):
    aux.append(names.get_full_name())

print(f"Gerando {qtd_nomes_aleatorios} nomes aleatórios")
dados = []
for i in range(qtd_nomes_aleatorios):
    dados.append(random.choice(aux))

# Salvar nomes em arquivo
with open('nomes_aleatorios.txt', 'w') as f:
    for nome in dados:
        f.write(f"{nome}\n")

print("Arquivo gerado com sucesso!")

# python etapa_3.py
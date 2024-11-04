'''Exercícios Parte 2
Leia o arquivo person.json, faça o parsing e imprima seu conteúdo.

Dica: leia a documentação do pacote json'''
import json

with open ('person.json') as arquivo:
    dados_js = json.load(arquivo)
    
print(dados_js)    
  
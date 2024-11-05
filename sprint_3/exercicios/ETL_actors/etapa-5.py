# etapa-5 A lista dos atores ordenada pelo faturamento bruto total, em ordem decrescente.

with open('actors.csv', 'r') as file:
    resultado = []
    for linha in file:
        palavras = linha.rsplit(',',5)
        resultado.append(palavras[:])

for coluna in resultado [1::]:
    with open ('etapa-5.txt', 'at', encoding='utf-8') as text:
        text.write('Ator: {} | Faturamento Bruto Total: {}\n'.format(coluna[0],coluna[1]).replace('"',''))
    

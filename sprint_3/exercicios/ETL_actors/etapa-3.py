# etapa-3 Apresente o ator/atriz com a maior média de faturamento por filme.

with open('actors.csv', 'r') as file:
    resultado = []
    for linha in file:
        palavras = linha.rsplit(',',5)
        resultado.append(palavras[:])

maiorfaturamento = []
atorfatura = 0
for coluna in resultado[1::]:
    maiorfaturamento.append(float(coluna[3]))
    maximo = max(maiorfaturamento)
    if float(coluna[3]) >= maximo:
        atorfatura = coluna[0]

with open ('etapa-3.txt', 'w', encoding='utf-8') as text:
    text.write('Apresente o ator/atriz com maior média de faturamento por filmes:')
    text.write('\nAtor/atriz com a maior média de faturamento por filme é {} com média: {}.'.format(atorfatura, maximo))


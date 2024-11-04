# etapa-1 Apresente o ator/atriz com maior número de filmes e a respectiva quantidade.

with open('actors.csv', 'r') as file:
    resultado = []
    for linha in file:
        palavras = linha.rsplit(',', 5)
        resultado.append(palavras[:])

numerofilmes = []
for coluna in resultado[1::]:
    numerofilmes.append(coluna[2])
    maior = max(numerofilmes)
    if coluna[2] == maior:
        ator= coluna[0]
print(ator, maior)

with open ('etapa-1.txt', 'w', encoding='utf-8') as text:
    text.write('Apresente o ator/atriz com maior número de filmes e a respectiva quantidade:')
    text.write('\nAtor com mais filmes: {}, quantidade filmes: {}.'.format(ator, maior))
    text.close() 

#etapa-2 Apresente a  média de faturamento bruto por ator.

# Etapa 2: Média de faturamento bruto por ator (coluna Gross)
gross_values = [float(coluna[5]) for coluna in resultado[1:]]
average_gross = sum(gross_values) / len(gross_values)


etapa_2_resultado = f'Média de receita de bilheteria bruta dos principais filmes: {average_gross:.2f}\n'
with open('etapa-2.txt', 'w', encoding='utf-8') as text:
    text.write(etapa_2_resultado)

    
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

# etapa-4 O nome do(s) filme(s) mais frequente(s) e sua respectiva frequência.
from collections import Counter

filme_frequencia = [coluna[4] for coluna in resultado[1:]]
filme_counts = Counter(filme_frequencia)
mais_frequente = filme_counts.most_common()

# Formatar resultados da Etapa 4
etapa_4_resultado = 'O nome dos filmes mais frequentes e sua respectiva frequência:\n'
etapa_4_resultado += "\n".join([f'O filme {filme} aparece {count} vez(es) no dataset.' for filme, count in mais_frequente])
with open('etapa-4.txt', 'w', encoding='utf-8') as text:
    text.write(etapa_4_resultado)

# etapa-5 A lista dos atores ordenada pelo faturamento bruto total, em ordem decrescente.

with open('actors.csv', 'r') as file:
    resultado = []
    for linha in file:
        palavras = linha.rsplit(',',5)
        resultado.append(palavras[:])

for coluna in resultado [1::]:
    with open ('etapa-5.txt', 'at', encoding='utf-8') as text:
        text.write('Ator: {} | Faturamento Bruto Total: {}\n'.format(coluna[0],coluna[1]).replace('"',''))
    
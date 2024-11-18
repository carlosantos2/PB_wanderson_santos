import csv

with open('estudantes.csv', encoding='utf-8') as arquivo:
    arquivos_csv = csv.reader(arquivo)

    for linhas in sorted(arquivos_csv):
        nomes_estudantes = str(linhas[0])
        notas = sorted(map(int, linhas[1:]), reverse=True)[:3]
        media = round(sum(notas) / 3, 2)
        print(f'Nome: {nomes_estudantes} Notas: {notas} Média: {media}')

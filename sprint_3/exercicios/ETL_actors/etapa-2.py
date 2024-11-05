# Etapa 2: Média de faturamento bruto por ator (coluna Gross)
gross_values = [float(coluna[5]) for coluna in resultado[1:]]
average_gross = sum(gross_values) / len(gross_values)


etapa_2_resultado = f'Média de receita de bilheteria bruta dos principais filmes: {average_gross:.2f}\n'
with open('etapa-2.txt', 'w', encoding='utf-8') as text:
    text.write(etapa_2_resultado)

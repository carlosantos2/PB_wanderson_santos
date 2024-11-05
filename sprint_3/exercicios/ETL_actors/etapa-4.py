
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
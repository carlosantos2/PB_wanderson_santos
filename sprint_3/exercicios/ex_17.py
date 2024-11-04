'''Exercícios Parte 2
Escreva uma função que recebe como parâmetro uma lista e retorna 3 listas: a lista recebida dividida em 3 partes iguais. Teste sua implementação com a lista abaixo

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]'''
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def listas_menores(lista, n):
    for i in range(0, len(lista), n):
        yield lista[i:i + n]

listas_divididas = list(listas_menores(lista, 4))

print(*listas_divididas, sep=' ')

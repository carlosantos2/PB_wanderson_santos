'''Exercícios Parte 2
Escreva uma função que recebe uma string de números separados por vírgula e retorne a soma de todos eles. Depois imprima a soma dos valores.
A string deve ter valor  "1,3,4,6,10,76"'''
def soma(l):
    sum = 0
    for i in l:
        sum += int(i)
    return sum

a = "1,3,4,6,10,76"

b = a.split(",")
c = soma(b)
print(c)


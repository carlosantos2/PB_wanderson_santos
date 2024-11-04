'''Exercícios Parte 1
Escreva um código Python para imprimir os números pares de 0 até 20 (incluso).

Importante: Aplique a função range() em seu código.'''

func_rang = range(21)
for r in func_rang:
    if r % 2 ==0:
        print(r)
'''Exercícios Parte 2
Escreva uma função que recebe um número variável de parâmetros não nomeados e um número variado de parâmetros nomeados e imprime o valor de cada parâmetro recebido.
Teste sua função com os seguintes parâmetros:
(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)'''

def func(*args, **kwargs):
    for i in args:
        print(i)
    
    for v in kwargs.values():
        print(v)

func(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)

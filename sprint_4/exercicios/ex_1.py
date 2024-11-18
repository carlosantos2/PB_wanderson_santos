with open('number.txt', 'r') as f:
    numeros = list(map(int, f.readlines()))  

pares = sorted(filter(lambda x: x % 2 == 0, numeros), reverse=True)
cinco_maiores = pares[:5]
soma = sum(cinco_maiores)

print( cinco_maiores)
print( soma)

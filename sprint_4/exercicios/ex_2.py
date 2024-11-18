
def conta_vogais(s):
    vogais = {'a', 'e', 'i', 'o', 'u'}
    return len(list(filter(lambda x: x.lower() in vogais, s)))

from functools import reduce

def calcula_saldo(lancamentos):
    saldo = reduce(
        lambda acc, valor: acc + valor,
        map(lambda x: x[0] if x[1] == 'C' else -x[0], lancamentos),
        0
    )
    return saldo

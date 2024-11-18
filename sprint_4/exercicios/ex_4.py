def calcular_valor_maximo(operadores, operandos):
    
    operacoes = list(zip(operadores, operandos))
    
    valores_finais = map(lambda op: eval(str(op[1][0]) + op[0] + str(op[1][1])), operacoes)
    
    return max(valores_finais)
operadores = ['+','-','*','/','+']
operandos  = [(3,6), (-7,4.9), (8,-8), (10,2), (8,4)]
print(calcular_valor_maximo(operadores, operandos)) 

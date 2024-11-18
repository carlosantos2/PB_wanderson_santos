def maiores_que_media(conteudo):
    # Calcular a média dos preços
    media = sum(conteudo.values()) / len(conteudo)
    
    produtos_acima_da_media = [
        (nome, preco) for nome, preco in conteudo.items() if preco > media
    ]
    
    # Ordenar os produtos pelo preço em ordem crescente
    produtos_acima_da_media.sort(key=lambda x: x[1])
    
    return produtos_acima_da_media

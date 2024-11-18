import hashlib

while True:
    palavra_mascar = input("Digite uma string para mascarar ou Digite 'sair' para encerrar: ")
    if palavra_mascar.lower() == 'sair':
        break
    has_mascarado = hashlib.sha1(palavra_mascar.encode())
    print("Hash SHA-1:", has_mascarado.hexdigest())
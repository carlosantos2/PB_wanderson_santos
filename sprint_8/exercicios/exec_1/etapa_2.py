# Etapa 2: Lista de animais
animais = ['cachorro', 'gato', 'elefante', 'leão', 'tigre', 
           'girafa', 'zebra', 'macaco', 'cobra', 'panda',
           'coelho', 'urso', 'lobo', 'águia', 'gorila',
           'rinoceronte', 'hipopótamo', 'crocodilo', 'pinguim', 'tartaruga']

animais_ordenados = sorted(animais)
[print(animal) for animal in animais_ordenados]

# Salvando em CSV
with open('animais.csv', 'w') as f:
    for animal in animais_ordenados:
        f.write(f"{animal}\n")


# python etapa_2.py
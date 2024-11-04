'''Exercícios Parte 1
Crie uma classe Avião que possua os atributos modelo, velocidade_maxima, cor e capacidade.

Defina o atributo cor de sua classe , de maneira que todas as instâncias de sua classe avião sejam da cor “azul”.

Após isso, a partir de entradas abaixo, instancie e armazene em uma lista 3 objetos da classe Avião.

Ao final, itere pela lista imprimindo cada um dos objetos no seguinte formato:

“O avião de modelo “x” possui uma velocidade máxima de “y”, capacidade para “z” passageiros e é da cor “w”.

Sendo x, y, z e w cada um dos atributos da classe “Avião”.

Valores de entrada:

modelo BOIENG456: velocidade máxima 1500 km/h: capacidade para 400 passageiros: Cor Azul

modelo Embraer Praetor 600: velocidade máxima 863km/h: capacidade para 14 passageiros: Cor Azul

modelo Antonov An-2: velocidade máxima de 258 Km/h: capacidade para 12 passageiros: Cor Azul'''
class Aviao:
  def __init__(self, modelo, velocidade, capacidade):
    self.modelo = modelo
    self.velocidade = velocidade 
    self.capacidade = capacidade
    self.cor = 'Azul'

listaaviao = []
listaaviao2 = []
listaaviao3 = []
listaaviao.append(Aviao('BOIENG456','1500Km/h','400'))
listaaviao2.append(Aviao('Embraer Praetor 600','863km/h','14'))
listaaviao3.append(Aviao('Antonov An-2','258km/h','12'))

for Aviao in listaaviao:
  print(f'O avião de modelo {Aviao.modelo} possui um velocidade máxima de {Aviao.velocidade}, capacidade para {Aviao.capacidade} passageiros e é da cor {Aviao.cor}')

for Aviao in listaaviao2:
  print(f'O avião de modelo {Aviao.modelo} possui um velocidade máxima de {Aviao.velocidade}, capacidade para {Aviao.capacidade} passageiros e é da cor {Aviao.cor}')

for Aviao in listaaviao3:
  print(f'O avião de modelo {Aviao.modelo} possui um velocidade máxima de {Aviao.velocidade}, capacidade para {Aviao.capacidade} passageiros e é da cor {Aviao.cor}')
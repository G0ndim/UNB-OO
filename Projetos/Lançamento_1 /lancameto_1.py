import classes
from classes import *

while True:

    print(f"{'=-=' * 20}")
    print()
    print(f"{'Calculadora Geometrica Bidimensional':^20}".upper())
    print()
    print(f"{'=-=' * 20}")

    figuras = {1: Poligono, 2: Triangulo, 3: Quadrilatero, 4: Pentagono, 5: Hexagono}

    for i, j in figuras.items():
        print(f"{i}. {j.__str__()}")

    num = int(input(f">>Escolha uma figura: "))

    if num != 1:
        n = num + 1
    else:
        n = int(input("Quantos vértices você quer digitar?: "))

    x, y = [], []

    for i in range(n):
        x.append(float(input(f"Digite o valor de x{i + 1}: ")))
        y.append(float(input(f"Digite o valor de y{i + 1}: ")))

    organizador_de_lista(x, y)
    forma = figuras[num](x, y, n)

    while True:
        print(f'Vértices: {forma.localizacoes()}')
        if input("Deseja trocar algum valor?(s/n): ").strip()[0] in 'Ss':
            posicao = input("Digite a posição do vértice a ser trocado:")
            forma.troca_coordenada(posicao)
        else:
            break

    print(f"Area: {forma.area()}")
    print(f"Perímetro: {forma.perimetro()}")
    print(f"Tipo: {forma.tipo()}")


# problema na funcao troca_coordenada

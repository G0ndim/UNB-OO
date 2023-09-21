
from classes import *


while True:

    print(f"{'=-=' * 20}")
    print()
    print(f"{'Calculadora Geometrica Bidimensional':^20}".upper())
    print()
    print(f"{'=-=' * 20}")

    figuras = ['Poligono', 'Triangulo', "Quadrilatero", "Pentagono", "Hexagono"]

    for i, j in enumerate(figuras):
        print(f"{i + 1}. {j}")

    num = input(f">>Escolha uma figura: ")

    """
    for i, j in enumerate(figuras):
        if num == i:
            fig =
    

    n = int(input("Quantos vértices você quer digitar?: "))
    x, y = [], []

    for i in range(n):
        x.append(float(input(f"Digite o valor de x{i + 1}: ")))
        y.append(float(input(f"Digite o valor de y{i + 1}: ")))

    organizador_de_lista(x, y)

    poligono = Poligono(x, y, n)
    tri = Triangulo(x, y, n)
    poligono.localizacoes()

    print(tri.tipo())
    
    """









from MyLibs.figurasGeometricas import *
from MyLibs.utils import *

while True:

    # Menu com as formas geometricas disponiveis
    figuras = {1: Poligono, 2: Triangulo, 3: Quadrilatero, 4: Pentagono, 5: Hexagono}
    menu_inicial(figuras)

    # Escolha do usuario entre os indices do menu
    opcao = int(input(f">> "))

    # Entrada dos vertices
    eixo_x, eixo_y, n = [], [], [0]
    coletor_vertices(opcao, n, eixo_x, eixo_y)
    forma = figuras[opcao](eixo_x, eixo_y, n[0])

    # Menu opcao de troca dos vertices
    troca_vertice(forma)

    # resultado final
    resultado(forma)


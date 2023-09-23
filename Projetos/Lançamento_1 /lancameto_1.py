from MyLibs.figurasGeometricas import *
from MyLibs.utils import *

while True:

    # Menu com as formas geométricas disponíveis
    figuras = {1: Poligono, 2: Triangulo, 3: Quadrilatero, 4: Pentagono, 5: Hexagono}
    menu_inicial(figuras)

    # Escolha do usuário entre os índices do menu
    opcao = int(input(f">> "))

    # Entrada dos vértices
    eixo_x, eixo_y, n = [], [], [0]
    coletor_vertices(opcao, n, eixo_x, eixo_y)
    forma = figuras[opcao](eixo_x, eixo_y, n[0])

    # Menu opção de troca dos vértices
    troca_vertice(forma)

    # Resultado dos cálculos
    resultado(forma)


from MyLibs.figurasGeometricas import *
from MyLibs.utils import *

while True:

    limpa_terminal()
    # Menu com as formas geométricas disponíveis
    figuras = {1: Poligono, 2: Triangulo, 3: Quadrilatero, 4: Pentagono, 5: Hexagono}
    menu_inicial(figuras)

    # Menu de seleção das figuras
    opcao = menu_selecao(figuras)

    # Entrada dos vértices
    eixo_x, eixo_y, n = [], [], [0]
    coletor_vertices(opcao, n, eixo_x, eixo_y, figuras, opcao)
    forma = figuras[opcao](eixo_x, eixo_y, n[0])

    # Menu opção de troca dos vértices
    troca_vertice(forma, figuras, opcao)

    # Resultado final
    resultado(forma, figuras, opcao)
    print(f"\033[32m{'---' * 15}")
    if input("Deseja continuar?(s/n): ")[0] in "Nn":
        print("Desligando calculadora")
        break

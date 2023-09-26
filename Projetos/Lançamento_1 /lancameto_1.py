from MyLibs.figurasGeometricas import *
from MyLibs.utils import *

while True:

    limpa_terminal()
    # Menu com as formas geometricas disponiveis
    figuras = {1: Poligono, 2: Triangulo, 3: Quadrilatero, 4: Pentagono, 5: Hexagono}
    menu_inicial(figuras)

    opcao = menu_selecao(figuras)

    # Entrada dos vertices
    eixo_x, eixo_y, n = [], [], [0]
    coletor_vertices(opcao, n, eixo_x, eixo_y, figuras, opcao)
    forma = figuras[opcao](eixo_x, eixo_y, n[0])

    # Menu opcao de troca dos vertices
    troca_vertice(forma, figuras, opcao)
    print(f"\033[32m{'---' * 15}")

    # resultado final
    resultado(forma)
    print(f"\033[32m{'---' * 15}")
    if input("Deseja continuar?(s/n): ")[0] in "Nn":
        print("Desligando calculadora")
        break


    """
    menu_inicial(figuras)

    # Escolha do usuario entre os indices do menu
    opcao = int(input(f"\033[36m>>(n): "))
    print(f"\033[32mOpcao selecionada: \033[36m{figuras[opcao].__str__()}")
    print(f"\033[32m{'---' * 15}")

    """
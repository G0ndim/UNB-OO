
def limpa_terminal():
    from subprocess import run
    from platform import system, release
    if system() == "Windows":
        if release() in {"10", "11"}:
            run("", shell=True)
            print("\033c", end="")
        else:
            run(["cls"])
    else:  # Linux and Mac
        print("\033c", end="")


def menu_inicial(figuras):

    print(f"\033[32m{'=-=' * 15}")
    print(f"\033[32m{'Calculadora Geométrica Bidimensional':^45}".upper())
    print(f"\033[32m{'=-=' * 15}")
    print(f"\033[32m{'Escolha uma das opções':^45}")
    for i, j in figuras.items():
        a = f"\033[36m{i}. \033[32m{j.__str__()}"
        print(f"\033[32m{a:<10}")
    print(f"\033[32m{'---' * 15}")
    pass


def menu_selecao(figuras):

    while True:
        opcao = int(input(f"\033[36m>>(n): "))
        limpa_terminal()
        print(f"\033[32m{'=-=' * 15}")
        print(f"\033[32m{'Calculadora Geométrica Bidimensional':^45}".upper())
        print(f"\033[32m{'=-=' * 15}")
        print(f"\033[32m{'Opção escolhida':^45}")
        for i, j in figuras.items():
            if i == opcao:
                a = f"\033[36m{i}. \033[7;36m{j.__str__()}\033[0m"
            else:
                a = f"\033[36m{i}. \033[32m{j.__str__()}"
            print(f"\033[32m{a:<10}")
        print(f"\033[32m{'---' * 15}")
        if input("Deseja selecionar outra opção?\033[36m(s/n): ") in "Nn":
            limpa_terminal()
            print(f"\033[32m{'=-=' * 15}")
            print(f"\033[32m{figuras[opcao].__str__():^45}".upper())
            print(f"\033[32m{'=-=' * 15}")
            break

    return opcao


def organizador_de_lista(lista_x, lista_y):
    """
    Função que organiza os vértices de um poligono convexo de forma anti-horária em relação ao ângulo entre suas
    coordenadas e um ponto central.

    :param lista_x: lista contendo os valores no eixo x
    :param lista_y: lista contendo os valores no eixo y
    :return:
    """
    from math import atan2, pi
    lista = []

    # [x1, x2, x3 ...] , [y1, y2, y3...]    --->   [[x1, y1], [x2, y2], ...]
    for i in range(len(lista_x)):
        lis = []
        lis.append(lista_x[i])
        lis.append(lista_y[i])
        lista.append(lis)
        del lis

    # Organiza as coordenadas em uma lista ordenada com relação ao ângulo formado
    # entre elas e um ponto no centro do poligono, de forma anti-horária.
    menor = min(lista, key=lambda x: (x[1], x[0]))
    lista.pop(lista.index(menor))

    vertices = sorted(lista, key=lambda x: atan2(x[1] - menor[1], x[0] - menor[0]) + 2 * pi)
    vertices.insert(0, menor)

    # Retorna os valores de x e y para suas respectivas lista, ja organizados.
    lista_x.clear()
    lista_y.clear()
    for i in vertices:
        lista_x.append(i[0])
        lista_y.append(i[1])
    pass


def coletor_vertices(num1, num_f, lista_x, lista_y, figuras, opcao):

    if num1 != 1:
        num_f[0] = num1 + 1
    else:
        print("\033[32mQuantos vértices você quer digitar?")
        num_f[0] = int(input("\033[36m>>(n): "))
        print(f"\033[32m{'---' * 15}")

    vertices = []
    x, y = [], []
    for i in range(num_f[0]):
        vertices.append([f"x{i + 1}", f"y{i + 1}"])

    for i in range(num_f[0] * 2):
        limpa_terminal()
        print(f"\033[32m{'=-=' * 15}")
        print(f"\033[32m{figuras[opcao].__str__():^45}".upper())
        print(f"\033[32m{'=-=' * 15}")
        print(f"\033[32mPreencha as coordenadas dos \033[36m{num_f[0]} \033[32mvértices a seguir: ")
        print()
        counter = 0
        for j in range(len(vertices)):
            print(f"\033[0;36m{j+1}.\033[0;32m (", end='')
            for k in range(2):
                if counter == i:
                    if k == 0:
                        print(f"\033[7;36m{vertices[j][k]}\033[0;32m", end=', ')
                    else:
                        print(f"\033[7;36m{vertices[j][k]}\033[0;32m", end='')
                    a, b = j, k
                else:
                    if k == 0:
                        print(f"\033[32m{vertices[j][k]}", end=', ')
                    else:
                        print(f"\033[32m{vertices[j][k]}", end='')
                counter += 1
            print(")")
        print(f"{'---' * 15}")
        coordenada = float(eval(input(f"\033[36m>>({vertices[a][b]}): ")))
        vertices[a][b] = coordenada
        if b == 0:
            x.append(vertices[a][b])
        else:
            y.append(vertices[a][b])
        print()

    organizador_de_lista(x, y)

    for i in range(len(x)):
        lista_x.append(x[i])
        lista_y.append(y[i])

    pass


def menu_vertices(classe, figuras, opcao):
    limpa_terminal()
    print(f"\033[32m{'=-=' * 15}")
    print(f"\033[32m{figuras[opcao].__str__():^45}".upper())
    print(f"\033[32m{'=-=' * 15}")
    print(f"\033[32m{'Vértices':^45}")
    for i, j in classe.localizacoes().items():
        a = f"\033[36m{i}. \033[32m{j.__str__()}"
        print(f"\033[32m{a:<10}")
    print(f"\033[32m{'---' * 15}")
    pass


def troca_vertice(classe, figuras, opcao):
    while True:
        menu_vertices(classe, figuras, opcao)
        if input("Deseja trocar algum valor?\033[36m(s/n): ").strip()[0] in 'Ss':
            limpa_terminal()
            print(f"\033[32m{'=-=' * 15}")
            print(f"\033[32m{figuras[opcao].__str__():^45}".upper())
            print(f"\033[32m{'=-=' * 15}")
            print(f"\033[32m{'Digite a posição do vértice a ser trocado':^45}")
            for i, j in classe.localizacoes().items():
                a = f"\033[36m{i}. \033[32m{j.__str__()}"
                print(f"\033[32m{a:<10}")
            print(f"\033[32m{'---' * 15}")
            while True:
                posicao = int(input("\033[36m>>(n): \033[0m"))
                limpa_terminal()
                print(f"\033[32m{'=-=' * 15}")
                print(f"\033[32m{figuras[opcao].__str__():^45}".upper())
                print(f"\033[32m{'=-=' * 15}")
                print(f"\033[32m{'Opção selecionada':^45}")
                for i, j in classe.localizacoes().items():
                    if i == posicao:
                        a = f"\033[36m{i}. \033[7;36m{j}\033[0m"
                    else:
                        a = f"\033[36m{i}. \033[32m{j}"
                    print(f"\033[32m{a:<10}")
                print(f"\033[32m{'---' * 15}")
                if input("Deseja selecionar outra opção?\033[36m(s/n): ") in "Nn":
                    break

            count = 0
            x_nov = "x"
            y_nov = "y"
            for j in range(2):
                limpa_terminal()
                print(f"\033[32m{'=-=' * 15}")
                print(f"\033[32m{figuras[opcao].__str__():^45}".upper())
                print(f"\033[32m{'=-=' * 15}")
                print(f"\033[32m{'Digite os novos valores':^45}")
                for k, l in classe.localizacoes().items():
                    if k == posicao:
                        if j == 0:
                            a = f"\033[36m{k}. {l}   --->   (\033[7m{x_nov}\033[0;36m, {y_nov})"
                        else:
                            a = f"\033[36m{k}. {l}   --->   ({x_nov}, \033[7m{y_nov}\033[0;36m)\033[0;32m"
                    else:
                        a = f"\033[36m{k}. \033[32m{l}"
                    print(f"\033[32m{a:<10}")
                if j == 0:
                    print(f"\033[32m{'---' * 15}")
                    x_nov = float(eval(input(f"\033[36m>>(x{posicao}): ")))
                else:
                    print(f"\033[32m{'---' * 15}")
                    y_nov = float(eval(input(f"\033[36m>>(y{posicao}): ")))
            limpa_terminal()
            print(f"\033[32m{'=-=' * 15}")
            print(f"\033[32m{figuras[opcao].__str__():^45}".upper())
            print(f"\033[32m{'=-=' * 15}")
            print(f"\033[32m{'Coordenadas modificadas':^45}")
            for m, n in classe.localizacoes().items():
                if m == posicao:
                    b = f"\033[36m{m}. {n}   --->   ({x_nov}, {y_nov})\033[32m"
                else:
                    b = f"\033[36m{m}. \033[32m{n}"
                print(f"\033[32m{b:<10}")
            print(f"{'---' * 15}")
            resposta = input("\033[32mQuer manter as alterações?\033[36m(s/n): ")
            if resposta.strip()[0] in 'Ss':
                classe.troca_coordenada(posicao - 1, x_nov, y_nov)
            organizador_de_lista(classe.crd_x, classe.crd_y)
        else:
            break
    pass


def resultado(classe, figuras, opcao):
    menu_vertices(classe, figuras, opcao)
    print(f"Classificação: {classe.tipo()}")
    print(f"Àrea: {classe.area(): .2f}")
    print(f"Perímetro: {classe.perimetro(): .2f}")
    print(f"Ângulos internos: ", end='')
    for i, j in enumerate(classe.angulos_internos()):
        if i == len(classe.angulos_internos()) - 1:
            print(f"{j}°.")
        else:
            print(f"{j}°", end=', ')
    pass


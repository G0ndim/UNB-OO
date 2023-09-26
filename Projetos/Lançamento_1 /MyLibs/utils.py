
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
                a = f"\033[36m{i}. \033[7;32m{j.__str__()}\033[0m"
            else:
                a = f"\033[36m{i}. \033[32m{j.__str__()}"
            print(f"\033[32m{a:<10}")
        print(f"\033[32m{'---' * 15}")
        if input("Deseja selecionar outra opção?(s/n): ") in "Nn":
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
    vertices = sorted(lista, key=lambda x: atan2(x[1] - menor[1], x[0] - menor[0]) + 2 * pi)

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
        coordenada = float(input(f"\033[36m>>({vertices[a][b]}): "))
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
        if input("Deseja trocar algum valor?(s/n): ").strip()[0] in 'Ss':
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
                        a = f"\033[36m{i}. \033[7;32m{j}\033[0m"
                    else:
                        a = f"\033[36m{i}. \033[32m{j}"
                    print(f"\033[32m{a:<10}")
                print(f"\033[32m{'---' * 15}")
                if input("Deseja selecionar outra opção?(s/n): ") in "Nn":
                    break

            for i in range(2):
                limpa_terminal()
                print(f"\033[32m{'=-=' * 15}")
                print(f"\033[32m{figuras[opcao].__str__():^45}".upper())
                print(f"\033[32m{'=-=' * 15}")
                print(f"\033[32m{'Digite os novos valores':^45}")
                if i == 0:
                    a = f"(\033[7;32m{classe.localizacoes()[posicao][0]}\033[0;32m, {classe.localizacoes()[posicao][1]})"
                    print(f"{a:^45}")
                    print(f"\033[32m{'---' * 15}")
                    x_nov = float(input(f"\033[36m>>(n): "))
                else:
                    a = f"({classe.localizacoes()[posicao][0]}, \033[7;32m{classe.localizacoes()[posicao][1]}\033[0;32m)"
                    print(f"{a:^45}")
                    print(f"\033[32m{'---' * 15}")
                    y_nov = float(input(f"\033[36m>>(n): "))

            print(f"\033[0;32m({classe.crd_x[posicao - 1]}, {classe.crd_y[posicao - 1]})  --->  ({x_nov}, {y_nov})")
            resposta = input("Quer manter as alterações?(s/n): ")
            if resposta.strip()[0] in 'Ss':
                classe.troca_coordenada(posicao - 1, x_nov, y_nov)
            organizador_de_lista(classe.crd_x, classe.crd_y)
        else:
            break
    pass


def resultado(classe, figuras, opcao):
    menu_vertices(classe, figuras, opcao)
    print(f"Àrea: {classe.area()}")
    print(f"Perímetro: {classe.perimetro()}")
    print(f"Ângulos internos: {classe.angulos_internos()}")
    print(classe.tipo())
    pass

# (6.0, 0.0), 2: (0.0, 0.0), 3: (8.0, 4.0), 4: (2.0, 4.0)

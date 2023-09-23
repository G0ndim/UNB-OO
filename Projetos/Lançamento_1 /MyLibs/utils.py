
def menu_inicial(figuras):

    print(f"{'=-=' * 15}")
    print(f"{'Calculadora Geometrica Bidimensional':^45}".upper())
    print(f"{'=-=' * 15}")
    print(f"{'Escolha uma figura':^45}")
    for i, j in figuras.items():
        a = f"{i}. {j.__str__()}"
        print(f"{a:<10}")
    print(f"{'---' * 15}")
    pass


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


def coletor_vertices(num1, num_f, lista_x, lista_y):

    if num1 != 1:
        num_f[0] = num1 + 1
    else:
        num_f[0] = int(input("Quantos vértices você quer digitar?: "))

    x, y = [], []

    for i in range(num_f[0]):
        x.append(float(input(f"Digite o valor de x{i + 1}: ")))
        y.append(float(input(f"Digite o valor de y{i + 1}: ")))

    organizador_de_lista(x, y)

    for i in range(len(x)):
        lista_x.append(x[i])
        lista_y.append(y[i])

    pass


def troca_vertice(classe):
    while True:
        print(f'Vértices: {classe.localizacoes()}')
        if input("Deseja trocar algum valor?(s/n): ").strip()[0] in 'Ss':
            posicao = int(input("Digite a posição do vértice a ser trocado:"))
            x_nov = float(input(f"Digite o novo valor de x{posicao}: "))
            y_nov = float(input(f"Digite o novo valor de y{posicao}: "))
            print(f"({classe.crd_x[posicao - 1]}, {classe.crd_y[posicao - 1]})  --->  ({x_nov}, {y_nov})")
            resposta = input("Quer manter as alterações?(s/n)")
            if resposta.strip()[0] in 'Ss':
                classe.troca_coordenada(posicao - 1, x_nov, y_nov)
        else:
            break
    pass


def resultado(classe):
    print(f"Area: {classe.area()}")
    print(f"Perímetro: {classe.perimetro()}")
    print(f"Tipo: {classe.tipo()}")
    pass


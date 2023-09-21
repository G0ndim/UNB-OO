class Ponto:

    def __init__(self, x, y, n):
        self.crd_x = x
        self.crd_y = y
        self.num = n

    def localizacoes(self):
        print("Localizacoes: ", end='')
        for i in range(len(self.crd_x)):
            print(f"({self.crd_x[i]}, {self.crd_y[i]})", end=' ')
        print()

    def troca_coordenada(self, posicao):
        """
        Método para trocar as coordenadas de um dado vertice
        :param posicao: Posição do do vertice dentro da lista
        :return:
        """
        x_novo = input(f"Digite o novo valor de x{posicao}: ")
        y_novo = input(f"Digite o novo valor de y{posicao}: ")
        print(f"({self.crd_x[posicao]}, {self.crd_y[posicao]}) --> ({x_novo}, {y_novo})")
        resposta = input("Quer manter as alterações?(s/n)")
        if resposta.strip()[0] in 'Ss':
            self.crd_x[posicao] = x_novo
            self.crd_y[posicao] = y_novo
        pass

    def lados(self):
        l_lados = []
        for i in range(self.num - 1):
            l_lados.append((((abs(self.crd_x[i] - self.crd_x[i + 1]) ** 2) + (abs(self.crd_y[i] - self.crd_y[i + 1]))
            ** 2)) ** (1 / 2))
        l_lados.append((((abs(self.crd_x[-1] - self.crd_x[0]) ** 2) + (abs(self.crd_y[-1] - self.crd_y[0]) ** 2))
                      ** (1 / 2)))

        return l_lados


class Poligono(Ponto):

    def __init__(self, x, y, n):
        super().__init__(x, y, n)

    def area(self):
        """
        Função que calcula a área de um poligono pelo Método de Gauss
        dado um determinado número de vertices dentro de um plano cartesiano.

        ATENCAO! para esse método funcionar é preciso primtiro utilizar a função
        "organizador_de_lista", pois os vertices do poligono precisam estar
        ordenados de forma anti-horaria

        :param x: lista das posições no eixo x
        :param y: lista das posiçõs no eixo y
        :param n: número de coordenadas
        :return: Área do poligono
        """
        area = 0.0
        j = self.num - 1
        for i in range(0, self.num):
            area += ((self.crd_x[j] + self.crd_x[i]) *
                     (self.crd_y[j] - self.crd_y[i]))
            j = i

        return float(abs(area / 2.0))

    def perimetro(self):
        return sum(self.lados())

    def verifica_convexo(self):
        pass

    @classmethod
    def tipo(cls):
        raise NotImplementedError('A classe filha precisa implementar esse metodo')


class Triangulo(Poligono):

    def __init__(self, x, y, n):
        super().__init__(x, y, n)

    def tipo(self):
        x = [self.lados().count(i) for i in self.lados()]
        if 3 in x:
            return "Equilatero"
        elif 2 in x:
            return "Isoceles"
        else:
            return "Escaleno"


class Quadrilatero(Poligono):

    def __init__(self, x, y, n):
        super().__init__(x, y, n)

    @classmethod
    def tipo(cls):

        pass


class Pentagono(Poligono):

    def __init__(self, x, y, n):
        super().__init__(x, y, n)

    @classmethod
    def tipo(cls):
        return f'{cls}'


class Hexagono(Pentagono):

    def __init__(self, x, y, n):
        super().__init__(x, y, n)

    @classmethod
    def tipo(cls):
        return f'{cls}'


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



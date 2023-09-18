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
        pass

class Poligono(Ponto):

    def __init__(self, x, y, n):
        super().__init__(x, y, n)

    def area(self):
        """
        Funcao que calcula a area de um poligono pelo Metodo de Gauss
        dado um determinado numero de vertices dentro de um plano cartesiano.

        ATENCAO! para essa funcao funcionar e preciso utilizar a outra funcao
        "organizador_de_lista", pois e preciso que os vertices do poligono
        estejam ordenadas de forma anti-horaria para a funcao funcionar

        :param x: lista das posicoes no eixo x
        :param y: lista das posicoes no eixo y
        :param n: numero de coordenadas
        :return: Area do poligono
        """
        area = 0.0
        j = self.num - 1
        for i in range(0, self.num):
            area += ((self.crd_x[j] + self.crd_x[i]) *
                     (self.crd_y[j] - self.crd_y[i]))
            j = i

        return float(abs(area / 2.0))

    def perimetro(self):
        perimetro = 0
        for i in range(self.num - 1):
            perimetro += (((abs(self.crd_x[i] - self.crd_x[i + 1]) ** 2) + (abs(self.crd_y[i] - self.crd_y[i + 1])
            ** 2)) ** (1 / 2))
        perimetro += (((abs(self.crd_x[-1] - self.crd_x[0]) ** 2) + (abs(self.crd_y[-1] - self.crd_y[0]) ** 2))
                      ** (1 / 2))
        return perimetro

    @classmethod
    def tipo(cls):
        raise NotImplementedError('A classe filha precisa implementar esse metodo')


class Triangulo(Poligono):

    def __init__(self, x, y, n):
        super().__init__(x, y, n)

    @classmethod
    def tipo(cls):
        return f'{cls}'


class Quadrilatero(Poligono):

    def __init__(self, x, y, n):
        super().__init__(x, y, n)

    @classmethod
    def tipo(cls):
        return f'{cls}'


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
    Funcao que organiza os vertices de um poligono convexo de forma anti-horaria em relacao com o angulo entre suas
    coordenadas e um ponto central.

    :param lista_x: lista contendo os valores no eixo x
    :param lista_y: lista contendo os valores no eixo y
    :return:
    """
    from math import atan2, pi
    lista = []

    # cria uma lista de coordendas [[x1, y1], [x2, y2], ...]
    for i in range(len(lista_x)):
        lis = []
        lis.append(lista_x[i])
        lis.append(lista_y[i])
        lista.append(lis)
        del lis

    # Organiza as coordenadas em relacao ao angulo formado entre elas e um ponto central do poligono,
    # de forma anti-horaria, dentro do primeiro quadrante.
    menor = min(lista, key=lambda x: (x[1], x[0]))
    vertices = sorted(lista, key=lambda x: atan2(x[1] - menor[1], x[0] - menor[0]) + 2 * pi)

    # Retorna os valores de x e y para suas respectivas lista, ja organizados.
    lista_x.clear()
    lista_y.clear()
    for i in vertices:
        lista_x.append(i[0])
        lista_y.append(i[1])
    pass

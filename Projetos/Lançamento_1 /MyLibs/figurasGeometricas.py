class Ponto:

    def __init__(self, x, y, n):
        self.crd_x = x
        self.crd_y = y
        self.num = n

    def localizacoes(self):
        locs = {}
        for i in range(len(self.crd_x)):
            locs.update({i+1: (self.crd_x[i], self.crd_y[i])})
        return locs

    def troca_coordenada(self, posicao, x_novo, y_novo):
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
        # raise NotImplementedError('A classe filha precisa implementar esse metodo')
        pass

    @classmethod
    def __str__(cls):
        return f"Poligono"


class Triangulo(Poligono):

    def __init__(self, x, y, n):
        super().__init__(x, y, n)

    def tipo(self):
        x = [self.lados().count(i) for i in self.lados()]
        if 3 in x:
            return "Triangulo Equilatero"
        elif 2 in x:
            return "Triangulo Isoceles"
        else:
            return "Triangulo Escaleno"

    @classmethod
    def __str__(cls):
        return f"Triângulo"


class Quadrilatero(Poligono):

    def __init__(self, x, y, n):
        super().__init__(x, y, n)

    def tipo(self):
        pass

    @classmethod
    def __str__(cls):
        return f"Quadrilátero"


class Pentagono(Poligono):

    def __init__(self, x, y, n):
        super().__init__(x, y, n)

    def tipo(self):
        for i in range(len(self.lados())):
            if self.lados()[0] != self.lados()[i]:
                return "Pentagono Irregular"
        return "Pentagono Regular"

    @classmethod
    def __str__(cls):
        return f"Pentagono"


class Hexagono(Poligono):

    def __init__(self, x, y, n):
        super().__init__(x, y, n)

    def tipo(self):
        for i in range(len(self.lados())):
            if self.lados()[0] != self.lados()[i]:
                return "Hexagono Irregular"
        return "Hexagono Regular"

    @classmethod
    def __str__(cls):
        return f"Hexagono"


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

    def angulos_internos(self):
        from math import atan2, degrees, pi
        lista = []

        for i in range(len(self.crd_x)):
            resultado = (atan2(self.crd_y[-1] - self.crd_y[0], self.crd_x[-1] - self.crd_x[0])
                         - atan2(self.crd_y[1] - self.crd_y[0], self.crd_x[1] - self.crd_x[0]))
            if resultado < 0:
                resultado = (2 * pi) + resultado
            lista.append(round(degrees(resultado)))
            self.crd_x.insert(0, self.crd_x[-1])
            self.crd_x.pop(-1)
            self.crd_y.insert(0, self.crd_y[-1])
            self.crd_y.pop(-1)

        return lista

    def verifica_convexo(self):
        y = [i for i in self.angulos_internos() if i > 180]
        if len(y) == 0:
            return "convexo"
        else:
            return "concavo"

    def tipo(self):
        tipos = ["Triângulo", "Quadrilátero", "Pentágono", "Hexágono", "Polígono"]
        i = len(self.crd_x)
        if i > 5:
            resposta = tipos[4]
        else:
            resposta = tipos[i - 3]
        if self.verifica_convexo() == "concavo":
            resposta = resposta + " Côncavo"
        else:
            resposta = resposta + " Convexo"

        return resposta

    @classmethod
    def __str__(cls):
        return f"Polígono"


class Triangulo(Poligono):

    def __init__(self, x, y, n):
        super().__init__(x, y, n)

    def tipo(self):
        x = [self.lados().count(i) for i in self.lados()]
        if 3 in x:
            return "Triângulo Equilátero"
        elif 2 in x:
            return "Triângulo Isósceles"
        elif 90 in self.angulos_internos():
            return "Triângulo Retângulo"
        return "Triângulo Escaleno"

    @classmethod
    def __str__(cls):
        return f"Triângulo"


class Quadrilatero(Poligono):

    def __init__(self, x, y, n):
        super().__init__(x, y, n)

    def tipo(self):
        if self.verifica_convexo() == "concavo":
            return "Quadrilatero Concavo"
        elif self.lados().count(self.lados()[0]) == 4:
            if 90 in self.angulos_internos():
                return "Quadrado"
            else:
                return "Losango"
        elif self.lados()[0] == self.lados()[2] and self.lados()[1] == self.lados()[3]:
            if 90 in self.angulos_internos():
                return "Retângulo"
            else:
                return "Paralelogramo"
        elif 90 in self.angulos_internos():
            return "Trapezio Retângulo"
        elif self.lados()[0] == self.lados()[2] or self.lados()[1] == self.lados()[3]:
            return "Trapezio Isósceles"
        else:
            if self.angulos_internos()[0] + self.angulos_internos()[1] == 90:
                return "Trapezio Escaleno"
            else:
                return "Quadrilátero Irregular"

    @classmethod
    def __str__(cls):
        return f"Quadrilátero"


class Pentagono(Poligono):

    def __init__(self, x, y, n):
        super().__init__(x, y, n)

    def tipo(self):
        if self.verifica_convexo() == "concavo":
            return "Pentágono Côncavo"
        for i in range(len(self.lados())):
            if self.lados()[0] != self.lados()[i]:
                return "Pentágono Irregular"
        return "Pentágono Regular"

    @classmethod
    def __str__(cls):
        return f"Pentágono"


class Hexagono(Poligono):

    def __init__(self, x, y, n):
        super().__init__(x, y, n)

    def tipo(self):
        if self.verifica_convexo() == "concavo":
            return "Hexágono Côncavo"
        for i in range(len(self.lados())):
            if self.lados()[0] != self.lados()[i]:
                return "Hexágono Irregular"
        return "Hexágono Regular"

    @classmethod
    def __str__(cls):
        return f"Hexágono"


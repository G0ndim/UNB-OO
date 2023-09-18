
from classes import *


while True:

    n = int(input("Quantos vertices voce quer digitar?: "))
    x, y = [], []

    for i in range(n):
        x.append(float(input(f"Digite o valor de x{i + 1}: ")))
        y.append(float(input(f"Digite o valor de y{i + 1}: ")))

    organizador_de_lista(x, y)

    poligono = Poligono(x, y, n)
    poligono.localizacoes()
    print(poligono.area())










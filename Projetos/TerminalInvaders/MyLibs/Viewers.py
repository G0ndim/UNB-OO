import pygame
from Models import *

pygame.init()


class Display:
    def __init__(self, largura, comprimento, nome):
        self._x = largura
        self._y = comprimento
        self._name = nome

    def screen(self, player, enemy, bala):
        tela = pygame.display.set_mode((self._x, self._y))
        pygame.display.set_caption(f'{self._name}')
        clock = pygame.time.Clock()
        player.pos_x = self._x / 2
        player.pos_y = self._y / 2

        while True:
            tela.fill('blue')
            player.movimentar(tela)
            enemy.spawn(self._x, self._y, tela)
            enemy.movimento(player.pos_x, player.pos_y, tela)
            bala.movimento(tela, player.pos_x, player.pos_y)
            pygame.display.update()
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

    pass


if __name__ == '__main__':
    name = 'Jogo :)'
    J = Jogador(15, 15, 15)
    N = Zumbi(5, 5, 5, 5)
    B = Bala(5, 3)
    teste = Display(1080, 1080, name)
    teste.screen(J, N, B)

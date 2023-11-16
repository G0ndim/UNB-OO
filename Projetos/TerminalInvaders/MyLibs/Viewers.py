import pygame
from Models import *

pygame.init()


class Display:
    def __init__(self, largura, comprimento, nome):
        self._x = largura
        self._y = comprimento
        self._name = nome

    def screen(self, player):
        tela = pygame.display.set_mode((self._x, self._y))
        pygame.display.set_caption(f'{self._name}')  # nome da janela
        clock = pygame.time.Clock()  # tempo do jogo
        # jogador = pg.image.load(player.player_skin)
        player_image = pygame.image.load(player.player_skin)
        player_image = pygame.transform.scale(player_image, (71, 97))
        tmh_x = self._x / 2
        tmh_y = self._y / 2
        player_rect = player_image.get_rect()

        while True:
            keys = pygame.key.get_pressed()
            speed = player.velocidade
            tela.fill('white')

            if keys[pygame.K_w] and tmh_y > 0:
                tmh_y -= speed
            if keys[pygame.K_s] and tmh_y < 1080 - player_rect.height:
                tmh_y += speed
            if keys[pygame.K_a] and tmh_x > 0:
                tmh_x -= speed
            if keys[pygame.K_d] and tmh_x < 1080 - player_rect.width:
                tmh_x += speed

            tela.blit(player_image, (tmh_x, tmh_y))
            pg.display.update()
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

    pass


if __name__ == '__main__':
    name = 'Jogo :)'
    J = Jogador(15, 15, 15)
    teste = Display(1080, 1080, name)
    teste.screen(J)

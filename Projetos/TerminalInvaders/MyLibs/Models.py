import pygame
from random import randint
from math import atan2, cos, sin

pygame.init()


class Jogador:
    def __init__(self, vida, estamina, velocidade, pontuacao=0):
        self._vida = vida
        self._estamina = estamina
        self.velocidade = velocidade
        self.armas = list()
        self.player_skin = '../public/player_test.png'
        self.pontuacao = pontuacao
        self.pos_x = int()
        self.pos_y = int()
        self.player_image = pygame.image.load(self.player_skin)
        self.player_rect = self.player_image.get_rect(topleft=(self.pos_x, self.pos_y))

    def movimentar(self, tela):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.pos_y > 0:
            self.pos_y -= self.velocidade
        if keys[pygame.K_s] and self.pos_y < 1080 - self.player_rect.height:
            self.pos_y += self.velocidade
        if keys[pygame.K_a] and self.pos_x > 0:
            self.pos_x -= self.velocidade
        if keys[pygame.K_d] and self.pos_x < 1080 - self.player_rect.width:
            self.pos_x += self.velocidade

        self.player_rect = self.player_image.get_rect()
        tela.blit(self.player_image, (self.pos_x, self.pos_y))


class Bala:
    def __init__(self, dano, velocidade,):
        self.dano = dano
        self.velocidade = velocidade
        self.skin = '../public/bullet_test.png'
        self.bullet_image = pygame.image.load(self.skin)
        self.bullet_rect = self.bullet_image.get_rect()


class Arma:
    def __init__(self, tempo_de_recarga):
        self.tmp_recarga = tempo_de_recarga
        self.weapon_skin = '../public/pistol.png'
        self.weapon_image = pygame.image.load(self.weapon_skin)

    def display_weapon(self, player_x, player_y, tela):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        tela.blit(self.weapon_image, (player_x, player_y))



class Inimigo:
    def __init__(self, vida, velocidade, pontos, dano):
        self.vida = vida
        self.velocidade = velocidade
        self.pontos = pontos
        self.dano = dano
        self.pos_x = int()
        self.pos_y = int()
        self.enemy_skin = '../public/enemy_error.png'
        self.enemy_image = pygame.image.load(self.enemy_skin)
        self.enemy_rect = self.enemy_image.get_rect()
        self.spawn_condition = False

    def spawn(self, x_tela, y_tela, tela):
        if not self.spawn_condition:
            x_inicial = randint(0, 1)
            y_inicial = randint(0, 1)
            if x_inicial:
                self.pos_x = randint(x_tela, x_tela + 100)
            else:
                self.pos_x = randint(-100, 0)
            if y_inicial:
                self.pos_y = randint(y_tela, y_tela + 100)
            else:
                self.pos_y = randint(-100, 0)

            self.enemy_rect = self.enemy_image.get_rect(topleft=(self.pos_x, self.pos_y))
            tela.blit(self.enemy_image, (self.pos_x, self.pos_y))
            self.spawn_condition = True

    def movimento(self, x_player, y_player, tela):
        ang = atan2(y_player - self.pos_y, x_player - self.pos_x)
        self.pos_x += self.velocidade * cos(ang)
        self.pos_y += self.velocidade * sin(ang)

        self.enemy_rect = self.enemy_image.get_rect(topleft=(self.pos_x, self.pos_y))
        tela.blit(self.enemy_image, (self.pos_x, self.pos_y))

    def ataque(self, colisao):
        pass


class Zumbi(Inimigo):
    def __init__(self, vida, velocidade, pontos, dano):
        super().__init__(vida, velocidade, pontos, dano)
        self.enemy_skin = '../public/zombie_test.png'
        self.enemy_image = pygame.image.load(self.enemy_skin)
        self.enemy_rect = self.enemy_image.get_rect()
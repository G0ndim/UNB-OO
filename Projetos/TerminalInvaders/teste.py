import pygame
from math import atan2, cos, sin
from random import randint


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.pos_x = 540
        self.pos_y = 540
        self.player_image = pygame.image.load('./public/player/player_left_pistol.png')
        self.player_rect = self.player_image.get_rect()
        self.velocidade = 1

    def movimentar(self, tela):
        keys = pygame.key.get_pressed()
        mouse_pos = pygame.mouse.get_pos()

        # Movimento do jogador na tela
        if keys[pygame.K_w] and self.pos_y > 0:
            self.pos_y -= self.velocidade
        if keys[pygame.K_s] and self.pos_y < 1080 - self.player_rect.height:
            self.pos_y += self.velocidade
        if keys[pygame.K_a] and self.pos_x > 0:
            self.pos_x -= self.velocidade
        if keys[pygame.K_d] and self.pos_x < 1080 - self.player_rect.width:
            self.pos_x += self.velocidade

        # Movimento do personagem na direcao do mouse
        if self.player_rect.topleft[0] <= mouse_pos[0] <= self.player_rect.topright[0]:
            if mouse_pos[1] <= self.pos_y:
                self.player_image = pygame.image.load('./public/player/player_top_pistol.png')
            if mouse_pos[1] >= self.pos_y:
                self.player_image = pygame.image.load('./public/player/player_bottom_pistol.png')
        elif mouse_pos[0] < self.player_rect.topleft[0]:
            if mouse_pos[1] <= self.player_rect.topleft[1]:
                self.player_image = pygame.image.load('./public/player/player_top_left_pistol.png')
            if mouse_pos[1] >= self.player_rect.bottomleft[1]:
                self.player_image = pygame.image.load('./public/player/player_bottom_left_pistol.png')
            if self.player_rect.bottomleft[1] >= mouse_pos[1] >= self.player_rect.topleft[1]:
                self.player_image = pygame.image.load('./public/player/player_left_pistol.png')
        elif mouse_pos[0] > self.player_rect.topright[0]:
            if mouse_pos[1] < self.player_rect.topright[1]:
                self.player_image = pygame.image.load('./public/player/player_top_right_pistol.png')
            if mouse_pos[1] > self.player_rect.bottomright[1]:
                self.player_image = pygame.image.load('./public/player/player_bottom_right_pistol.png')
            if self.player_rect.bottomright[1] >= mouse_pos[1] >= self.player_rect.topright[1]:
                self.player_image = pygame.image.load('./public/player/player_right_pistol.png')

        tela.blit(self.player_image, (self.pos_x, self.pos_y))
        self.player_rect = self.player_image.get_rect(topleft=(self.pos_x, self.pos_y))

    def create_bullet(self):
        return Bullet(self.player_rect.center[0], self.player_rect.center[1])


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.Surface((3, 3))
        self.image.fill((255, 0, 0))
        self.pos_y = pos_y
        self.pos_x = pos_x
        self.rect = self.image.get_rect(center=(pos_x, pos_y))
        self.ang = int()
        self.mouse_pos = tuple()
        self.flag = False

    def update(self):
        if not self.flag:
            self.mouse_pos = pygame.mouse.get_pos()
            self.flag = True
        self.ang = atan2(self.mouse_pos[1] - self.pos_y, self.mouse_pos[0] - self.pos_x)
        self.rect.x += 5 * cos(self.ang)
        self.rect.y += 5 * sin(self.ang)

        if self.rect.x >= 1080 or self.rect.x <= 0 or self.rect.y >= 1080 or self.rect.y <= 0:
            self.kill()


class Inimigo(pygame.sprite.Sprite):
    def __init__(self, velocidade, x_tela, y_tela):
        super().__init__()
        self.velocidade = velocidade
        self.pos_x = int()
        self.pos_y = int()
        self.enemy_skin = './public/enemy/enemy_error.png'
        self.enemy_image = pygame.image.load(self.enemy_skin)
        self.enemy_rect = self.enemy_image.get_rect()
        self.spawn_condition = False
        self.x_tela = x_tela
        self.y_tela = y_tela
        self.sprites_left = list()
        self.sprites_right = list()
        self.sprites_left.append(pygame.image.load('./public/zombie_models/zombie_left_walking_1.png'))
        self.sprites_left.append(pygame.image.load('./public/zombie_models/zombie_left_walking_2.png'))
        self.sprites_right.append(pygame.image.load('./public/zombie_models/zombie_right_walking_1.png'))
        self.sprites_right.append(pygame.image.load('./public/zombie_models/zombie_right_walking_2.png'))
        self.current_walking_sprite = 0
        self.attack_sprites_left = list()
        self.attack_sprites_right = list()
        self.attack_sprites_left.append(pygame.image.load('./public/zombie_models/zombie_left_atk_1.png'))
        self.attack_sprites_left.append(pygame.image.load('./public/zombie_models/zombie_left_atk_2.png'))
        self.attack_sprites_left.append(pygame.image.load('./public/zombie_models/zombie_left_atk_3.png'))
        self.attack_sprites_left.append(pygame.image.load('./public/zombie_models/zombie_left_atk_4.png'))
        self.attack_sprites_right.append(pygame.image.load('./public/zombie_models/zombie_right_atk_1.png'))
        self.attack_sprites_right.append(pygame.image.load('./public/zombie_models/zombie_right_atk_2.png'))
        self.attack_sprites_right.append(pygame.image.load('./public/zombie_models/zombie_right_atk_3.png'))
        self.attack_sprites_right.append(pygame.image.load('./public/zombie_models/zombie_right_atk_4.png'))
        self.current_attack_sprite = 0
        self.player_distance = 0
        self.attack_state = False

    def attack(self, screen, x_player, y_player):
        self.player_distance = (((self.pos_x - x_player) ** 2) + ((self.pos_y - y_player) ** 2)) ** (1/2)
        if self.player_distance <= 5:
            self.attack_state = True

        if self.enemy_rect.center[0] > x_player:
            self.enemy_image = self.attack_sprites_right[int(self.current_attack_sprite)]
        else:
            self.enemy_image = self.attack_sprites_right[int(self.current_attack_sprite)]

        self.attack_state += 0.02

        if self.current_attack_sprite == len(self.attack_sprites_right):
            self.current_attack_sprite = 0
            self.attack_state = False
            self.player_distance = (((self.pos_x - x_player) ** 2) + ((self.pos_y - y_player) ** 2)) ** (1 / 2)
        screen.blit(self.enemy_image, (self.pos_x, self.pos_y))
        self.enemy_rect = self.enemy_image.get_rect(topleft=(self.pos_x, self.pos_y))

    def spawn(self, screen, x_player, y_player):
        if not self.attack_state:
            # spawns the enemy outside the screen in a random place when instanced
            if not self.spawn_condition:
                x_inicial = randint(0, 1)
                y_inicial = randint(0, 1)
                if x_inicial:
                    self.pos_x = randint(self.x_tela, self.x_tela + 100)
                else:
                    self.pos_x = randint(-100, 0)
                if y_inicial:
                    self.pos_y = randint(self.y_tela, self.y_tela + 100)
                else:
                    self.pos_y = randint(-100, 0)
                self.spawn_condition = True
            else:
                # move the enemy towards the player
                ang = atan2(y_player - self.pos_y, x_player - self.pos_x)
                self.pos_x += self.velocidade * cos(ang)
                self.pos_y += self.velocidade * sin(ang)

            # alternates between two image every half second
            self.current_walking_sprite = int(pygame.time.get_ticks() / 500) % 2
            if self.enemy_rect.center[0] > x_player:
                self.enemy_image = self.sprites_right[int(self.current_walking_sprite)]
            else:
                self.enemy_image = self.sprites_left[int(self.current_walking_sprite)]

            self.player_distance = (((self.pos_x - x_player) ** 2) + ((self.pos_y - y_player) ** 2)) ** (1 / 2)
            if self.player_distance <= 5:
                self.attack_state = True

            # display the result
            screen.blit(self.enemy_image, (self.pos_x, self.pos_y))
            self.enemy_rect = self.enemy_image.get_rect(topleft=(self.pos_x, self.pos_y))

    def estado(self, bullet_rect):
        if self.enemy_rect.colliderect(bullet_rect):
            self.kill()


if __name__ == '__main__':
    pygame.init()
    tela = pygame.display.set_mode((1080, 1080))
    pygame.display.set_caption(f'jogu')
    clock = pygame.time.Clock()
    p1 = Player()

    bullet_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    for i in range(5):
        p2 = Inimigo(1, 1080, 1080)
        enemy_group.add(p2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                bullet_group.add(p1.create_bullet())

        tela.fill((48, 10, 36))
        for inimigo in enemy_group.sprites():
            inimigo.spawn(tela, p1.pos_x, p1.pos_y)
        bullet_group.draw(tela)
        bullet_group.update()
        for inimigo in enemy_group.sprites():
            for bullet in bullet_group.sprites():
                inimigo.estado(bullet.rect)
        p1.movimentar(tela)
        pygame.display.update()
        clock.tick(60)

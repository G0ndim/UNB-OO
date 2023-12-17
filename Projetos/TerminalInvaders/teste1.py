import pygame
from math import atan2, cos, sin
from random import randint


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.player_health = 5
        self.pos_x = 540
        self.pos_y = 540
        self.weapons = [0, Pistol(), Shotguun(), Sniper()]
        self.weapon_number = 1
        self.player_skin = './public/player_test.png'
        self.player_image = pygame.image.load(self.player_skin)
        self.player_rect = self.player_image.get_rect()
        self.velocidade = 3
        self.invulnerabilidade = 0

    def change_weapon(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_2]:
            self.weapon_number = 1
        if keys[pygame.K_3]:
            self.weapon_number = 2
        if keys[pygame.K_4]:
            self.weapon_number = 3

    def movimentar(self):
        # Movimento do jogador na tela
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.pos_y > 0:
            self.pos_y -= self.velocidade
        if keys[pygame.K_s] and self.pos_y < 1080 - self.player_rect.height:
            self.pos_y += self.velocidade
        if keys[pygame.K_a] and self.pos_x > 0:
            self.pos_x -= self.velocidade
        if keys[pygame.K_d] and self.pos_x < 1080 - self.player_rect.width:
            self.pos_x += self.velocidade

    def direction_animation(self):
        # Movimento do personagem na direcao do mouse
        mouse_pos = pygame.mouse.get_pos()
        weapons = [0, self.weapons[1].skin, self.weapons[2].skin, self.weapons[3].skin]
        if self.player_rect.topleft[0] <= mouse_pos[0] <= self.player_rect.topright[0]:
            if mouse_pos[1] <= self.pos_y:
                self.player_skin = weapons[self.weapon_number][0]
                self.player_image = pygame.image.load(self.player_skin)
            if mouse_pos[1] >= self.pos_y:
                self.player_skin = weapons[self.weapon_number][1]
                self.player_image = pygame.image.load(self.player_skin)
        elif mouse_pos[0] < self.player_rect.topleft[0]:
            if mouse_pos[1] <= self.player_rect.topleft[1]:
                self.player_skin = weapons[self.weapon_number][2]
                self.player_image = pygame.image.load(self.player_skin)
            if mouse_pos[1] >= self.player_rect.bottomleft[1]:
                self.player_skin = weapons[self.weapon_number][3]
                self.player_image = pygame.image.load(self.player_skin)
            if self.player_rect.bottomleft[1] >= mouse_pos[1] >= self.player_rect.topleft[1]:
                self.player_skin = weapons[self.weapon_number][4]
                self.player_image = pygame.image.load(self.player_skin)
        elif mouse_pos[0] > self.player_rect.topright[0]:
            if mouse_pos[1] < self.player_rect.topright[1]:
                self.player_skin = weapons[self.weapon_number][5]
                self.player_image = pygame.image.load(self.player_skin)
            if mouse_pos[1] > self.player_rect.bottomright[1]:
                self.player_skin = weapons[self.weapon_number][6]
                self.player_image = pygame.image.load(self.player_skin)
            if self.player_rect.bottomright[1] >= mouse_pos[1] >= self.player_rect.topright[1]:
                self.player_skin = weapons[self.weapon_number][7]
                self.player_image = pygame.image.load(self.player_skin)

    def update(self, tela):
        self.movimentar()
        self.change_weapon()
        self.direction_animation()
        tela.blit(self.player_image, (self.pos_x, self.pos_y))
        self.player_rect = self.player_image.get_rect(topleft=(self.pos_x, self.pos_y))

    def atacar(self, timer_event):
        self.weapons[self.weapon_number].atirar(self.player_rect.center[0], self.player_rect.center[1], timer_event)

    def levar_dano(self, dano):
        if not self.invulnerabilidade:
            self.player_health -= dano
        if self.player_health <= 0:
            print('a')


class Arma():
    def __init__(self):
        self.dano = int()
        self.velocidade = int()
        self.tempo_disparo = 1000
        self.skin = list()
        self.bullet_group = pygame.sprite.Group()

    def create_bullet(self, player_pos_x, player_pos_y):
        return Bullet(player_pos_x, player_pos_y)

    def atirar(self, player_pos_x, player_pos_y, timer_event):
        if event.type == timer_event:
            self.bullet_group.add(self.create_bullet(player_pos_x, player_pos_y))

    def bullet_update(self, tela):
        self.bullet_group.draw(tela)
        self.bullet_group.update()


class Pistol(Arma):
    def __init__(self):
        super().__init__()
        self.skin = ['./public/player/player_top_pistol.png',
                     './public/player/player_bottom_pistol.png',
                     './public/player/player_top_left_pistol.png',
                     './public/player/player_bottom_left_pistol.png',
                     './public/player/player_left_pistol.png',
                     './public/player/player_top_right_pistol.png',
                     './public/player/player_bottom_right_pistol.png',
                     './public/player/player_right_pistol.png']


class Shotguun(Arma):
    def __init__(self):
        super().__init__()
        self.skin = ['./public/player/player_top_shotgun.png',
                     './public/player/player_bottom_shotgun.png',
                     './public/player/player_top_left_shotgun.png',
                     './public/player/player_bottom_left_shotgun.png',
                     './public/player/player_left_shotgun.png',
                     './public/player/player_top_right_shotgun.png',
                     './public/player/player_bottom_right_shotgun.png',
                     './public/player/player_right_shotgun.png']


class Sniper(Arma):
    def __init__(self):
        super().__init__()
        self.skin = ['./public/player/player_top_sniper.png',
                     './public/player/player_bottom_sniper.png',
                     './public/player/player_top_left_sniper.png',
                     './public/player/player_bottom_left_sniper.png',
                     './public/player/player_left_sniper.png',
                     './public/player/player_top_right_sniper.png',
                     './public/player/player_bottom_right_sniper.png',
                     './public/player/player_right_sniper.png']


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
        self.vida = 3
        self.velocidade = velocidade
        self.pos_x = int()
        self.pos_y = int()
        self.dano = 1
        self.enemy_skin = './public/enemy_error.png'
        self.enemy_image = pygame.image.load(self.enemy_skin)
        self.enemy_rect = self.enemy_image.get_rect()
        self.spawn_condition = False
        self.x_tela = x_tela
        self.y_tela = y_tela
        self.sprites_left = [pygame.image.load('./public/zombie_models/zombie_left_walking_1.png'),
                             pygame.image.load('./public/zombie_models/zombie_left_walking_2.png')]
        self.sprites_right = [pygame.image.load('./public/zombie_models/zombie_right_walking_1.png'),
                              pygame.image.load('./public/zombie_models/zombie_right_walking_2.png')]
        self.current_walking_sprite = 0
        self.player_distance = int()

    def movement(self, x_player, y_player):
        # move the enemy towards the player
        ang = atan2(y_player - self.pos_y, x_player - self.pos_x)
        self.pos_x += self.velocidade * cos(ang)
        self.pos_y += self.velocidade * sin(ang)

    def spawn(self, x_player, y_player):
        # spawns the enemy outside the screen in a random place when instanced
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

    def walking_animation(self, x_player):
        # alternates between two image every half second
        self.current_walking_sprite = int(pygame.time.get_ticks() / 500) % 2
        if self.enemy_rect.center[0] > x_player:
            self.enemy_image = self.sprites_right[int(self.current_walking_sprite)]
        else:
            self.enemy_image = self.sprites_left[int(self.current_walking_sprite)]

    def update(self, screen, x_player, y_player):

        if not self.spawn_condition:
            self.spawn(x_player, y_player)
        else:
            self.movement(x_player, y_player)

        self.walking_animation(x_player)

        self.player_distance = (((self.pos_x - x_player) ** 2) + ((self.pos_y - y_player) ** 2)) ** (1 / 2)

        screen.blit(self.enemy_image, (self.pos_x, self.pos_y))
        self.enemy_rect = self.enemy_image.get_rect(topleft=(self.pos_x, self.pos_y))

    def estado(self, bullet_rect):
        flag = 0
        if self.enemy_rect.colliderect(bullet_rect):
            self.vida -= 1
            flag += 1
        if self.vida <= 0:
            self.kill()
        return flag

    def attack(self, player):
        if self.enemy_rect.colliderect(player.player_rect):
            player.levar_dano(self.dano)


if __name__ == '__main__':
    pygame.init()
    tela = pygame.display.set_mode((1080, 1080))
    pygame.display.set_caption(f'jogu')
    clock = pygame.time.Clock()
    p1 = Player()
    timer_event = pygame.USEREVENT + 1
    timer_interval = 1000
    pygame.time.set_timer(timer_event, timer_interval)

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
            p1.atacar(timer_event)

        tela.fill((48, 10, 36))

        for inimigo in enemy_group.sprites():
            inimigo.update(tela, p1.pos_x, p1.pos_y)

        p1.weapons[p1.weapon_number].bullet_update(tela)

        for inimigo in enemy_group.sprites():
            inimigo.attack(p1)
            for bullet in p1.weapons[p1.weapon_number].bullet_group.sprites():
                inimigo.estado(bullet.rect)
                if inimigo.estado(bullet.rect) >= 1:
                    bullet.kill()

        p1.update(tela)

        pygame.display.update()
        clock.tick(60)

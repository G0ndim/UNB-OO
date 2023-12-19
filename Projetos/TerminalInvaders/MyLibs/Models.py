import pygame
from math import atan2, cos, sin
from random import randint, uniform


class Player(pygame.sprite.Sprite):
    def __init__(self, x_tela, y_tela, vida, velocidade, w1_d, w2_d, w3_d, w2_c, w3_c):
        super().__init__()
        self.player_health = vida
        self.velocidade = velocidade
        self.pos_x = x_tela / 2
        self.pos_y = y_tela / 2
        self.weapons = [Pistol(w1_d), Shotgun(w2_d), Sniper(w3_d)]
        self.weapon_number = 0
        self.player_skin = '../public/player_test.png'
        self.player_image = pygame.image.load(self.player_skin)
        self.player_rect = self.player_image.get_rect()
        self.invulnerabilidade = 0
        self.inv_flag = 0
        self.death_flag = False
        self.shotgun_condition = w2_c
        self.sniper_condition = w3_c
        self.x_tela = x_tela
        self.y_tela = y_tela
        self.health_bar = pygame.Surface((self.player_health, 9))
        self.health_bar.fill((255, 0, 0))
        self.weapon_images = [pygame.image.load('../public/pistol.png'),
                              pygame.image.load('../public/shotgun.png'),
                              pygame.image.load('../public/sniper.png')]

    def change_weapon(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            self.weapon_number = 0
        if keys[pygame.K_2] and self.shotgun_condition:
            self.weapon_number = 1
        if keys[pygame.K_3] and self.sniper_condition:
            self.weapon_number = 2

    def movimentar(self):
        # Movimento do jogador na tela
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.pos_y > 0:
            self.pos_y -= self.velocidade
        if keys[pygame.K_s] and self.pos_y < self.y_tela - self.player_rect.height:
            self.pos_y += self.velocidade
        if keys[pygame.K_a] and self.pos_x > 0:
            self.pos_x -= self.velocidade
        if keys[pygame.K_d] and self.pos_x < self.x_tela - self.player_rect.width:
            self.pos_x += self.velocidade

    def direction_animation(self):
        # Movimento do personagem na direcao do mouse
        mouse_pos = pygame.mouse.get_pos()
        weapons = [self.weapons[0].skin, self.weapons[1].skin, self.weapons[2].skin]
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
        self.player_image = pygame.transform.scale(self.player_image, (self.player_image.get_width() / 1.5,
                                                                       self.player_image.get_height() / 1.5))
        self.update_ui(tela)
        tela.blit(self.player_image, (self.pos_x, self.pos_y))
        self.player_rect = self.player_image.get_rect(topleft=(self.pos_x, self.pos_y))

    def atacar(self, timer_event, event):
        self.weapons[self.weapon_number].atirar(self.player_rect.center[0], self.player_rect.center[1], timer_event, event)

    def invulneravel(self, timer_event, timer_interval):
        if not self.inv_flag:
            pygame.time.set_timer(timer_event, timer_interval)
            self.inv_flag = 1

    def levar_dano(self, dano, timer_event, timer_interval):
        if not self.invulnerabilidade:
            self.player_health -= dano
            self.invulnerabilidade = True
            # print(self.player_health)
            pygame.time.set_timer(timer_event, timer_interval, 1)
        if self.player_health <= 0:
            self.death_flag = True
            # print('Morto')

    def update_ui(self, tela):
        if self.player_health >= 0:
            self.health_bar = pygame.Surface((self.player_health, 9))
            self.health_bar.fill((255, 0, 0))
            tela.blit(self.health_bar, (6, 6))
            tela.blit(self.weapon_images[self.weapon_number], (6, 21))
            font = pygame.font.SysFont(None, 18)
            tela.blit(font.render(f'{self.player_health}', True, (255, 0, 0)), (self.player_health + 12, 6))


class Arma:
    def __init__(self, dano):
        self.dano = dano
        self.velocidade = int()
        self.skin = list()
        self.bullet_group = pygame.sprite.Group()
        self.range = int()

    def create_bullet(self, player_pos_x, player_pos_y):
        return Bullet(player_pos_x, player_pos_y, 0)

    def atirar(self, player_pos_x, player_pos_y, timer_event, event):
        if event.type == timer_event:
            self.bullet_group.add(self.create_bullet(player_pos_x, player_pos_y))

    def bullet_update(self, tela):
        self.bullet_group.draw(tela)
        self.bullet_group.update(self.velocidade, self.range)


class Pistol(Arma):
    def __init__(self, dano):
        super().__init__(dano)
        self.skin = ['../public/player/player_top_pistol.png',
                     '../public/player/player_bottom_pistol.png',
                     '../public/player/player_top_left_pistol.png',
                     '../public/player/player_bottom_left_pistol.png',
                     '../public/player/player_left_pistol.png',
                     '../public/player/player_top_right_pistol.png',
                     '../public/player/player_bottom_right_pistol.png',
                     '../public/player/player_right_pistol.png']
        # self.dano = 2
        self.velocidade = 5
        self.range = 100


class Shotgun(Arma):
    def __init__(self, dano):
        super().__init__(dano)
        self.skin = ['../public/player/player_top_shotgun.png',
                     '../public/player/player_bottom_shotgun.png',
                     '../public/player/player_top_left_shotgun.png',
                     '../public/player/player_bottom_left_shotgun.png',
                     '../public/player/player_left_shotgun.png',
                     '../public/player/player_top_right_shotgun.png',
                     '../public/player/player_bottom_right_shotgun.png',
                     '../public/player/player_right_shotgun.png']
        self.ang = int()
        # self.dano = 1
        self.velocidade = 3
        self.range = 75

    def create_bullet(self, player_pos_x, player_pos_y, flag):
        mouse_pos = pygame.mouse.get_pos()
        self.ang = atan2(mouse_pos[1] - player_pos_y, mouse_pos[0] - player_pos_x)

        if flag == 1:
            bullet1 = Bullet(player_pos_x, player_pos_y, 0)
            return bullet1
        if flag == 2:
            bullet2 = Bullet(player_pos_x, player_pos_y, self.ang + 0.5)
            return bullet2
        if flag == 3:
            bullet3 = Bullet(player_pos_x, player_pos_y, self.ang - 0.5)
            return bullet3

    def atirar(self, player_pos_x, player_pos_y, timer_event, event):
        if event.type == timer_event:
            self.bullet_group.add(self.create_bullet(player_pos_x, player_pos_y, 1))
            self.bullet_group.add(self.create_bullet(player_pos_x, player_pos_y, 2))
            self.bullet_group.add(self.create_bullet(player_pos_x, player_pos_y, 3))


class Sniper(Arma):
    def __init__(self, dano):
        super().__init__(dano)
        self.skin = ['../public/player/player_top_sniper.png',
                     '../public/player/player_bottom_sniper.png',
                     '../public/player/player_top_left_sniper.png',
                     '../public/player/player_bottom_left_sniper.png',
                     '../public/player/player_left_sniper.png',
                     '../public/player/player_top_right_sniper.png',
                     '../public/player/player_bottom_right_sniper.png',
                     '../public/player/player_right_sniper.png']
        # self.dano = 9
        self.velocidade = 10
        self.range = 900


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, desvio_shotgun):
        super().__init__()
        self.image = pygame.Surface((3, 3))
        self.image.fill((255, 0, 0))
        self.pos_y = pos_y
        self.pos_x = pos_x
        self.rect = self.image.get_rect(center=(pos_x, pos_y))
        self.ang = int()
        self.mouse_pos = tuple()
        self.flag = False
        self.desvio_shotgun = desvio_shotgun

    def update(self, velocidade, range):
        if not self.flag:
            self.mouse_pos = pygame.mouse.get_pos()
            self.flag = True
        if self.desvio_shotgun == 0:
            self.ang = atan2(self.mouse_pos[1] - self.pos_y, self.mouse_pos[0] - self.pos_x)
        else:
            self.ang = self.desvio_shotgun
        self.rect.x += velocidade * cos(self.ang)
        self.rect.y += velocidade * sin(self.ang)

        if (self.rect.x >= self.pos_x + range or self.rect.x <= self.pos_x - range or
                self.rect.y >= self.pos_y + range or self.rect.y <= self.pos_y - range):
            self.kill()


class Fireball(Bullet):
    def __init__(self, pos_x, pos_y, player_x, player_y):
        super().__init__(pos_x, pos_y, 0)
        self.image = pygame.Surface((4, 4))
        self.image.fill((255, 32, 254))
        self.x_final = player_x
        self.y_final = player_y

    def update(self):
        self.ang = atan2(self.y_final - self.pos_y, self.x_final - self.pos_x)
        self.rect.x += 1.75 * cos(self.ang)
        self.rect.y += 1.75 * sin(self.ang)

        if self.rect.x >= 900 or self.rect.x <= 0 or self.rect.y >= 900 or self.rect.y <= 0:
            self.kill()


class Inimigo(pygame.sprite.Sprite):
    def __init__(self, x_tela, y_tela):
        super().__init__()
        self.vida = 5
        self.velocidade = float()
        self.pontuacao = 0
        self.pos_x = int()
        self.pos_y = int()
        self.dano = int()
        self.enemy_skin = '../public/enemy_error.png'
        self.enemy_image = pygame.image.load(self.enemy_skin)
        self.enemy_rect = self.enemy_image.get_rect()
        self.spawn_condition = False
        self.x_tela = x_tela
        self.y_tela = y_tela
        self.sprites_left = []
        self.sprites_right = []
        self.current_walking_sprite = 0
        self.player_distance = int()
        self.death_flag = False

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
            self.pos_x = randint(self.x_tela + 10, self.x_tela + 20)
        else:
            self.pos_x = randint(-20, -10)
        if y_inicial:
            self.pos_y = randint(self.y_tela + 10, self.y_tela + 20)
        else:
            self.pos_y = randint(-20, -10)
        self.spawn_condition = True

    def walking_animation(self, x_player):
        # alternates between two image every half second
        self.current_walking_sprite = int(pygame.time.get_ticks() / 500) % 2
        if self.enemy_rect.center[0] > x_player:
            self.enemy_image = self.sprites_right[int(self.current_walking_sprite)]
        else:
            self.enemy_image = self.sprites_left[int(self.current_walking_sprite)]

    def update(self, screen, x_player, y_player):
        if self.death_flag:
            self.kill()
        if not self.spawn_condition:
            self.spawn(x_player, y_player)
        else:
            self.movement(x_player, y_player)

        self.walking_animation(x_player)

        self.player_distance = (((self.pos_x - x_player) ** 2) + ((self.pos_y - y_player) ** 2)) ** (1 / 2)

        screen.blit(self.enemy_image, (self.pos_x, self.pos_y))
        self.enemy_rect = self.enemy_image.get_rect(topleft=(self.pos_x, self.pos_y))

    def estado(self, bullet, dano_recebido):
        if self.enemy_rect.colliderect(bullet.rect):
            self.vida -= dano_recebido
            bullet.kill()
        if self.vida <= 0:
            if not self.death_flag:
                self.death_flag = True
                return self.pontuacao

    def attack(self, player, timer_event, timer_interval):
        if self.enemy_rect.colliderect(player.player_rect):
            player.levar_dano(self.dano, timer_event, timer_interval)


class Zombie(Inimigo):
    def __init__(self, x_tela, y_tela):
        super().__init__(x_tela, y_tela)
        self.sprites_left = [pygame.image.load('../public/zombie_models/zombie_left_walking_1.png'),
                             pygame.image.load('../public/zombie_models/zombie_left_walking_2.png')]
        self.sprites_right = [pygame.image.load('../public/zombie_models/zombie_right_walking_1.png'),
                              pygame.image.load('../public/zombie_models/zombie_right_walking_2.png')]
        self.vida = 100
        self.dano = 20
        self.velocidade = uniform(0.4, 0.5)
        self.pontuacao = 100


class Bat(Inimigo):
    def __init__(self, x_tela, y_tela):
        super().__init__(x_tela, y_tela)
        self.sprites_left = [pygame.image.load('../public/Bat/bat_1.png'),
                             pygame.image.load('../public/Bat/bat_2.png')]
        self.sprites_right = [pygame.image.load('../public/Bat/bat_1.png'),
                              pygame.image.load('../public/Bat/bat_2.png')]
        self.vida = 50
        self.dano = 10
        self.velocidade = uniform(0.6, 0.7)
        self.pontuacao = 50


class Mage(Inimigo):
    def __init__(self, x_tela, y_tela):
        super().__init__(x_tela, y_tela)
        self.sprites_left = [pygame.image.load('../public/Mage/mage_walking_right_1.png'),
                             pygame.image.load('../public/Mage/mage_walking_right_2.png')]
        self.sprites_right = [pygame.image.load('../public/Mage/mage_walking_left_1.png'),
                              pygame.image.load('../public/Mage/mage_walking_left_2.png')]
        self.attack_sprites_left = [pygame.image.load('../public/Mage/mage_attack_right_1.png'),
                                    pygame.image.load('../public/Mage/mage_attack_right_3.png')]
        self.attack_sprites_right = [pygame.image.load('../public/Mage/mage_attack_left_1.png'),
                                     pygame.image.load('../public/Mage/mage_attack_left_3.png')]
        self.current_attack_sprite = 0
        self.dano = 10
        self.vida = 150
        self.velocidade = 0.4
        self.x_final = int()
        self.y_final = int()
        self.attack_condition = False
        self.fireball_group = pygame.sprite.Group()
        self.pontuacao = 150

    def spawn(self, x_player, y_player):
        # spawns the enemy outside the screen in a random place when instanced
        x_inicial = randint(0, 1)
        y_inicial = randint(0, 1)
        if x_inicial:
            self.pos_x = randint(self.x_tela + 10, self.x_tela + 20)
            self.x_final = randint(self.pos_x - 200, self.pos_x - 120)
        else:
            self.pos_x = randint(-20, -10)
            self.x_final = randint(self.pos_x + 120, self.pos_x + 300)
        if y_inicial:
            self.pos_y = randint(self.y_tela + 10, self.y_tela + 20)
            self.y_final = randint(self.pos_y - 200, self.pos_y - 120)
        else:
            self.pos_y = randint(-20, -10)
            self.y_final = randint(self.pos_y + 120, self.pos_y + 200)

        self.spawn_condition = True

    def attack_animation(self, x_player):
        # alternates between two image every half second
        self.current_attack_sprite = int(pygame.time.get_ticks() / 500) % 2
        if self.enemy_rect.center[0] > x_player:
            self.enemy_image = self.attack_sprites_right[int(self.current_attack_sprite)]
        else:
            self.enemy_image = self.attack_sprites_left[int(self.current_attack_sprite)]

    def movement(self, x_player, y_player):
        # move the mage towards a random place on the screen
        if not self.attack_condition:
            ang = atan2(self.y_final - self.pos_y, self.x_final - self.pos_x)
            self.pos_x += self.velocidade * cos(ang)
            self.pos_y += self.velocidade * sin(ang)
        if ((int(self.pos_x) == self.x_final or int(self.pos_x) == self.x_final + 1
             or int(self.pos_x) == self.x_final - 1) and (int(self.pos_y) == self.y_final or
                                                          int(self.pos_y) == self.y_final - 1 or
                                                          int(self.pos_y) == self.y_final + 1)):
            self.attack_condition = True

    def update(self, screen, x_player, y_player):
        if self.death_flag:
            self.kill()
        if not self.attack_condition:
            if not self.spawn_condition:
                self.spawn(x_player, y_player)
            else:
                self.movement(x_player, y_player)

            self.walking_animation(x_player)
        else:
            self.attack_animation(x_player)

        self.player_distance = (((self.pos_x - x_player) ** 2) + ((self.pos_y - y_player) ** 2)) ** (1 / 2)

        screen.blit(self.enemy_image, (self.pos_x, self.pos_y))
        self.enemy_rect = self.enemy_image.get_rect(topleft=(self.pos_x, self.pos_y))

    def create_fireball(self, player_x, player_y):
        return Fireball(self.pos_x, self.pos_y, player_x, player_y)

    def fireball_attack(self, player_x, player_y, timer_event, event):
        if self.attack_condition:
            if event.type == timer_event:
                self.fireball_group.add(self.create_fireball(player_x, player_y))

    def fireball_update(self, tela):
        self.fireball_group.draw(tela)
        self.fireball_group.update()

    def attack(self, player, timer_event, timer_interval):
        for spell in self.fireball_group.sprites():
            if spell.rect.colliderect(player.player_rect):
                player.levar_dano(self.dano, timer_event, timer_interval)
                spell.kill()


class Slime(Inimigo):
    def __init__(self, x_tela, y_tela, x_inicial, y_inicial):
        super().__init__(x_tela, y_tela)
        self.sprites_left = [pygame.image.load('../public/King_Slime/slime_1.png'),
                             pygame.image.load('../public/King_Slime/slime_2.png')]
        self.sprites_right = [pygame.image.load('../public/King_Slime/slime_1.png'),
                              pygame.image.load('../public/King_Slime/slime_2.png')]
        self.dano = 15
        self.velocidade = uniform(0.3, 0.8)
        self.vida = 75
        self.x_inicial = x_inicial
        self.y_inicial = y_inicial
        self.pontuacao = 75

    def spawn(self, x_player, y_player):
        self.pos_x = self.x_inicial
        self.pos_y = self.y_inicial
        self.spawn_condition = True


class KingSlime(Inimigo):
    def __init__(self, x_tela, y_tela):
        super().__init__(x_tela, y_tela)
        self.sprites_left = [pygame.image.load('../public/King_Slime/king_slime_1.png'),
                             pygame.image.load('../public/King_Slime/king_slime_2.png')]
        self.sprites_right = [pygame.image.load('../public/King_Slime/king_slime_1.png'),
                              pygame.image.load('../public/King_Slime/king_slime_2.png')]
        self.dano = 50
        self.velocidade = uniform(0.3, 0.4)
        self.vida = 300
        self.x_death = int()
        self.y_death = int()

    def estado(self, bullet, dano_recebido):
        if self.enemy_rect.colliderect(bullet.rect):
            self.vida -= dano_recebido
            bullet.kill()
        if self.vida <= 0:
            if not self.death_flag:
                self.death_flag = True
                return (self.pos_x, self.pos_y)

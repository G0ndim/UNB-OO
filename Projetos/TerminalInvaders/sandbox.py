import pygame
from math import atan2, cos, sin

pygame.init()
tela = pygame.display.set_mode((1080, 1080))
pygame.display.set_caption(f'jogo')  # nome da janela
clock = pygame.time.Clock()  # tempo do jogo
test_surface = pygame.Surface((100, 200))  # algo para botar na tela

# jogador = pg.image.load(player.player_skin)
jogador = pygame.image.load('./public/mario_sprite.png').convert_alpha()
jogador = pygame.transform.scale(jogador, (71, 97))
x = 20
y = 20
jogador_rect = jogador.get_rect()

#############################################################################

enemy = pygame.image.load('./public/zombie.png').convert_alpha()
enemy = pygame.transform.scale(enemy, (71, 97))
enemy_rect = enemy.get_rect()
x_inimigo = 40
y_inimigo = 40

###############################################################################

bola_fogo = pygame.image.load(('./public/bola.png')).convert_alpha()
bola_fogo = pygame.transform.scale(bola_fogo, (20, 20))
bola_rect = bola_fogo.get_rect()


while True:
    tela.fill('white')
    keys = pygame.key.get_pressed()
    speed = 15

    x_bola = x
    y_bola = y

    if keys[pygame.K_w] and y > 0:
        y -= speed
    if keys[pygame.K_s] and y < 1080 - jogador_rect.height:
        y += speed
    if keys[pygame.K_a] and x > 0:
        x -= speed
    if keys[pygame.K_d] and x < 1080 - jogador_rect.width:
        x += speed

    ang = atan2(y - y_inimigo, x - x_inimigo)

    x_inimigo += 5 * cos(ang)
    y_inimigo += 5 * sin(ang)

    if pygame.mouse.get_pressed()[0]:
        mouse_pos = pygame.mouse.get_pos()
        print(mouse_pos)

    jogador_rect = jogador.get_rect(topleft=(x, y))
    enemy_rect = enemy.get_rect(topleft=(x_inimigo, y_inimigo))

    tela.blit(jogador, (x, y))
    tela.blit(enemy, (x_inimigo, y_inimigo))
    tela.blit(bola_fogo, (x_bola, y_bola))

    if jogador_rect.colliderect(enemy_rect):
        print("colisao")

    pygame.display.update()
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

"""
import pygame
from math import atan2, cos, sin


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.pos_x = 0
        self.pos_y = 0
        self.player_image = pygame.image.load('./public/player/player_left_pistol.png')
        self.player_rect = self.player_image.get_rect()
        self.velocidade = 5

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
        return Bullet(self.pos_x, self.pos_y)


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


if __name__ == '__main__':
    pygame.init()
    tela = pygame.display.set_mode((1080, 1080))
    pygame.display.set_caption(f'jogu')
    clock = pygame.time.Clock()
    p1 = Player()
    bullet_group = pygame.sprite.Group()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                bullet_group.add(p1.create_bullet())

        tela.fill((48, 10, 36))
        p1.movimentar(tela)
        bullet_group.draw(tela)
        bullet_group.update()
        pygame.display.update()
        clock.tick(60)



"""


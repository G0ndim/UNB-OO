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


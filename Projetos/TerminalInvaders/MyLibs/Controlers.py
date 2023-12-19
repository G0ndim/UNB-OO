import pygame
from Models import *


class Round:
    def __init__(self, player, enemys, x_tela, y_tela):
        self.grupo_zumbis = pygame.sprite.Group()
        self.grupo_morcegos = pygame.sprite.Group()
        self.grupo_magos = pygame.sprite.Group()
        self.grupo_slime_king = pygame.sprite.Group()
        self.grupo_slime = pygame.sprite.Group()
        self.player = Player(x_tela, y_tela, player[0], player[1], player[2], player[3], player[4], player[5], player[6])
        self.enemy_list = enemys
        self.x_tela = x_tela
        self.y_tela = y_tela
        self.bullet_group = pygame.sprite.Group()
        self.condicao_vitoria = False
        self.condicao_derrota = False

    def config_enemys(self):
        for zombie_number in range(self.enemy_list[0]):
            zumbi = Zombie(self.x_tela, self.y_tela)
            self.grupo_zumbis.add(zumbi)
        for bat_number in range(self.enemy_list[1]):
            morcego = Bat(self.x_tela, self.y_tela)
            self.grupo_morcegos.add(morcego)
        for mage_number in range(self.enemy_list[2]):
            mago = Mage(self.x_tela, self.y_tela)
            self.grupo_magos.add(mago)
        for king_slime_number in range(self.enemy_list[3]):
            king_slime = KingSlime(self.x_tela, self.y_tela)
            self.grupo_slime_king.add(king_slime)

    def condicao_round(self):
        if self.player.death_flag:
            self.condicao_derrota = True
        if (len(self.grupo_zumbis.sprites()) == 0 and len(self.grupo_morcegos.sprites()) == 0 and
                len(self.grupo_magos.sprites()) == 0 and len(self.grupo_slime_king.sprites()) == 0):
            self.condicao_vitoria = True


if __name__ == '__main__':
    pygame.init()
    x_tela = 600
    y_tela = 600
    tela = pygame.display.set_mode((x_tela, y_tela))
    pygame.display.set_caption(f'jogu')
    clock = pygame.time.Clock()
    player_health = 120
    player_velocity = 0.75
    player = [player_health, player_velocity, 20, 10, 90, True, True]
    enemys1 = [1, 1, 1, 1, 0]
    round1 = Round(player, enemys1, x_tela, y_tela)
    pontuacao = 0
    timer_event = pygame.USEREVENT + 1
    timer_interval = 1000
    timer_event2 = pygame.USEREVENT + 2
    timer_interval2 = 600

    pygame.time.set_timer(timer_event, timer_interval)

    round1.config_enemys()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            round1.player.atacar(timer_event, event)

            for enemy_mage in round1.grupo_magos.sprites():
                enemy_mage.fireball_attack(round1.player.pos_x, round1.player.pos_y, timer_event, event)

            if event.type == timer_event2:
                round1.player.invulnerabilidade = False

        horda = [round1.grupo_zumbis.sprites(),
                 round1.grupo_morcegos.sprites(),
                 round1.grupo_magos.sprites(),
                 round1.grupo_slime_king.sprites(),
                 round1.grupo_slime.sprites()]

        tela.fill((48, 10, 36))  # Cor de Fundo da Tela

        for enemy_type in horda:
            for inimigo in enemy_type:
                inimigo.update(tela, round1.player.pos_x, round1.player.pos_y)

        round1.player.weapons[round1.player.weapon_number].bullet_update(tela)

        for enemy_mage in round1.grupo_magos.sprites():
            enemy_mage.fireball_update(tela)

        for enemy_type in horda:
            for inimigo in enemy_type:
                inimigo.attack(round1.player, timer_event2, timer_interval2)
                for bullet in round1.player.weapons[round1.player.weapon_number].bullet_group.sprites():
                    i = inimigo.estado(bullet, round1.player.weapons[round1.player.weapon_number].dano)
                    if isinstance(i, tuple):
                        round1.grupo_slime.add(Slime(x_tela, y_tela, i[0], i[1]))
                        round1.grupo_slime.add(Slime(x_tela, y_tela, i[0] + 9, i[1] + 30))
                        round1.grupo_slime.add(Slime(x_tela, y_tela, i[0] + 14, i[1] - 30))
                    elif isinstance(i, int):
                        pontuacao += i
                        print(pontuacao)
                    i = 0

        font = pygame.font.SysFont(None, 18)
        tela.blit(font.render(f'{pontuacao}', True, (255, 255, 255)), (x_tela - 50, 6))

        round1.player.update(tela)

        pygame.display.update()
        clock.tick(60)

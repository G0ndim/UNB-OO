import pygame
import asyncio
import sys
import json
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
            print('Derrota')
        if (len(self.grupo_zumbis.sprites()) == 0 and len(self.grupo_morcegos.sprites()) == 0 and
                len(self.grupo_magos.sprites()) == 0 and len(self.grupo_slime_king.sprites()) == 0):
            self.condicao_vitoria = True
            print('vitoria')


class Arena:
    def __init__(self, player, enemys, x_tela, y_tela, pontuacao):
        self.round1 = Round(player, enemys, x_tela, y_tela)
        self.pontuacao = pontuacao
        self.x_tela = x_tela
        self.y_tela = y_tela
        self.count = 0

    def play(self):
        pygame.init()
        tela = pygame.display.set_mode((self.x_tela, self.y_tela))
        pygame.display.set_caption(f'Terminal Invaders')
        clock = pygame.time.Clock()
        timer_event = pygame.USEREVENT + 1
        timer_interval = 1000
        timer_event2 = pygame.USEREVENT + 2
        timer_interval2 = 600

        pygame.time.set_timer(timer_event, timer_interval)

        self.round1.config_enemys()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                self.round1.player.atacar(timer_event, event)

                for enemy_mage in self.round1.grupo_magos.sprites():
                    enemy_mage.fireball_attack(self.round1.player.pos_x, self.round1.player.pos_y, timer_event, event)

                if event.type == timer_event2:
                    self.round1.player.invulnerabilidade = False

            horda = [self.round1.grupo_zumbis.sprites(),
                     self.round1.grupo_morcegos.sprites(),
                     self.round1.grupo_magos.sprites(),
                     self.round1.grupo_slime_king.sprites(),
                     self.round1.grupo_slime.sprites()]

            tela.fill((48, 10, 36))  # Cor de Fundo da Tela

            for enemy_type in horda:
                for inimigo in enemy_type:
                    inimigo.update(tela, self.round1.player.pos_x, self.round1.player.pos_y)

            self.round1.player.weapons[self.round1.player.weapon_number].bullet_update(tela)

            for enemy_mage in self.round1.grupo_magos.sprites():
                enemy_mage.fireball_update(tela)

            if pygame.time.get_ticks() >= 500:
                for enemy_type in horda:
                    for inimigo in enemy_type:
                        inimigo.attack(self.round1.player, timer_event2, timer_interval2)
                        for bullet in self.round1.player.weapons[self.round1.player.weapon_number].bullet_group.sprites():
                            self.count = inimigo.estado(bullet, self.round1.player.weapons[self.round1.player.weapon_number].dano)
                            if isinstance(self.count, tuple):
                                self.round1.grupo_slime.add(Slime(self.x_tela, self.y_tela, self.count[0], self.count[1]))
                                self.round1.grupo_slime.add(Slime(self.x_tela, self.y_tela, self.count[0] + 9, self.count[1] + 30))
                                self.round1.grupo_slime.add(Slime(self.x_tela, self.y_tela, self.count[0] + 14, self.count[1] - 30))
                            elif isinstance(self.count, int):
                                self.pontuacao += self.count
                            self.count = 0

            font = pygame.font.SysFont(None, 18)
            tela.blit(font.render(f'{self.pontuacao}', True, (255, 255, 255)), (self.x_tela - 50, 6))

            self.round1.condicao_round()
            self.round1.player.update(tela)

            if self.round1.condicao_vitoria:
                return (self.pontuacao, self.round1.player.player_health)
            elif self.round1.condicao_derrota:
                return self.pontuacao

            pygame.display.update()
            clock.tick(120)


class Upgrade:
    def __init__(self, p, screen_resolution):
        self.player_health = p[0]
        self.player_velocity = p[1]
        self.pistol_damage = p[2]
        self.shotgun_damage = p[3]
        self.sniper_damage = p[4]
        self.shotgun_condition = p[5]
        self.sniper_condition = p[6]
        self.screen_resolution = screen_resolution
        self.upgrade_health_image = pygame.image.load('../public/upgrade_HEALTH.jpeg')
        self.health_rect = self.upgrade_health_image.get_rect(topleft=(24, 180))
        self.upgrade_velocity_image = pygame.image.load('../public/upgrade_SPEED.jpeg')
        self.velocity_rect = self.upgrade_velocity_image.get_rect(topleft=(312, 180))
        self.upgrade_screen_image = pygame.image.load('../public/upgrade_SCREEN.jpeg')
        self.screen_rect = self.upgrade_screen_image.get_rect(topleft=(456, 180))
        self.upgrade_damage_image = pygame.image.load('../public/upgrade_DAMAGE.jpeg')
        self.damage_rect = self.upgrade_damage_image.get_rect(topleft=(168, 180))

    def update_parameters(self):
        tela = pygame.display.set_mode((600, 400))
        pygame.display.set_caption(f'UPGRADE')
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            mouse_x, mouse_y = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            tela.fill((48, 10, 36))  # Cor de Fundo da Tela

            font = pygame.font.SysFont(None, 30)
            tela.blit(font.render(f'ESCOLHA UM UPGRADE', True, (0, 255, 1)), (165, 60))

            tela.blit(self.upgrade_health_image, (24, 180))
            tela.blit(self.upgrade_damage_image, (168, 180))
            tela.blit(self.upgrade_velocity_image, (312, 180))
            tela.blit(self.upgrade_screen_image, (456, 180))

            if self.health_rect.collidepoint(mouse_x, mouse_y):
                if mouse_pressed[0]:
                    print('a')
                    return ([self.player_health + 25, self.player_velocity,
                             self.pistol_damage, self.shotgun_damage, self.sniper_damage,
                             self.shotgun_condition, self.sniper_condition], self.screen_resolution)
            elif self.damage_rect.collidepoint(mouse_x, mouse_y):
                if mouse_pressed[0]:
                    print('b')
                    if self.shotgun_condition and not self.sniper_condition:
                        return ([self.player_health, self.player_velocity,
                                 self.pistol_damage, self.shotgun_damage + 5, self.sniper_damage,
                                 self.shotgun_condition, self.sniper_condition], self.screen_resolution)
                    elif self.sniper_condition:
                        return ([self.player_health, self.player_velocity,
                                 self.pistol_damage, self.shotgun_damage, self.sniper_damage + 5,
                                 self.shotgun_condition, self.sniper_condition], self.screen_resolution)
                    else:
                        return ([self.player_health, self.player_velocity,
                                self.pistol_damage + 5, self.shotgun_damage, self.sniper_damage,
                                self.shotgun_condition, self.sniper_condition], self.screen_resolution)
            elif self.velocity_rect.collidepoint(mouse_x, mouse_y):
                if mouse_pressed[0]:
                    print('c')
                    return ([self.player_health, self.player_velocity + 0.2,
                             self.pistol_damage, self.shotgun_damage, self.sniper_damage,
                             self.shotgun_condition, self.sniper_condition], self.screen_resolution)
            elif self.screen_rect.collidepoint(mouse_x, mouse_y):
                if mouse_pressed[0]:
                    print('d')
                    return ([self.player_health, self.player_velocity,
                             self.pistol_damage, self.shotgun_damage, self.sniper_damage,
                             self.shotgun_condition, self.sniper_condition], self.screen_resolution + 50)

            pygame.display.update()
            clock.tick(120)


class GameOver:
    def __init__(self, final_score):
        self.username = ''
        self.final_score = final_score
        self.background_image = pygame.transform.scale(pygame.image.load('../public/tela_GAMEOVER.jpeg'), (600, 600))

    def morte(self):
        pygame.init()
        tela = pygame.display.set_mode((600, 600))
        pygame.display.set_caption(f'GAME OVER')
        clock = pygame.time.Clock()
        font = pygame.font.SysFont(None, 30)

        data = []

        try:
            with open('score.txt') as score_file:
                data = json.load(score_file)
        except:
            pass

        async def main():
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        with open('score.txt', 'w') as score_file:
                            json.dump(data, score_file)
                        pygame.quit()
                        exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            self.username = self.username[:-1]
                        if event.key == pygame.K_RETURN:
                            data.update({"Player": self.username, "Score": self.final_score})
                        else:
                            self.username += event.unicode

                tela.fill((48, 10, 36))  # Cor de Fundo da Tela
                tela.blit(self.background_image, (0, 0))
                tela.blit(font.render(f'DIGITE SEU NOME', True, (0, 255, 1)), (200, 375))
                text_surface = font.render(self.username, True, (255, 255, 255))
                tela.blit(text_surface, (200, 400))

                pygame.display.update()
                clock.tick(120)

                await asyncio.sleep(0)
        asyncio.run(main())


if __name__ == '__main__':
    i = GameOver(10)
    i.morte()

"""
    
    
    
    x_tela = 600
    y_tela = 600
    player_health = 100
    player_velocity = 0.75
    pistol_damage = 20
    shotgun_damage = 10
    sniper_damage = 90
    shotgun_enable = True
    sniper_enable = True
    player = [player_health, player_velocity, pistol_damage, shotgun_damage, sniper_damage, shotgun_enable, sniper_enable]
    enemys1 = [5, 2, 3, 1, 0]  # 5 zumbis, 2 morcegos, 3 magos, 1 slime_king, 0 slimes (sao instanciados na morte do king)
    pontuacao = 500  # exemplo de pontuacao que foi obtida em round anterior
    arena = Arena(player, enemys1, x_tela, y_tela, pontuacao)
    arena.play()
    
    
    
    
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
    pontuacao = 0
    round1 = Round(player, enemys1, x_tela, y_tela)
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
"""

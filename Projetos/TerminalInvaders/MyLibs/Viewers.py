import pygame
from Controlers import *


class GameScreen:
    def __init__(self):
        self.pontuacao = 0
        self.player_health = 100
        self.player_velocity = 0.75
        self.pistol_damage = 200
        self.shotgun_damage = 10
        self.sniper_damage = 90
        self.tamanho_tela = 500
        self.shotgun_enable = False
        self.sniper_enable = False
        self.enemy_list = [[6, 0, 0, 0, 0],
                           [8, 0, 0, 0, 0],
                           [10, 0, 0, 0, 0],
                           [6, 2, 0, 0, 0],
                           [8, 3, 0, 0, 0],
                           [8, 5, 0, 0, 0],
                           [5, 4, 2, 0, 0],
                           [6, 6, 3, 0, 0],
                           [8, 6, 4, 0, 0],
                           [5, 5, 4, 2, 0],
                           [8, 5, 5, 3, 0],
                           [10, 6, 5, 4, 0]]  # [zombie, bat, mage, king_slime, slime]
        self.round_num = 0
        self.player = [self.player_health, self.player_velocity, self.pistol_damage,
                       self.shotgun_damage, self.sniper_damage, self.shotgun_enable, self.shotgun_enable]
        self.round = Arena(self.player, self.enemy_list[self.round_num], self.tamanho_tela,
                           self.tamanho_tela, self.pontuacao)
        self.current_round = None
        self.upgrade = Upgrade(self.player, self.tamanho_tela)
        self.user_name = ''

    def update_screen(self, pontuacao_adicional, vida):
        self.pontuacao = pontuacao_adicional
        self.player_health = vida
        self.round_num += 1
        if self.round_num == 5:
            self.shotgun_enable = True
        if self.round_num == 8:
            self.sniper_enable = True
        self.player = [self.player_health, self.player_velocity, self.pistol_damage,
                       self.shotgun_damage, self.sniper_damage, self.shotgun_enable, self.shotgun_enable]
        self.round = Arena(self.player, self.enemy_list[self.round_num], self.tamanho_tela,
                           self.tamanho_tela, self.pontuacao)

    def gameplay(self):
        pygame.init()
        while True:
            self.current_round = self.round.play()
            if isinstance(self.current_round, tuple):
                self.update_screen(self.current_round[0], self.current_round[1])
                self.player = Upgrade(self.player, self.tamanho_tela).update_parameters()[0]
            elif isinstance(self.current_round, int):
                return GameOver(self.pontuacao).morte()
            pygame.event.clear()


class MainScreen:
    def __init__(self, game_screen, leader_board):
        self.play = game_screen
        self.placar_local = leader_board

    def tela_inicial(self):
        pass


if __name__ == '__main__':
    teste = GameScreen()
    i = teste.gameplay()
    print(i)

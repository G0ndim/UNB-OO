import pygame as pg

pg.init()

class Jogador:
    def __init__(self, vida, estamina, velocidade, pontuacao=0):
        self._vida = vida
        self._estamina = estamina
        self.velocidade = velocidade
        self.armas = list()
        self.player_skin = '../public/mario_sprite.png'
        self.pontuacao = pontuacao
        self.localizacao = ()
        # self.aparencia = pg.image.load()




class Inimigo:
    def __init__(self, vida, velocidade, pontos, dano, posicao):
        self.vida = vida
        self.velocidade = velocidade
        self.pontos = pontos
        self.dano = dano
        self.pos_inimigo = posicao
        self.enemy_skin = ''

    def ataque(self):
        pass

    def movimento(self):
        pass

class Zumbi(Inimigo):
    def __init__(self, vida, velocidade, pontos, dano, posicao):
        super().__init__(self, vida, velocidade, pontos, dano, posicao)
        self.enemy_skin = '../public/zombie.png'



class Arma:
    pass

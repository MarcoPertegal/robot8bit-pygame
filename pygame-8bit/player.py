import pygame
from sprites import *
import maps
from sounds import *
import random

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_skins
        pygame.sprite.Sprite.__init__(self, self.groups)

        #COlocar al player en el centro de la pantalla de 800 por 600
        self.x, self.y = 400, 300
        self.width, self.height = TILESIZE, TILESIZE

        self.x_change = 0
        self.y_change = 0
        self.facing = "down"
        self.animation_loop = 1

        self.image = self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.x, self.y

    def movement(self):
        keys = pygame.key.get_pressed()
        #Para que el jugador se mantenga en el centro y el mapa se mueva
        if keys[pygame.K_LEFT]:
            for sprite in self.game.all_skins:
                sprite.rect.x += PLAYER_SPEED
            self.x_change -= PLAYER_SPEED
            self.facing = 'left'
        if keys[pygame.K_RIGHT]:
            for sprite in self.game.all_skins:
                sprite.rect.x -= PLAYER_SPEED
            self.x_change += PLAYER_SPEED
            self.facing = 'right'
        if keys[pygame.K_UP]:
            for sprite in self.game.all_skins:
                sprite.rect.y += PLAYER_SPEED
            self.x_change -= PLAYER_SPEED
            self.facing = 'up'
        if keys[pygame.K_DOWN]:
            for sprite in self.game.all_skins:
                sprite.rect.y -= PLAYER_SPEED
            self.y_change += PLAYER_SPEED
            self.facing = 'down'

    def update(self):
        self.movement()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0
import pygame
from config import *
from sounds import *
from player import *
from map_build import *
import maps
from sprites import *

import sys

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.groundsheet = Spritesheet('assets/gound4.png')
        self.character_spritesheet = Spritesheet('assets/character2.png')
        self.wallsheet = Spritesheet('assets/spikes.png')
        self.lavasheet = Spritesheet('assets/lava.png')
    def createTileMap(self, tilemap):
        build_map(self, tilemap)

    def new(self, tilemap):
        self.playing = True
        self.all_skins = pygame.sprite.LayeredUpdates()
        self.walls = pygame.sprite.LayeredUpdates()
        self.lava = pygame.sprite.LayeredUpdates()
        self.createTileMap(tilemap)


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        self.all_skins.update()

    def draw(self):
        self.screen.fill("black")
        self.all_skins.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()

    def main(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()

        """self.running = False"""

    def game_over(self):
        pass

    def intro_screen(self):
        pass

#Creacion del mapa y del bucle del juego
TILEMAP = maps.world_1.stage_1
game = Game()
game.new(TILEMAP)
while game.running:
    game.main()

pygame.quit()

import pygame
from skins import *
from config import *
import sys


class Spritesheet:
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))
        return sprite


class Ground(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = 1
        self.groups = self.game.all_skins
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width, self.height = TILESIZE, TILESIZE
        self.image = self.game.groundsheet.get_sprite(0, 96, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.x, self.y


def build_map(self, tilemap):
    for i, row in enumerate(tilemap):
        for j, column in enumerate(row):
            Ground(self, j, i)


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.groundsheet = Spritesheet('assets/ground.png')

    def createTileMap(self, tilemap):
        build_map(self, tilemap)

    def new(self, tilemap):
        self.playing = True
        self.all_skins = pygame.sprite.LayeredUpdates()
        self.createTileMap(tilemap)

        """
        self.rocks = pygame.sprite.LayeredUpdates()
        self.player = Player(self, 1, 2)"""

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


game = Game()
game.new(TILEMAP)
while game.running:
    game.main()

pygame.quit()

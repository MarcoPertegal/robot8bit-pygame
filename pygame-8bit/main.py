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
        self.font = pygame.font.Font('assets/game_font.ttf', 32)
        self.groundsheet = Spritesheet('assets/gound4.png')
        self.character_spritesheet = Spritesheet('assets/character2.png')
        self.wallsheet = Spritesheet('assets/spikes.png')
        self.lavasheet = Spritesheet('assets/lava.png')
        self.intro_background = pygame.image.load("assets/intro_background.png")
        self.game_background = pygame.image.load("assets/game_background.PNG")
        self.diamondsheet = Spritesheet('assets/diamond.png')
        self.bombsheet = Spritesheet('assets/bomb2.png')
        self.shieldsheet = Spritesheet('assets/shiled.png')
        self.healsheet = Spritesheet('assets/heal.png')
        self.character_suit = Spritesheet('assets/character_suit.png')
    def createTileMap(self, tilemap):
        build_map(self, tilemap)

    def new(self, tilemap):
        self.playing = True
        self.all_skins = pygame.sprite.LayeredUpdates()
        self.walls = pygame.sprite.LayeredUpdates()
        self.lava = pygame.sprite.LayeredUpdates()
        self.diamond = pygame.sprite.LayeredUpdates()
        self.bomb = pygame.sprite.LayeredUpdates()
        self.shield = pygame.sprite.LayeredUpdates()
        self.heal = pygame.sprite.LayeredUpdates()
        self.shield = pygame.sprite.LayeredUpdates()
        self.createTileMap(tilemap)


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        self.all_skins.update()

    def draw(self):
        self.screen.blit(self.game_background, (0,0))
        self.all_skins.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()

    def main(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def game_over(self):
        self.intro_screen("Restart")


    def restart_game(self):
        self.all_skins.empty()
        self.walls.empty()
        self.lava.empty()
        self.new(TILEMAP)

    def intro_screen(self, startresume):
        intro = True

        title = self.font.render("Main menu", True, "black")
        title_rect = title.get_rect(x=200, y=100)

        play_button = Button(SCREEN_WIDTH/2-BTN_W/2, 200, BTN_W, BTN_H, 'black', 'gray', f"{startresume} Game", 32)
        exit_button = Button(SCREEN_WIDTH/2-BTN_W/2, 400, BTN_W, BTN_H, 'black', 'gray', "Exit Game", 32)

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if play_button.is_pressed(mouse_pos, mouse_pressed):
                intro = False
                self.running = True
                self.playing = True

            elif exit_button.is_pressed(mouse_pos, mouse_pressed):
                self.running = False
                pygame.quit()
                sys.exit()

            self.screen.blit(self.intro_background, (0,0))
            self.screen.blit(title, title_rect)
            self.screen.blit(play_button.image, play_button.rect)
            self.screen.blit(exit_button.image, exit_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()


#Creacion del mapa y del bucle del juego
world_instance = maps.world_1()
objects,TILEMAP = world_instance.load_map()
print(TILEMAP)
#print(objects)
game = Game()
game.intro_screen("Start")
game.new(TILEMAP)
while game.running:
    game.main()

pygame.quit()
sys.exit()

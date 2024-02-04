import pygame

import player
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
        self.font = pygame.font.Font(game_font, 32)
        self.groundsheet = Spritesheet(ground_sprite)
        self.character_spritesheet = Spritesheet(character_default_sprite)
        self.wallsheet = Spritesheet(wall_sprite)
        self.lavasheet = Spritesheet(lava_sprite)
        self.intro_background = pygame.image.load(intro_background_sprite)
        self.game_background = pygame.image.load(game_background_sprite)
        self.diamondsheet = Spritesheet(diamond_sprite)
        self.bombsheet = Spritesheet(bomb_sprite)
        self.shieldsheet = Spritesheet(shield_sprite)
        self.healsheet = Spritesheet(heal_sprite)
        self.character_suit = Spritesheet(character_suit_sprite)
        self.background_sound = background_sound
        self.playing = True
        self.all_skins = pygame.sprite.LayeredUpdates()
        self.walls = pygame.sprite.LayeredUpdates()
        self.lava = pygame.sprite.LayeredUpdates()
        self.diamond = pygame.sprite.LayeredUpdates()
        self.bomb = pygame.sprite.LayeredUpdates()
        self.shield = pygame.sprite.LayeredUpdates()
        self.heal = pygame.sprite.LayeredUpdates()
        self.shield = pygame.sprite.LayeredUpdates()
        self.total_diamonds = objects.get('D', 0)
        self.background_sound = background_sound
        self.gameover_sound = gameover_sound
        self.gameover_sound_played = False

    def createTileMap(self, tilemap):
        build_map(self, tilemap)

    def new(self, tilemap):
        self.createTileMap(tilemap)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        self.all_skins.update()
        self.check_victory_condition()

    def draw(self):
        self.screen.blit(self.game_background, (0, 0))
        self.all_skins.draw(self.screen)
        self.draw_health_bar()
        self.draw_inventory()
        self.clock.tick(FPS)
        pygame.display.update()

    def main(self):
        while self.playing:
            self.events()
            self.Player.handle_bomb_usage()
            self.update()
            self.draw()

    def game_over(self):
        if not self.gameover_sound_played:
            self.play_gameover_sound()
            self.gameover_sound_played = True

        self.stop_background_sound()

        game_over_text = self.font.render("Game Over!", True, "red")
        game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 50))

        restart_button = Button(SCREEN_WIDTH / 2 - BTN_W / 2, SCREEN_HEIGHT / 2, BTN_W, BTN_H, 'black', 'gray',
                                "Restart Game", 32)
        exit_button = Button(SCREEN_WIDTH / 2 - BTN_W / 2, SCREEN_HEIGHT / 2 + 200, BTN_W, BTN_H, 'black', 'gray',
                             "Exit Game", 32)

        game_over = True
        while game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = False
                    self.running = False

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if restart_button.is_pressed(mouse_pos, mouse_pressed):
                game_over = False
                self.running = True
                self.playing = True
                self.restart_game()

            elif exit_button.is_pressed(mouse_pos, mouse_pressed):
                self.running = False
                pygame.quit()
                sys.exit()

            self.screen.blit(self.game_background, (0, 0))
            self.screen.blit(game_over_text, game_over_rect)
            self.screen.blit(restart_button.image, restart_button.rect)
            self.screen.blit(exit_button.image, exit_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()

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

            self.screen.blit(self.intro_background, (0, 0))
            self.screen.blit(title, title_rect)
            self.screen.blit(play_button.image, play_button.rect)
            self.screen.blit(exit_button.image, exit_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()

    def draw_health_bar(self):
        background_rect = pygame.Rect(SCREEN_WIDTH - 200, 10, 200, 20)
        background_color = (0, 0, 0)
        pygame.draw.rect(self.screen, background_color, background_rect)

        bar_width = int((self.Player.live_points / 200) * 200)
        bar_height = 20
        bar_color = (255, 0, 0)
        bar_rect = pygame.Rect(SCREEN_WIDTH - bar_width, 10, bar_width, bar_height)
        pygame.draw.rect(self.screen, bar_color, bar_rect)

    def draw_inventory(self):
        inventory_start_x = SCREEN_WIDTH - 220
        inventory_start_y = 40

        for i, (obj_type, count) in enumerate(self.Player.inventory.items()):
            obj_text = self.font.render(f"{obj_type}: {count}", True, (255, 255, 255))
            obj_text_rect = obj_text.get_rect(topleft=(inventory_start_x, inventory_start_y + i * 30))
            self.screen.blit(obj_text, obj_text_rect)

    def check_victory_condition(self):
        if self.Player.inventory["diamond"] == self.total_diamonds:
            self.victory_screen()

    def start_game(self):
        start_resume_option = "Start"
        self.intro_screen(start_resume_option)
        self.play_background_sound()
        self.new(TILEMAP)
        while self.running:
            self.main()

    def victory_screen(self):
        self.stop_background_sound()
        victory = True

        victory_text = self.font.render("Congratulations! You have won!", True, "black")
        victory_rect = victory_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 50))

        restart_button = Button(SCREEN_WIDTH / 2 - BTN_W / 2, SCREEN_HEIGHT / 2, BTN_W, BTN_H, 'black', 'gray',
                                "Restart Game", 32)
        exit_button = Button(SCREEN_WIDTH / 2 - BTN_W / 2, SCREEN_HEIGHT / 2 + 200, BTN_W, BTN_H, 'black', 'gray',
                             "Exit Game", 32)

        while victory:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    victory = False
                    self.running = False

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if restart_button.is_pressed(mouse_pos, mouse_pressed):
                victory = False
                self.running = True
                self.playing = True
                self.new(TILEMAP)
                self.restart_game()

            elif exit_button.is_pressed(mouse_pos, mouse_pressed):
                self.running = False
                pygame.quit()
                sys.exit()

            self.screen.blit(self.game_background, (0, 0))
            self.screen.blit(victory_text, victory_rect)
            self.screen.blit(restart_button.image, restart_button.rect)
            self.screen.blit(exit_button.image, exit_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()

    def restart_game(self):
        self.stop_background_sound()
        self.all_skins.empty()
        self.walls.empty()
        self.lava.empty()
        self.diamond.empty()
        self.bomb.empty()
        self.shield.empty()
        self.heal.empty()
        objects, TILEMAP = world_instance.load_map()
        self.new(TILEMAP)
        self.play_background_sound()

    def play_background_sound(self):
        pygame.mixer.music.load(self.background_sound)
        pygame.mixer.music.play(-1)

    def stop_background_sound(self):
        pygame.mixer.music.stop()

    def play_gameover_sound(self):
        pygame.mixer.Sound(self.gameover_sound).play()




world_instance = maps.world_1()
objects,TILEMAP = world_instance.load_map()
print(TILEMAP)
print(objects)

game = Game()
game.start_game()
game.new(TILEMAP)
while game.running:
    game.main()

pygame.quit()
sys.exit()

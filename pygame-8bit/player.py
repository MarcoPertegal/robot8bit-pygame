import pygame
from sprites import *
import sys
import maps
from sounds import *
import random

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_skins
        self.live_points = 200
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
        self.inventory = {"diamond": 0, "bomb": 0, "shield": 0, "heal": 0}
        self.heal_sound = healing_sound
        self.bomb_sound = bomb_sound
        self.shield_active = False
        self.shield_key_pressed = False
        self.bomb_key_pressed = False

        Player_animation(self)
    def movement(self):
        keys = pygame.key.get_pressed()
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
            self.y_change -= PLAYER_SPEED
            self.facing = 'up'
        if keys[pygame.K_DOWN]:
            for sprite in self.game.all_skins:
                sprite.rect.y -= PLAYER_SPEED
            self.y_change += PLAYER_SPEED
            self.facing = 'down'

    def update(self):
        self.movement()
        self.animate()
        self.collide_objects()
        self.rect.x += self.x_change
        self.collide_walls("X")
        self.rect.y += self.y_change
        self.collide_walls("Y")
        self.handle_shield_activation()
        self.collide_lava()

        self.x_change = 0
        self.y_change = 0

    def collide_walls(self, direction):
        if direction == 'X':
            hits = pygame.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.x_change > 0:
                    for sprite in self.game.all_skins:
                        sprite.rect.x += PLAYER_SPEED
                    self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_change < 0:
                    for sprite in self.game.all_skins:
                        sprite.rect.x -= PLAYER_SPEED
                    self.rect.x = hits[0].rect.right
                self.live_points -= 1
                print(self.live_points)
                if self.live_points <= 0:
                    self.kill()
                    self.game.game_over()

        if direction == 'Y':
            hits = pygame.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.y_change > 0:
                    for sprite in self.game.all_skins:
                        sprite.rect.y += PLAYER_SPEED
                    self.rect.y = hits[0].rect.top - self.rect.height
                if self.y_change < 0:
                    for sprite in self.game.all_skins:
                        sprite.rect.y -= PLAYER_SPEED
                    self.rect.y = hits[0].rect.bottom
                self.live_points -= 1
                print(self.live_points)
                if self.live_points <= 0:
                    self.kill()
                    self.game.game_over()

    def collide_lava(self):
        if not self.shield_active:
            hits = pygame.sprite.spritecollide(self, self.game.lava, False)
            if hits:
                self.live_points -= 0.5

            if self.live_points <= 0:
                self.kill()
                self.game.game_over()

    def animate(self):
        Player_animation_animate(self)

    def collect_object(self, obj_type):
        if obj_type in self.inventory:
            self.inventory[obj_type] += 1
            print(f"Collected {obj_type} - Total: {self.inventory[obj_type]}")
            self.healing(obj_type)

    def healing(self, obj_type):
        if obj_type == "heal":
            self.live_points += 50
            self.heal_sound.play()
            if self.live_points > 200:
                self.live_points = 200
            print(f"Healed! Current Health: {self.live_points}")


    def collide_objects(self):
        object_hits = pygame.sprite.spritecollide(self, self.game.diamond, True)
        for obj in object_hits:
            self.collect_object("diamond")

        object_hits = pygame.sprite.spritecollide(self, self.game.bomb, True)
        for obj in object_hits:
            self.collect_object("bomb")

        object_hits = pygame.sprite.spritecollide(self, self.game.shield, True)
        for obj in object_hits:
            self.collect_object("shield")

        object_hits = pygame.sprite.spritecollide(self, self.game.heal, True)
        for obj in object_hits:
            self.collect_object("heal")


    def activate_shield(self):
        if self.inventory["shield"] > 0:
            self.shield_active = True
            print("Shield activated!")

    def deactivate_shield(self):
        self.shield_active = False
        print("Shield deactivated!")

    def handle_shield_activation(self):
        keys = pygame.key.get_pressed()
        current_shield_key_state = keys[pygame.K_t]

        if current_shield_key_state and not self.shield_key_pressed:
            if self.inventory["shield"] > 0:
                if not self.shield_active:
                    self.activate_shield()
                else:
                    self.deactivate_shield()

        self.shield_key_pressed = current_shield_key_state


    def use_bomb(self):
        if self.inventory["bomb"] > 0:
            self.inventory["bomb"] -= 1
            self.bomb_sound.play()
            for sprite in self.game.walls:
                if abs(sprite.rect.x - self.rect.x) <= 2 * TILESIZE and abs(sprite.rect.y - self.rect.y) <= 2 * TILESIZE:
                    sprite.kill()

            for sprite in self.game.shield:
                if abs(sprite.rect.x - self.rect.x) <= 2 * TILESIZE and abs(sprite.rect.y - self.rect.y) <= 2 * TILESIZE:
                    sprite.kill()

    def handle_bomb_usage(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_b] and not self.bomb_key_pressed:
            self.bomb_key_pressed = True
            self.use_bomb()
        elif not keys[pygame.K_b]:
            self.bomb_key_pressed = False


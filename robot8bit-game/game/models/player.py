from game.models.rock import Rock
import pygame


class Player():
    def __init__(self, player_skin):
        self.position = [100, 60]
        self.speed = 10
        self.size = [50, 50]
        self.player_skin = player_skin
        self.life = 10

    def move_right(self):
        self.position[0] += self.speed

    def move_left(self):
        self.position[0] -= self.speed

    def move_up(self):
        self.position[1] -= self.speed

    def move_down(self):
        self.position[1] += self.speed

    def check_collision(self, rock: Rock):
        player_rect = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])
        rock_rect = pygame.Rect(rock.position[0], rock.position[1], rock.size[0], rock.size[1])

        if player_rect.colliderect(rock_rect):
            return True
        return False

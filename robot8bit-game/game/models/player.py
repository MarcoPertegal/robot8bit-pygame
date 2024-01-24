from game.models.obstacle import Obstacle

class Player():
    def __init__(self, skin):
        self.position = [100, 60]
        self.speed = 10
        self.size = [50, 50]
        self.skin = skin
        self.life = 10

    def move_right(self):
        self.position[0] += self.speed

    def move_left(self):
        self.position[0] -= self.speed

    def move_up(self):
        self.position[1] -= self.speed

    def move_down(self):
        self.position[1] += self.speed

    def check_collision(self, obstacle: Obstacle):
        if (self.position[0] == obstacle.position[0] and
        self.position[1] == obstacle.position[1]):
            return True
        return False
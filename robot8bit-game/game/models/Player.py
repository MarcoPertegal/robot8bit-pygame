"""class Player():
    def __init__(self):
        self.position = [0, 0]
        self.speed = 10

    def move_right(self):
        self.position[0] += self.speed


player_one = Player()

while game_running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_one.move_right()
            if event.key == pygame.K_LEFT:
                player_one.move_left()


class Obstacle():
    def __init__(self):
        self.position = [100, 100]
        self.size = [20, 20]
player_one = Player()
obstacle = Obstacle()
def check_collision(player, obstacle):
  if (player.position[0]  obstacle.position[0] and
      player.position[1]  obstacle.position[1]):
    return True
  return False"""
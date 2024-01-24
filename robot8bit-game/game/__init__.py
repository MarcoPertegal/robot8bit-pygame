import pygame
from game.models.player import Player
from game.models.obstacle import Obstacle

pygame.init()

#Imagenes
bg = pygame.image.load("../assets/background.png")
skin = pygame.image.load("../assets/skin.png")
obstacle = pygame.image.load("../assets/obstacle.png")

#Skin player
scaled_skin = pygame.transform.scale(skin, (120, 120))
player_one = Player(scaled_skin)

#Obstaculo
scaled_obstacle = pygame.transform.scale(obstacle, (100, 70))
obstacle = Obstacle(scaled_obstacle)

#Pantalla
screen = pygame.display.set_mode((1100, 620))

#Puntuacion
font = pygame.font.Font(None, 36)
score = 0

running = True

while running:
    for event in pygame.event.get():
        #Moviemiento
            keys = pygame.key.get_pressed()
            if keys[pygame.K_d]:
                #intento de colision con la piedra parece que el metodo siempre devuelve false
                if not player_one.check_collision(obstacle):
                    #para que el player no pueda salirse de la pantalla
                    if player_one.position[0] + player_one.size[0] < screen.get_width():
                        player_one.move_right()
            if keys[pygame.K_a]:
                if player_one.position[0] > 0:
                    player_one.move_left()
            if keys[pygame.K_w]:
                if player_one.position[1] > 0:
                    player_one.move_up()
            if keys[pygame.K_s]:
                if player_one.position[1] + player_one.size[1] < screen.get_height():
                    player_one.move_down()

    #pintar pantalla y fondo
    screen.blit(bg, (0, 0))

    # pintar la skin
    screen.blit(player_one.skin, (player_one.position[0], player_one.position[1]))

    # pintar obstacle
    screen.blit(obstacle.skin,
                     (obstacle.position[0], obstacle.position[1]))

    #La puntuacion
    text = font.render("Score: " + str(score), 1, (10, 10, 10))
    screen.blit(text, (10, 10))

    pygame.display.flip()

    if event.type == pygame.QUIT:
        running = False

pygame.quit()
"""

#HACER que nose salga la bola de la pantalla disminuir tamaño imagen y pintar al player
screen = pygame.display.set_mode((1100, 620))
bg = pygame.image.load("../assets/background.png")
skin = pygame.image.load("../assets/skin.png")
clock = pygame.time.Clock()
running = True
player_one = Player(skin)
dt = 0

#Se divide entre dos para que empiece en el medio de la pantalla
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    #para el juego si le damos a la cruz para salir
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.blit(bg, (0, 0))

    pygame.draw.circle(screen, "black", player_pos, 40)


    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()"""
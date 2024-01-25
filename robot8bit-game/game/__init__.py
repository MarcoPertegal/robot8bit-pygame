import pygame
from game.models.player import Player
from game.models.rock import Rock

pygame.init()

# Imagenes
bg = pygame.image.load("../assets/background.png")
player_skin = pygame.image.load("../assets/skin.png")
obstacle_skin = pygame.image.load("../assets/rock.png")

# Skin player
player_one = Player(player_skin)

# Obstaculo
rock = Rock(obstacle_skin)

# Pantalla
screen = pygame.display.set_mode((1100, 620))

# Puntuacion
font = pygame.font.Font(None, 36)
score = 0

# Posicion inicial del player
player_initial_pos = [(screen.get_width() - player_one.size[0]) // 2, (screen.get_height() - player_one.size[1]) // 2]
player_one.position = player_initial_pos

running = True

while running:
    for event in pygame.event.get():
        # Problema cuando el player esta junto a la piedra no deja moverse, EL JUSGO SE BUGGEA AL MOVER EL RATON
        #ver para hacer cuadriculas porque sino el personaje se puede quedar entre dos cuadrados y daproblemasRub
        # herencia con obstacle
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            new_x = player_one.position[0] + player_one.speed
            if new_x + player_one.size[0] < screen.get_width() and not player_one.check_collision(rock):
                player_one.move_right()
        if keys[pygame.K_a]:
            if player_one.position[0] > 0:
                player_one.move_left()
        if keys[pygame.K_w]:
            new_x = player_one.position[1] + player_one.speed
            if new_x + player_one.size[0] < screen.get_width() and not player_one.check_collision(rock):
                player_one.move_up()
        if keys[pygame.K_s]:
            if player_one.position[1] + player_one.size[1] < screen.get_height():
                player_one.move_down()

#Se necesitaria un mapa precargado y haciendo uso de un COMO MURO Y PINCHE TIENE LOS MISMOS ATRIBUTOS HABRIA QUE HACER HERENCIA
#
    # pintar pantalla y fondo
    screen.blit(bg, (0, 0))

    # pintar la skin
    screen.blit(player_one.player_skin, (player_one.position[0], player_one.position[1]))

    # pintar obstacle
    screen.blit(rock.obstacle_skin, (rock.position[0], rock.position[1]))

    # La puntuacion
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

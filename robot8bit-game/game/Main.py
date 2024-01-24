import pygame
pygame.init()
#HACER que nose salga la bola de la pantalla disminuir tamaño imagen y pintar al player
screen = pygame.display.set_mode((1280, 720))
bg = pygame.image.load("../assets/background.png")
sprite = pygame.image.load("../assets/player.png")
clock = pygame.time.Clock()
running = True
dt = 0

#Se divide entre dos para que empiece en el medio de la pantalla
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    #para el juego si le damos a la cruz para salir
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #fondo ver como poner el background mui
    """
    if player_pos.y < 300:
        screen.fill("grey")
    else:
        screen.fill("red")"""

    screen.blit(bg, (-20, -20))

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

pygame.quit()
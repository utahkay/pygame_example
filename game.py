import pygame
from player import Player
from message_broker import Pulsar

def main():
    worldx = 960
    worldy = 720
    fps = 40  # frame rate
    ani = 4  # animation cycles
    world = pygame.display.set_mode([worldx, worldy])

    # backdrop = pygame.image.load(os.path.join('images', 'stage.png'))
    clock = pygame.time.Clock()
    pygame.init()
    # backdropbox = world.get_rect()
    main_flag = True

    player = Player("upside-down.png")  # spawn player
    player.rect.x = 0  # go to x
    player.rect.y = 0  # go to y
    player_list = pygame.sprite.Group()
    player_list.add(player)

    '''
    Main Loop
    '''

    pulsar = Pulsar("video-game")
    consumer = pulsar.consumer("video-game")
    while True:
        msg = consumer.receive()
        command = msg.value()
        if command == "up":
            player.move_up()
        if command == "down":
            player.move_down()
        if command == "right":
            player.move_right()
        if command == "left":
            player.move_left()

        consumer.acknowledge(msg)

        # world.blit(backdrop, backdropbox)
        world.fill((0, 0, 0))
        player_list.draw(world)
        pygame.display.flip()
        clock.tick(fps)


# define a main function
def old_main():
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("./kitten.jpg")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")

    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((500, 500))

    avatar = pygame.image.load("upside-down.png")
    avatar = pygame.transform.scale(avatar, (80, 80))
    avatar_rect = avatar.get_rect()
    avatar_rect.x = 50
    avatar_rect.y = 50

    bomb = pygame.image.load("bomb.png")

    bomb_rect = bomb.get_rect()
    bomb_rect.x = 120
    bomb_rect.y = 120

    # define the position of the smiley
    step_x = 10
    step_y = 10

    # Draw the first screen
    screen.blit(avatar, avatar_rect)
    screen.blit(bomb, bomb_rect)
    pygame.display.flip()

    # define a variable to control the main loop
    running = True
    is_over = False

    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            if event.type == pygame.KEYDOWN and not is_over:
                if event.key == pygame.K_UP:
                    avatar_rect.y -= step_y
                if event.key == pygame.K_DOWN:
                    avatar_rect.y += step_y
                if event.key == pygame.K_LEFT:
                    avatar_rect.x -= step_x
                if event.key == pygame.K_RIGHT:
                    avatar_rect.x += step_x
                screen.fill((0, 0, 0))
                screen.blit(avatar, avatar_rect)
                screen.blit(bomb, bomb_rect)
                pygame.display.flip()
                print(f"Bomb: {bomb_rect.x}, {bomb_rect.y}")
                print(f"Avatar: {avatar_rect.x}, {avatar_rect.y}")
                is_over = avatar_rect.colliderect(bomb_rect)
                if is_over:
                    screen.fill((255, 0, 0))
                    pygame.display.flip()


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()

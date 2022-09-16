import pygame

import driver
from player import Player
from message_broker import Pulsar
from multiprocessing import Process


def main():
    player_name = input("What's your name?").strip()

    players = {

    }

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

    player = Player("upside-down.png", player_name)  # spawn player
    # p = Process(target=driver.drive, args=(player_name,))
    # p.start()

    players[player_name] = player
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
        _player_name = command.split(":")[0]
        position = command.split(":")[1]
        if _player_name == player_name:
            if position == "up":
                player.move_up()
            if position == "down":
                player.move_down()
            if position == "right":
                player.move_right()
            if position == "left":
                player.move_left()
        else:
            if _player_name in players:
                another_player = players[_player_name]
                if position == "up":
                    another_player.move_up()
                if position == "down":
                    another_player.move_down()
                if position == "right":
                    another_player.move_right()
                if position == "left":
                    another_player.move_left()
            else:
                # start another player
                another_player = Player("upside-down.png", _player_name)
                players[_player_name] = another_player  # spawn player
                another_player.rect.x = 0  # go to x
                another_player.rect.y = 0  # go to y
                player_list.add(another_player)

        consumer.acknowledge(msg)

        # world.blit(backdrop, backdropbox)
        world.fill((0, 0, 0))
        player_list.draw(world)
        pygame.display.flip()
        clock.tick(fps)


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()

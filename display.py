import pygame
from player import Player
from message_broker import Pulsar
import time


def receive_messages(consumer, msg):
    msg_str = msg.data().decode('utf-8')
    _player_name = msg_str.split(":")[0]
    position = msg_str.split(":")[1]
    print(msg_str)

    if _player_name in players:
        _player = players[_player_name]
        if position == "up":
            _player.move_up()
        if position == "down":
            _player.move_down()
        if position == "right":
            _player.move_right()
        if position == "left":
            _player.move_left()


def display():
    worldx = 960
    worldy = 720
    fps = 40  # frame rate
    ani = 4  # animation cycles
    world = pygame.display.set_mode([worldx, worldy])

    # backdrop = pygame.image.load(os.path.join('images', 'stage.png'))
    clock = pygame.time.Clock()
    pygame.init()

    pulsar = Pulsar("video-game")
    consumer = pulsar.consumer_with_callback("video-game", receive_messages)

    # Loop forever
    while True:
        world.fill((0, 0, 0))
        player_list.draw(world)
        pygame.display.flip()
        clock.tick(fps)


if __name__ == "__main__":
    fps = 1  # frame rate
    ani = 4  # animation cycles
    world = pygame.display.set_mode([960, 720])

    player1 = Player("upside-down.png", "kay")  # spawn player
    player2 = Player("upside-down.png", "lishen")  # spawn player
    # p = Process(target=driver.drive, args=(player_name,))
    # p.start()
    players = {
        "kay": player1,
        "lishen": player2
    }

    player1.rect.x, player1.rect.y = (0, 0)
    player2.rect.x, player2.rect.y = (400, 400)
    player_list = pygame.sprite.Group()
    player_list.add(player1)
    player_list.add(player2)

    display()

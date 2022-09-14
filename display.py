import pygame
from player import Player
from message_broker import Pulsar
import time


def receive_messages(consumer, msg):
    msg_str = msg.data().decode('utf-8')
    print(msg_str)


def display():
    # worldx = 960
    # worldy = 720
    # fps = 40  # frame rate
    # ani = 4  # animation cycles
    # world = pygame.display.set_mode([worldx, worldy])
    #
    # # backdrop = pygame.image.load(os.path.join('images', 'stage.png'))
    # clock = pygame.time.Clock()
    # pygame.init()

    pulsar = Pulsar("video-game")
    consumer = pulsar.consumer_with_callback("video-game", receive_messages)

    # Loop forever
    while True:
        time.sleep(10)


if __name__ == "__main__":
    display()

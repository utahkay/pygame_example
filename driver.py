import pygame
from message_broker import Pulsar


def main():
    pulsar = Pulsar("video-game")
    pygame.init()

    main_flag = True
    while main_flag:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                main_flag = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    print("up")
                    pulsar.send_message("up")
                if event.key == pygame.K_DOWN:
                    print("down")
                    pulsar.send_message("down")
                if event.key == pygame.K_LEFT:
                    print("left")
                    pulsar.send_message("left")
                if event.key == pygame.K_RIGHT:
                    print("right")
                    pulsar.send_message("right")


if __name__ == "__main__":
    main()

import pygame


class Player(pygame.sprite.Sprite):
    """
    Spawn a player
    """

    def __init__(self, avatar_path: str, name: str):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.name = name

        img = pygame.image.load(avatar_path).convert()
        img = pygame.transform.scale(img, (80, 80))

        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()

        self.distance = 15

    def move_up(self):
        self.rect.y -= self.distance

    def move_down(self):
        self.rect.y += self.distance

    def move_left(self):
        self.rect.x -= self.distance

    def move_right(self):
        self.rect.x += self.distance


if __name__ == "__main__":
    pass
    # player = Player()
    # screen = pygame.display.set_mode((500, 500))

import pygame, sys
from player import Player
from npcs import Beata, Beata2, Pinky, Ring, Middle, Index, Thumb


class BaseScene:

    def __init__(self):
        self.player = Player(self, 10, 10)
        self.x = 1280
        self.y = 720
        self.screen = pygame.display.set_mode((self.x, self.y))
        self.bg = pygame.image.load("assets/bg_hill.png")
        self.npcs = []

    def play(self):
        pygame.init()
        pygame.display.set_caption("the koń fajny game")
        close = False
        while not close:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
            self.screen.blit(self.bg, (0, 0))
            self.running()
            self.player.move()
            self.player.display()
            pygame.display.update()

    def running(self):
        pass

    def door(self, position):
        img = pygame.image.load("assets/door.png")
        self.screen.blit(img, position)
        if self.player.rect.topright[0] > position[0]:
            if (self.player.x) < (position[0] + 64):
                if self.player.rect.bottomright[1] > position[1]:
                    if (self.player.y) < (position[1] + 64):
                        return True


class HillScene(BaseScene):
    def __init__(self):
        super().__init__()
        self.bg = pygame.image.load("assets/bg_hill.png")
        self.npcs = [Beata(self, 680, 210)]
        self.player = Player(self, 10, 400)

    def running(self):
        for npc in self.npcs:
            if npc.disappear == False:
                npc.display()
            else:
                self.screen.blit(pygame.image.load("assets/g.png"), (0, 0))
                if self.door((1230, 335)):
                    HandScene().play()


class HillScene2(HillScene):
    def __init__(self):
        super().__init__()
        self.player = Player(self, 950, 400)
        self.npcs = [Beata2(self, 680, 210)]


class HandScene(BaseScene):
    def __init__(self):
        super().__init__()
        self.bg = pygame.image.load("assets/bg_hand.png")
        self.player = Player(self, 100, 100)
        self.npcs = [
            Pinky(self, 341, 188),
            Ring(self, 383, 112),
            Middle(self, 530, 70),
            Index(self, 665, 145),
            Thumb(self, 815, 300),
        ]
        self.door_open = False

    def running(self):
        for npc in self.npcs:
            if npc.disappear == False:
                npc.display()
        if self.door_open:
            if self.door((0, 335)):
                HillScene2().play()

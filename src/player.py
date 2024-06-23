import pygame


class Player(object):
    def __init__(self, game, x, y):
        self.game = game
        self.img = pygame.image.load("assets/horseright.png")
        self.rect = self.img.get_rect()
        self.leftImg = pygame.image.load("assets/horseleft.png")
        self.rightImg = pygame.image.load("assets/horseright.png")
        self.x = x
        self.y = y
        self.speed = 300
        self.clock = pygame.time.Clock()
        self.next = (x, y)

    def move(self):
        v = self.clock.tick(60) / 1000
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.next = (self.x - self.speed * v, self.y)
            self.img = self.leftImg
        if keys[pygame.K_d]:
            self.next = (self.x + self.speed * v, self.y)
            self.img = self.rightImg
        if keys[pygame.K_w]:
            self.next = (self.x, self.y - self.speed * v)
        if keys[pygame.K_s]:
            self.next = (self.x, self.y + self.speed * v)

        if (
            not self.is_in_collision_with_boundaries()
            and not self.is_in_collision_with_npc()
        ):
            self.rect.topleft = self.next
            self.x, self.y = self.next

    def display(self):
        self.game.screen.blit(self.img, self.rect.topleft)

    def is_in_collision_with_boundaries(self):
        if self.next[0] < 0:
            return True
        elif self.next[1] < 0:
            return True
        elif self.next[0] > (self.game.x - 241):
            return True
        elif self.next[1] > (self.game.y - 319):
            return True

    def is_in_collision_with_npc(self):
        for npc in self.game.npcs:
            if npc.disappear == False:
                if self.next[0] + 241 > npc.rect.topleft[0]:
                    if self.next[0] < npc.rect.topright[0]:
                        if self.next[1] + 319 > npc.rect.topleft[1]:
                            if self.next[1] < npc.rect.bottomright[1]:
                                return True

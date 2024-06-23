import pygame


class Dialog_box(object):

    def __init__(self, npc):
        self.img = pygame.image.load("assets/dialog_box.png")
        self.rect = self.img.get_rect()
        self.npc = npc

    def display_text(self, text, pos, size):
        font = pygame.font.Font("freesansbold.ttf", size)
        txt = font.render(text, True, (255, 255, 255))
        rect = txt.get_rect()
        rect.topleft = pos
        self.npc.game.screen.blit(txt, rect)

    def talk(self, main_text, answer1, answer2=" ", main_text2=""):
        i = 0
        while i == 0:
            self.npc.game.player.display()
            self.npc.game.screen.blit(self.img, (0, 480))
            self.display_text(self.npc.name + ": " + main_text, (10, 490), 20)
            self.display_text(main_text2, (10, 520), 20)
            self.display_text("1: " + answer1, (15, 590), 15)
            if answer2 != " ":
                self.display_text("2: " + answer2, (15, 650), 15)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        i = 1
                    if answer2 != " ":
                        if event.key == pygame.K_2:
                            i = 2

            pygame.display.update()
        return i

import pygame, sys
from dialog_box import Dialog_box


class Npc(object):
    def __init__(self, game, x, y):
        self.img = pygame.image.load("assets/beata.png")
        self.rect = self.img.get_rect()
        self.rect.topleft = (x, y)
        self.game = game
        self.distance = 270
        self.dialog = Dialog_box(self)
        self.disappear = False

    def display(self):
        self.game.screen.blit(self.img, self.rect.topleft)
        if self.game.player.is_in_collision_with_npc():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.talk()

    def talk(self):
        pass


class Beata(Npc):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.name = "Beata"

    def talk(self):
        a = self.dialog.talk("...", "Hejka", "Cześć")
        if a == 1:
            hi = "Hejka"
        if a == 2:
            hi = "Cześć"
        b = self.dialog.talk(
            hi
            + ", boze ja juz mam dosyc moich rodzicow nie akceptuja mojej odmiennosci muj tata powiedzial ze wyrzuci",
            "nie obchodzi mnie to",
            "aha a czemu cie nie akceptuja?",
            "mnie z domu bo nie jestem taka jak oni mam dosyc",
        )
        if b == 2:
            self.dialog.talk("bo jezdze konno", "no słabo", "rozumiem")
        c = self.dialog.talk(
            "koniu pamietasz jak grales ze mn w remika wczoraj?", "nie", "tak"
        )
        if c == 1:
            self.dialog.talk(
                "no to gralismy w remika wczoraj i przegrales", "aha, faktycznie"
            )
        self.dialog.talk(
            "no a gralismy ze kto przegrywa to sobie musi wyrwac paznokcie",
            "no ale jak ja mam sobie wyrwać jak ja nie mam ręki nawet, jestem koniem",
        )
        self.dialog.talk("sluchaj", "...")
        self.dialog.talk(
            "ty masz rękę, musisz ją tylko znaleźć", "jak niby mam ją znaleźć?"
        )
        e = self.dialog.talk("musisz wejsc w glab siebie", "w głąb siebie?", "oki")
        if e == 1:
            self.dialog.talk("tak, musisz wejść w głąb siebie", "oki")
        self.disappear = True


class Beata2(Beata):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.name = "Beata"

    def talk(self):
        self.dialog.talk(
            "koniuuu, co ty robisz?", "słuchaj, wyrwałem wszystkie paznokcie"
        )
        self.dialog.talk(
            "super koniu, wygrałeś tę grę, jesteś najlepszy", "dziękuję <3"
        )
        sys.exit(0)


class Pinky(Npc):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.name = "Mały palec"
        self.img = pygame.image.load("assets/npc_rect.png")

    def talk(self):
        self.dialog.talk("...", "cześć, muszę oderwać ci paznokcia")
        self.dialog.talk("słuchaj, wcale nie musisz tego robić", "muszę")
        self.dialog.talk(
            "wcale nie musisz tego robić, jeszcze nie jest za późno", "muszę"
        )
        self.dialog.talk(
            "nie musisz tego robić, przecież nie jesteś złym koniem",
            "jestem bardzo złym koniem",
        )
        self.dialog.talk(
            "będziesz miał mnie na sumieniu do końca życia, nie chcesz tak skończyć",
            "nie chcę tego robić, ale muszę",
        )
        self.disappear = True
        self.game.bg = pygame.image.load("assets/blood1.png")


class Ring(Npc):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.name = "Serdeczny palec"
        self.img = pygame.image.load("assets/npc_rect.png")

    def talk(self):
        self.dialog.talk("...", "cze, muszę oderwać ci paznokcia")
        self.dialog.talk(
            "proszę, okaż litość, tak bardzo się boję", "nie ma czego się bać"
        )
        self.dialog.talk("to musi być okropny ból", "co tyy, nie może być aż tak źle")
        self.dialog.talk(
            "proszęęęęę, naprawdę jestem przerażony",
            "uwierz mi na słowo, że ból wcale nie jest taki zły",
        )
        self.dialog.talk(
            "po prostu mnie zostaw, błagam", "przepraszam, ale muszę to zrobić"
        )

        self.game.bg = pygame.image.load("assets/blood2.png")
        self.game.screen.blit(self.game.bg, (0, 0))
        self.game.screen.blit(self.game.player.img, self.game.player.rect.topleft)
        pygame.display.update()

        self.dialog.talk(
            "to było najgorsze na świecie, możesz dla mnie zrobić coś żebym poczuł się lepiej?",
            "no jasne, co chcesz?",
        )
        self.dialog.talk(
            "nienawidzę środkowego palca. chciałbym żeby on też poczuł najgorszy na świecie ból",
            "nie ma sprawy",
        )
        self.dialog.talk(
            "niech ból będzie jedyną rzeczą, którą będzie czuł, to sprawi mi przyjemność",
            "oki",
        )
        self.disappear = True


class Middle(Npc):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.name = "Środkowy palec"
        self.img = pygame.image.load("assets/npc_rect.png")

    def talk(self):
        self.dialog.talk("follow g0sie on instagram pls", "oki", "ale ja nie chcę")
        self.dialog.talk(
            "FOLLOW G0SIE, FOLLOW G0SIE, FOLLOW G0SIE",
            "słuchaj, ciebie to mi nawet nie szkoda",
        )
        self.game.bg = pygame.image.load("assets/blood3.png")
        self.disappear = True


class Index(Npc):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.name = "Wskazujący palec"
        self.img = pygame.image.load("assets/npc_rect.png")

    def talk(self):
        self.dialog.talk("hejka, co tam?", "muszę ci sprawić ból")
        self.dialog.talk("ból? uwielbiam ból!", "muszę wyrwać ci paznokcia")
        self.dialog.talk("o taaak, to brzmi jak wielki ból", "dziwny jesteś")
        self.dialog.talk(
            "ból to cudowne uczucie. gdy jest wystarczająco mocny to zapominam o wszystkim innym",
            "...",
        )
        self.dialog.talk(
            "jeśli ból jest najsilniejszym uczuciem na świecie, to nie ma nic cudowniejszego",
            "oki, da się zrobić",
            "zobaczę",
            "proszę, odrywaj wolno, bym mógł się jak najdłużej rozkoszować bólem",
        )
        self.game.bg = pygame.image.load("assets/blood4.png")
        self.disappear = True


class Thumb(Npc):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)
        self.name = "Kciuk"
        self.img = pygame.image.load("assets/npc_rect.png")

    def talk(self):
        self.dialog.talk("...", "siemka, muszę ci wyrwać paznokcia")
        self.dialog.talk("okej", "to będzie bardzo bolało")
        a = self.dialog.talk("whatever", "nie boisz się bólu?", "oki to wyrywam")
        if a == 1:
            self.dialog.talk(
                "a czego tu się bać? ból to tylko jedno z odczuć w świadomości",
                "no i co z tego?",
            )
            self.dialog.talk(
                "życie nie ma sensu, jestem tylko jednym z 14 milionów kciuków",
                "miliardów",
            )
            self.dialog.talk(
                "wolna wola to tylko iluzja, w rzeczywistości moje życie zależy od jakiegoś konia,",
                "to moja sprawa w co gram",
                "wygrałbym, ale zabrakło mi dwóch oczek tylkoo",
                "który jest uzależniony od gry w remika",
            )
            self.dialog.talk(
                "mój strach nic nie zmieni, mogę tylko zaakceptować swój ból i cierpienie",
                "oki to wyrywam",
            )
        self.game.bg = pygame.image.load("assets/blood5.png")
        self.disappear = True
        self.game.door_open = True

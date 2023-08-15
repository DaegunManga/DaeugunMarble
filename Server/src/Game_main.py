import pygame as pg

class Game () :
    def __init__ (self) :
        pg.init() #시작
        pg.display.set_caption('server') #제목
        self.WindowSize = (960, 1200)
        self.Img_init()

    def Img_init (self) :
        self.background_img = pg.image.load('./Image/background.png', ) # 배경
        self.background_img = pg.transform.scale(self.background_img, self.WindowSize)

    def Size_init (self) :
        pass

    def main_game (self) :
        screen = pg.display.set_mode(self.WindowSize)
        fps = pg.time.Clock()

        while True :
            screen.blit(self.background_img, (0, 0))
            screen.fill((255,255,255))
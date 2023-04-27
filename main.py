#File Created by Isaac Leon 


# This file was created by: Chris Cozort
# Sources: http://kidscancode.org/blog/2016/08/pygame_1-1_getting-started/
# Sources: 

# import libs
import pygame as pg
import os
# import settings 
from settings import *
from sprites import *
from os import path
# from pg.sprite import Sprite

# set up assets folders

'''
goal: Fall down the screen and say "you loose" and try to make a new platorm that disappears. 
'''

# create game class in order to pass properties to the sprites file

class Game:
    def __init__(self):
        # init game window etc.
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("my game")
        self.clock = pg.time.Clock()
        self.running = True
        print(self.screen)

    def load_data(self):
        self.player_img = pg.image.load(path.join(img_folder, "Doodle jump")).convert()

    def new(self):
        # starting a new game
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.player = Player(self)
        self.plat1 = Platform(WIDTH, 50, 0, HEIGHT-50, (150,150,150), "normal")
        # self.plat1 = Platform(WIDTH, 50, 0, HEIGHT-50, (150,150,150), "normal")
        self.all_sprites.add(self.plat1)
        self.platforms.add(self.plat1)
        
        self.all_sprites.add(self.player)
        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        for i in range(0,10):
            m = Mob(20,20,(0,255,0))
            self.all_sprites.add(m)
            self.enemies.add(m)
        self.run()

    def load_data(self):
        self.player_img = pg.image.load(path.join(img_folder, "Doodle Jump.jpg")).convert()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()
    def update(self):
        self.all_sprites.update()
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                # These two platforms will not disappear, they are my safe zones. 
                if hits[0].variant == "normal":
                    hits[0].kill()
                    # No matter how may times I hit them, they will not kill me (lose)
                elif hits[0].variant == "normal":
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = -PLAYER_JUMP
                else:
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0
                if not self.win:
            # self.draw_text(str(self.player.rot), 24, WHITE, WIDTH/2, HEIGHT/2)
                    self.update(str("YOU LOSE"), 50, RED, WIDTH/2, HEIGHT/2)
            #This says that as long as I am on a platform I am winning 
                if self.win == pg.sprite.spritecollide(self.player, self.platforms, False):
                    self.update("YOU WIN THE LOTTERY!", 24, WHITE, WIDTH/2, HEIGHT/2)

    def draw(self):
        
        self.screen.fill(BLUE)
        self.draw_text("GAME ON", 100, BLACK, WIDTH/2, HEIGHT/2)
        self.all_sprites.draw(self.screen)
        # Winning = I am on a platform 
        self.win = (pg.sprite.spritecollide(self.player, self.platforms, False))
        # This says as long as I am not on a platform, I am loosing or I just lost ebcuase the platforms on the bottom will dissappear
    
        # is this a method or a function?
        pg.display.flip()
    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)
    def get_mouse_now(self):
        x,y = pg.mouse.get_pos()
        return (x,y)

# instantiate the game class...
g = Game()

# kick off the game loop
while g.running:
    g.new()

pg.quit()
